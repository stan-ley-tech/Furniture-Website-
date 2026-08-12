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
    Product(
        id=7,
        name="Harlow Linen Sofa",
        slug="harlow-linen-sofa",
        category="Living Room",
        price=245000.00,
        description="Three-seat sofa on a solid oak frame, upholstered in washed linen.",
        image="/images/products/harlow-linen-sofa.jpg",
    ),
    Product(
        id=8,
        name="Bruno Coffee Table",
        slug="bruno-coffee-table",
        category="Living Room",
        price=58000.00,
        description="Block-top coffee table in mixed hardwood on a slim steel base.",
        image="/images/products/bruno-coffee-table.jpg",
    ),
    Product(
        id=9,
        name="Windsor Dining Chair",
        slug="windsor-dining-chair",
        category="Dining Room",
        price=31000.00,
        description="Curved-back dining chair in solid oak, sold individually.",
        image="/images/products/windsor-dining-chair.jpg",
    ),
    Product(
        id=10,
        name="Camden Dining Bench",
        slug="camden-dining-bench",
        category="Dining Room",
        price=74500.00,
        description="Long-form bench in solid pine for the dining table, seats three.",
        image="/images/products/camden-dining-bench.jpg",
    ),
    Product(
        id=11,
        name="Porter Counter Stool",
        slug="porter-counter-stool",
        category="Dining Room",
        price=24900.00,
        description="Backless counter stool turned from solid beech.",
        image="/images/products/porter-counter-stool.jpg",
    ),
    Product(
        id=12,
        name="Elm Sideboard",
        slug="elm-sideboard",
        category="Storage",
        price=148000.00,
        description="Slatted-door sideboard in solid elm with woven rattan drawers.",
        image="/images/products/elm-sideboard.jpg",
    ),
    Product(
        id=13,
        name="Foster Media Console",
        slug="foster-media-console",
        category="Storage",
        price=132500.00,
        description="Low reclaimed-wood media console on castors, with three drawers.",
        image="/images/products/foster-media-console.jpg",
    ),
    Product(
        id=14,
        name="Bellwood Armoire",
        slug="bellwood-armoire",
        category="Storage",
        price=176000.00,
        description="Freestanding wardrobe in solid oak with adjustable interior shelving.",
        image="/images/products/bellwood-armoire.jpg",
    ),
    Product(
        id=15,
        name="Birch Nightstand",
        slug="birch-nightstand",
        category="Bedroom",
        price=42900.00,
        description="Compact two-drawer nightstand in solid birch.",
        image="/images/products/birch-nightstand.jpg",
    ),
    Product(
        id=16,
        name="Aspen Dresser",
        slug="aspen-dresser",
        category="Bedroom",
        price=154000.00,
        description="Six-drawer dresser in solid ash with woven cane fronts.",
        image="/images/products/aspen-dresser.jpg",
    ),
    Product(
        id=17,
        name="Linden Bedroom Bench",
        slug="linden-bedroom-bench",
        category="Bedroom",
        price=68500.00,
        description="Upholstered bench on hairpin legs, seats two at the foot of the bed.",
        image="/images/products/linden-bedroom-bench.jpg",
    ),
    Product(
        id=18,
        name="Teak Outdoor Dining Table",
        slug="teak-outdoor-dining-table",
        category="Outdoor",
        price=189000.00,
        description="Weather-ready teak dining table for six, finished for year-round outdoor use.",
        image="/images/products/teak-outdoor-dining-table.jpg",
    ),
    Product(
        id=19,
        name="Cypress Garden Bench",
        slug="cypress-garden-bench",
        category="Outdoor",
        price=51500.00,
        description="Solid cypress garden bench, weather-sealed for year-round outdoor use.",
        image="/images/products/cypress-garden-bench.jpg",
    ),
    Product(
        id=20,
        name="Coastal Lounge Daybed",
        slug="coastal-lounge-daybed",
        category="Outdoor",
        price=224000.00,
        description="Suspended outdoor daybed in a solid eucalyptus frame, hung from rope supports.",
        image="/images/products/coastal-lounge-daybed.jpg",
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
