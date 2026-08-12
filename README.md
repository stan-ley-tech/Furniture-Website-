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

### Third-party assets

- **Font Awesome Free** (CDN, `frontend/src/app.html`) for nav icons — [Font Awesome Free License](https://fontawesome.com/license/free) (icons: CC BY 4.0, free for commercial use).
