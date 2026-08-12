from fastapi import APIRouter, HTTPException

from app.models.product import Product

router = APIRouter(prefix="/api/products", tags=["products"])

PRODUCTS: list[Product] = [
    Product(
        id=1,
        name="Anders Oak Dining Table",
        slug="anders-oak-dining-table",
        category="Dining Room",
        price=168900.00,
        description="Solid white oak dining table with a hand-rubbed natural finish.",
        image="/images/products/anders-oak-dining-table.jpg",
    ),
    Product(
        id=2,
        name="Marlow Boucle Lounge Chair",
        slug="marlow-boucle-lounge-chair",
        category="Living Room",
        price=84400.00,
        description="Curved silhouette lounge chair upholstered in ivory boucle.",
        image="/images/products/marlow-boucle-lounge-chair.jpg",
    ),
    Product(
        id=3,
        name="Haven Walnut Bookshelf",
        slug="haven-walnut-bookshelf",
        category="Storage",
        price=116900.00,
        description="Five-tier open bookshelf in rich American walnut veneer.",
        image="/images/products/haven-walnut-bookshelf.jpg",
    ),
    Product(
        id=4,
        name="Sutton Wingback Chair",
        slug="sutton-wingback-chair",
        category="Living Room",
        price=78500.00,
        description="Hand-joined oak frame wingback chair, built for long reading afternoons.",
        image="/images/sections/meet-sutton.jpg",
    ),
    Product(
        id=5,
        name="Willow Platform Bed",
        slug="willow-platform-bed",
        category="Bedroom",
        price=189900.00,
        description="Low-profile platform bed in solid oak, no box spring required.",
        image="/images/products/willow-platform-bed.jpg",
    ),
    Product(
        id=6,
        name="Cedar Adirondack Chair",
        slug="cedar-adirondack-chair",
        category="Outdoor",
        price=45900.00,
        description="Weather-ready lounge chair hand-built from naturally durable cedar.",
        image="/images/products/cedar-adirondack-chair.jpg",
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
