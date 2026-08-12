# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Elite Wood Furniture is a full-stack furniture e-commerce site: a SvelteKit frontend backed by a FastAPI (Python) API. The two live side by side in this monorepo and run as separate processes in development.

## Commands

### Backend (`backend/`)

```bash
cd backend
python -m venv venv
source venv/Scripts/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8001
```

- API base: `http://127.0.0.1:8001`
- Interactive OpenAPI docs: `http://127.0.0.1:8001/docs`
- No test suite exists yet.

### Frontend (`frontend/`)

```bash
cd frontend
npm install
npm run dev              # start dev server (Vite picks 5173 or next free port)
npm run build             # production build
npm run preview           # preview the production build
npm run check              # svelte-kit sync + svelte-check (type checking)
```

- No test suite exists yet.
- Requires `frontend/.env` (copy from `.env.example`) with `PUBLIC_API_BASE_URL` pointing at the backend.

## Architecture

- **Frontend/backend are fully decoupled.** The SvelteKit app never talks to a database directly — all product data flows through the FastAPI JSON API via `frontend/src/lib/api.ts`. When adding data-backed features, add/extend a FastAPI router rather than fetching third-party or file-based data from within Svelte routes.
- **Data loading pattern:** page-level `+page.ts` `load` functions call helpers in `src/lib/api.ts` (e.g. `getProducts`), which use SvelteKit's passed-in `fetch` so requests work correctly during SSR. `getProducts` swallows fetch errors and returns `[]` on failure so pages degrade gracefully (see the `+page.svelte` empty-state) instead of crashing — preserve this pattern for new API calls.
- **API base URL** is read via `$env/dynamic/public` (`PUBLIC_API_BASE_URL`), not hardcoded — required because the frontend and backend run on independently-assigned ports in dev.
- **Backend structure:** `app/main.py` wires up the FastAPI app, CORS, and routers. Routers live in `app/routers/` (currently `products.py`), Pydantic schemas in `app/models/`. The product catalog is currently an in-memory list in `app/routers/products.py` — this is a placeholder for a real database and should be swapped out before launch (see README "Notes for the client").
- **CORS is regex-based** (`allow_origin_regex` in `app/main.py`) matching any `localhost`/`127.0.0.1` port, since Vite's dev port isn't fixed (it shifts if 5173 is already in use).
- **Design system:** global theme (colors, typography, spacing) is defined once as CSS custom properties in `frontend/src/app.css` and imported in `+layout.svelte`. Reuse these tokens (`--color-*`, `--font-*`, `.btn`, `.container`, `.eyebrow`) rather than introducing new one-off styles, to keep the site visually consistent.
- **All photography/video is temporary stock** (Pexels — see README "Notes for the client" and the credits table), not real product/brand assets. Don't treat filenames or content as final.
- **Hero section is a layered stack**, not a single background image: a `<video>` background (`.hero-video`, `z-index: 0`) with a poster fallback, a darkening gradient (`.hero::before`, `z-index: 1`), and caption/overlay text (`z-index: 2`) on top — all absolutely positioned inside `.hero` (`position: relative`). When editing hero markup in `+page.svelte`, preserve this z-index ordering or the gradient/text will render behind the video. Video is hidden under `prefers-reduced-motion: reduce`, falling back to the `.hero` element's own `background-image`.
- **Logo:** `frontend/src/lib/components/Logo.svelte` is an inline SVG monogram (props: `size`), used in `Header.svelte` and duplicated as the static favicon at `frontend/src/lib/assets/favicon.svg`. It's a placeholder mark, not a designed identity — see README.
- **Icons** come from Font Awesome Free, loaded via CDN `<link>` in `frontend/src/app.html` (not an npm package) — use `<i class="fa-solid fa-...">` rather than adding a new icon library.
- **Categories are a single source of truth:** `frontend/src/lib/categories.ts` exports `categories` (slug, name, description, image) and `getCategory(slug)`. The homepage room tiles, `Header.svelte` nav, `Footer.svelte` shop links, and `/shop/[category]` all read from this file — add a new category here, not by hardcoding it in multiple components. Category `slug` (URL-friendly, e.g. `dining-room`) is distinct from `name` (e.g. `Dining Room`), which must match the backend `Product.category` string exactly (case-insensitive) since `/shop/[category]/+page.ts` filters via `getProducts(fetch, category.name)`.
- **Shop/product routing:** `/shop` (all products), `/shop/[category]` (filtered by category, 404s via `error(404, ...)` for unknown slugs), and `/products/[slug]` (detail page, also 404s on unknown slugs) all follow the same load pattern as the homepage — fetch in `+page.ts`, render in `+page.svelte`. `ProductCard.svelte` always links to `/products/{slug}`; pass `showDescription` to render the product description (used on listing pages, omitted on the homepage Best Sellers grid).
- **Gotcha — don't use the `padding: X 0 Y` shorthand on an element that also carries the `.container` class.** `.container` sets `padding: 0 var(--gutter)` for the side gutters; a scoped rule like `padding: 2rem 0 5rem` on the same element zeroes that gutter out (the `0` is left/right), pushing content flush to the viewport edge. This bug has hit multiple pages here — always use `padding-top`/`padding-bottom` (or repeat `var(--gutter)` explicitly) when adding vertical spacing to a `.container` element.
- **Static pages** (`/our-story`, `/sustainability`, `/careers`, `/contact`, `/shipping-returns`, `/warranty`, `/faq`) use the shared `.simple-page` class from `app.css` for consistent typography/width rather than per-page `<style>` blocks — reuse it for new brand/policy pages instead of restyling from scratch.
- **Consultation and contact forms are client-side only** (`/consultation`, `/contact`) — `onsubmit` just flips a `submitted` boolean to show a confirmation message; nothing is sent anywhere. There's no backend endpoint for form submissions yet.
- **Cart is a `localStorage`-backed Svelte store**, not backend state: `frontend/src/lib/cart.ts` exports `cart` (subscribe/add/remove/setQuantity/clear) plus derived `cartCount` and `cartTotal`. It works fully client-side — there's no order/session persistence on the server, so a cart doesn't survive across browsers/devices. `/checkout` reads directly from this store and calls `cart.clear()` on submit.
- **Header overlays (cart drawer, search) are controlled by a shared UI store**, not local component state: `frontend/src/lib/ui.ts` exports `cartOpen`/`searchOpen` booleans. `Header.svelte` only sets them; `CartDrawer.svelte`/`SearchOverlay.svelte` (rendered once in `+layout.svelte`, not inside `Header.svelte`) read them and render as `position: fixed` overlays with an `{#if}` block, closing on Escape (`svelte:window onkeydown`) or backdrop click. Follow this pattern (shared store + layout-level overlay) for any new header-triggered overlay rather than adding local state to `Header.svelte`.
- **Search is client-side substring filtering**, not a real search backend: `SearchOverlay.svelte` fetches the full catalog once via `getProducts()` on first open (cached in component state) and filters by name/category/description on every keystroke. Fine at this catalog size; would need a real search endpoint before the catalog grows large.
- **Dev-mode hydration is slow** (~5s cold, observed via Playwright) because SvelteKit dev serves an unbundled ES module graph — this is normal for `vite dev` and not present in production builds. When testing interactivity (clicks on Header buttons, etc.) immediately after a fresh page load, wait for the page to actually be interactive rather than assuming `networkidle` means hydration finished — clicking too early silently no-ops since event listeners aren't attached yet. This caused a large amount of test flakiness during development; it is not an application bug.
- **Catalog is 20 products, exactly 4 per category**, maintained by hand in `backend/app/routers/products.py` — there's no seeding script. When adding a product, pick a `category` value that exactly matches an existing entry in `frontend/src/lib/categories.ts` (case-insensitive) or it won't show up on that category's `/shop/[category]` page.
- **`WhatsAppButton.svelte`** is a fixed-position `<a href="wa.me/...">`, rendered once in `+layout.svelte` (not per-page) so it floats over every route. Its phone number is a placeholder shared with the contact page — see README.
