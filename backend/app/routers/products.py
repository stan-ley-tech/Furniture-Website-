from fastapi import APIRouter, HTTPException

from app.db import supabase
from app.models.product import Product

router = APIRouter(prefix="/api/products", tags=["products"])


@router.get("", response_model=list[Product])
def list_products(category: str | None = None):
    query = supabase.table("products").select("*").order("id")
    if category:
        query = query.ilike("category", category)
    result = query.execute()
    return result.data


@router.get("/{slug}", response_model=Product)
def get_product(slug: str):
    result = supabase.table("products").select("*").eq("slug", slug).limit(1).execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="Product not found")
    return result.data[0]
