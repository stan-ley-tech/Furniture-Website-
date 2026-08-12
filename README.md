# Elite Wood Furniture

A full-stack e-commerce website for Elite Wood Furniture, a solid-wood furniture retailer. The design language draws on modern minimalist furniture-retail conventions (clean grid layouts, generous whitespace, editorial product presentation) — all code, copy, and visual assets are original to this project.

## Stack

- **Frontend:** [SvelteKit](https://svelte.dev/docs/kit) (TypeScript)
- **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (Python)

## Project structure

```
Furniture-Website-/
├── frontend/           SvelteKit app
│   └── src/
│       ├── routes/      pages
│       └── lib/         components, API client
├── backend/             FastAPI app
│   └── app/
│       ├── main.py      app entrypoint
│       ├── routers/     API routes
│       └── models/      Pydantic models
└── README.md
```

## Getting started

### Backend (FastAPI)

```bash
cd backend
python -m venv venv
source venv/Scripts/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8001
```

API runs at `http://127.0.0.1:8001`. Interactive docs at `http://127.0.0.1:8001/docs`.

### Frontend (SvelteKit)

```bash
cd frontend
npm install
cp .env.example .env   # points the frontend at the backend API
npm run dev
```

The dev server prints the local URL (defaults to `http://localhost:5173`, but will pick the next free port if that one is taken).

## Notes for the client

- **Photography and video are temporary stock, not final product assets.** Images/video under `frontend/static/images/` and `frontend/static/videos/` are free-to-use stock media from [Pexels](https://www.pexels.com) (Pexels License — free for commercial use, no attribution required), standing in for real furniture/lifestyle photography and a real workshop video. Replace them with actual shoots before launch: swap the files in `frontend/static/images/products/`, `frontend/static/images/categories/`, `frontend/static/images/sections/`, and `frontend/static/videos/`, and update the `image` field in `backend/app/routers/products.py` (or the future database) to match.
- **The logo is a placeholder mark**, not a designed brand identity — a simple "EW" monogram (`frontend/src/lib/components/Logo.svelte`, also used as the favicon at `frontend/src/lib/assets/favicon.svg`). Commission real logo design before launch.
- The product catalog currently lives in-memory in `backend/app/routers/products.py`. Swap this for a real database (e.g. PostgreSQL) before launch.
- **Cart, search, sign-in, and checkout are real but client-side only** — no backend involved. The cart (`frontend/src/lib/cart.ts`) persists to `localStorage` and actually works (add/remove/update quantity, badge count, checkout summary); search filters the live product catalog; but there's no real authentication, payment processing, inventory reservation, or order storage behind any of it. Wire these to real backend endpoints (auth, payments, orders) before launch.
- **The newsletter, consultation, and contact forms are UI only** — they don't submit anywhere yet, just show an inline confirmation client-side. Wire these to real backend endpoints (email delivery, CRM) before launch.
- **Contact details are placeholders** (`frontend/src/routes/contact/+page.svelte`) — replace the email, phone, and showroom address with real ones.
- **Policy pages (Shipping & Returns, Warranty, Sustainability, Careers, FAQ) have starter copy**, written to be directionally correct for a solid-wood furniture business but not reviewed against your actual policies — have someone confirm the specifics (timelines, fees, warranty terms) before launch.
- **Catalog has 20 products, 4 per category** (Living Room, Dining Room, Bedroom, Storage, Outdoor) — enough to make navigation and listing pages feel real, but still placeholder inventory (names, prices, and descriptions are invented). Add real inventory, pricing, and photography before launch; category pages with no products show a graceful "check back soon" message rather than breaking.
- **WhatsApp button and social links use placeholder contacts.** The floating WhatsApp button (`frontend/src/lib/components/WhatsAppButton.svelte`) links to `wa.me/254700000000` (the same placeholder number as the contact page); the footer's Instagram/TikTok icons link to `instagram.com/elitewoodfurniture` and `tiktok.com/@elitewoodfurniture`, which are guessed handles, not confirmed real accounts. Replace all three with real ones before launch.

### Stock media sources (temporary)

| File | Source |
| --- | --- |
| `videos/craft-hero.mp4` | [Pexels video 5973221](https://www.pexels.com/video/a-person-working-on-wood-5973221/) |
| `images/categories/living-room.jpg` | [Pexels photo 6636320](https://www.pexels.com/photo/cozy-living-room-interior-with-wooden-furniture-and-comfy-couch-6636320/) |
| `images/categories/dining-room.jpg` | [Pexels photo 3968056](https://www.pexels.com/photo/brown-wooden-dining-table-and-chairs-3968056/) |
| `images/categories/bedroom.jpg` | [Pexels photo 5824522](https://www.pexels.com/photo/classic-bedroom-interior-with-wooden-furniture-and-antique-carpets-5824522/) |
| `images/categories/outdoor.jpg` | [Pexels photo 8180361](https://www.pexels.com/photo/wooden-furniture-on-wooden-platform-8180361/) |
| `images/products/anders-oak-dining-table.jpg` | [Pexels photo 534172](https://www.pexels.com/photo/brown-wooden-dining-table-with-beige-pendant-lamp-534172/) |
| `images/products/marlow-boucle-lounge-chair.jpg` | [Pexels photo 16269026](https://www.pexels.com/photo/houseplants-by-the-window-and-next-to-an-armchair-in-a-room-16269026/) |
| `images/products/haven-walnut-bookshelf.jpg` | [Pexels photo 2883049](https://www.pexels.com/photo/photo-of-a-wooden-bookshelf-2883049/) |
| `images/sections/design-consultation.jpg` | [Pexels photo 6583355](https://www.pexels.com/photo/hand-of-a-person-holding-wooden-plank-samples-6583355/) |
| `images/sections/our-craft.jpg` | [Pexels photo 5974283](https://www.pexels.com/photo/focused-artisan-making-hole-on-plank-with-hammer-and-chisel-5974283/) |
| `images/sections/meet-sutton.jpg` | [Pexels photo 9220877](https://www.pexels.com/photo/brown-padded-armchairs-beside-the-glass-window-9220877/) |
| `images/products/willow-platform-bed.jpg` | [Pexels photo 7303688](https://www.pexels.com/photo/messy-bed-7303688/) |
| `images/products/cedar-adirondack-chair.jpg` | [Pexels photo 11586228](https://www.pexels.com/photo/brown-wooden-armchair-11586228/) |
| `images/products/harlow-linen-sofa.jpg` | [Pexels photo 12474787](https://www.pexels.com/photo/a-cozy-living-room-with-green-couch-12474787/) |
| `images/products/bruno-coffee-table.jpg` | [Pexels photo 18288703](https://www.pexels.com/photo/table-on-carpet-in-living-room-18288703/) |
| `images/products/windsor-dining-chair.jpg` | [Pexels photo 29917912](https://www.pexels.com/photo/minimalist-wooden-chair-design-in-modern-setting-29917912/) |
| `images/products/camden-dining-bench.jpg` | [Pexels photo 4044789](https://www.pexels.com/photo/wooden-table-and-benches-on-the-dining-room-4044789/) |
| `images/products/porter-counter-stool.jpg` | [Pexels photo 10557274](https://www.pexels.com/photo/a-stool-in-a-room-10557274/) |
| `images/products/elm-sideboard.jpg` | [Pexels photo 11112749](https://www.pexels.com/photo/photo-of-a-wooden-cabinet-11112749/) |
| `images/products/foster-media-console.jpg` | [Pexels photo 11112748](https://www.pexels.com/photo/close-up-of-a-wooden-console-table-11112748/) |
| `images/products/bellwood-armoire.jpg` | [Pexels photo 19050707](https://www.pexels.com/photo/wooden-wardrobe-in-living-room-19050707/) |
| `images/products/birch-nightstand.jpg` | [Pexels photo 5825694](https://www.pexels.com/photo/comfortable-bed-located-near-wooden-night-stand-in-sun-rays-5825694/) |
| `images/products/aspen-dresser.jpg` | [Pexels photo 30355552](https://www.pexels.com/photo/cozy-modern-bedroom-with-wooden-dresser-30355552/) |
| `images/products/linden-bedroom-bench.jpg` | [Pexels photo 12715495](https://www.pexels.com/photo/stylish-minimalist-bedroom-with-geometric-stools-and-bench-standing-next-to-bed-12715495/) |
| `images/products/teak-outdoor-dining-table.jpg` | [Pexels photo 17527772](https://www.pexels.com/photo/wooden-table-and-chairs-17527772/) |
| `images/products/cypress-garden-bench.jpg` | [Pexels photo 289445](https://www.pexels.com/photo/wooden-bench-in-garden-289445/) |
| `images/products/coastal-lounge-daybed.jpg` | [Pexels photo 879010](https://www.pexels.com/photo/brown-wooden-framed-with-white-mattress-hanging-bed-surrounded-by-green-grass-879010/) |

### Third-party assets

- **Font Awesome Free** (CDN, `frontend/src/app.html`) for nav icons — [Font Awesome Free License](https://fontawesome.com/license/free) (icons: CC BY 4.0, free for commercial use).
