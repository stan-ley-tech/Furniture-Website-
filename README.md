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

- Product photography is currently placeholder color blocks — swap in real product photos under `frontend/static/images/products/` and update the `image` field in `backend/app/routers/products.py` (or the future database) once photography is available.
- The product catalog currently lives in-memory in `backend/app/routers/products.py`. Swap this for a real database (e.g. PostgreSQL) before launch.
