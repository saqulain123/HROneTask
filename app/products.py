from fastapi import APIRouter, Request, Query
from app.models import ProductCreate
from app.database import product_collection
from bson import ObjectId

router = APIRouter()

@router.post("/products", status_code=201)
def create_product(product: ProductCreate):
    result = product_collection.insert_one(product.dict())
    return {"id": str(result.inserted_id)}

@router.get("/products")
def list_products(
    name: str = Query(None),
    size: str = Query(None),
    limit: int = 10,
    offset: int = 0
):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["sizes.size"] = size

    products_cursor = product_collection.find(query).skip(offset).limit(limit)
    products = []
    for p in products_cursor:
        products.append({
            "id": str(p["_id"]),
            "name": p["name"],
            "price": p["price"]
        })

    return {
        "data": products,
        "page": {
            "next": offset + limit,
            "limit": limit,
            "previous": offset - limit
        }
    }
