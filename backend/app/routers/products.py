from fastapi import APIRouter, HTTPException

from app.models.product import Product

router = APIRouter(prefix="/api/products", tags=["products"])

PRODUCTS: list[Product] = [
    Product(
        id=1,
        name="Anders Oak Dining Table",
        slug="anders-oak-dining-table",
        category="Dining",
        price=1299.00,
        description="Solid white oak dining table with a hand-rubbed natural finish.",
        image="/images/products/anders-oak-dining-table.jpg",
    ),
    Product(
        id=2,
        name="Marlow Boucle Lounge Chair",
        slug="marlow-boucle-lounge-chair",
        category="Living Room",
        price=649.00,
        description="Curved silhouette lounge chair upholstered in ivory boucle.",
        image="/images/products/marlow-boucle-lounge-chair.jpg",
    ),
    Product(
        id=3,
        name="Haven Walnut Bookshelf",
        slug="haven-walnut-bookshelf",
        category="Storage",
        price=899.00,
        description="Five-tier open bookshelf in rich American walnut veneer.",
        image="/images/products/haven-walnut-bookshelf.jpg",
    ),
]


@router.get("", response_model=list[Product])
def list_products(category: str | None = None):
    if category:
        return [p for p in PRODUCTS if p.category.lower() == category.lower()]
    return PRODUCTS


@router.get("/{slug}", response_model=Product)
def get_product(slug: str):
    for product in PRODUCTS:
        if product.slug == slug:
            return product
    raise HTTPException(status_code=404, detail="Product not found")
