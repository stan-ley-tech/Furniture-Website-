from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import products

app = FastAPI(title="Elite Wood Furniture API")

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"http://(localhost|127\.0\.0\.1):\d+",
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products.router)


@app.get("/api/health")
def health():
    return {"status": "ok"}
