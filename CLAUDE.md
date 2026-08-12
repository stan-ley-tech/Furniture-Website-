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
