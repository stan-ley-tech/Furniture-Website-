import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import products

app = FastAPI(title="Elite Wood Furniture API")

# Production frontend origin(s), e.g. "https://elite-wood-furniture.vercel.app".
# Comma-separated if there's more than one (e.g. a preview + production URL).
_frontend_origins = os.environ.get("FRONTEND_ORIGIN", "")
allow_origins = [origin.strip() for origin in _frontend_origins.split(",") if origin.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_origin_regex=r"http://(localhost|127\.0\.0\.1):\d+",
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products.router)


@app.get("/api/health")
def health():
    return {"status": "ok"}
