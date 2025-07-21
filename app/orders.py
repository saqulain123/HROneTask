from fastapi import APIRouter
from app.models import OrderCreate
from app.database import order_collection, product_collection
from bson import ObjectId

router = APIRouter()

@router.post("/orders", status_code=201)
def create_order(order: OrderCreate):
    result = order_collection.insert_one(order.dict())
    return {"id": str(result.inserted_id)}

@router.get("/orders/{user_id}")
def list_orders(user_id: str, limit: int = 10, offset: int = 0):
    cursor = order_collection.find({"userId": user_id}).skip(offset).limit(limit)
    orders = []

    for order in cursor:
        items = []
        for item in order["items"]:
            product = product_collection.find_one({"_id": ObjectId(item["productId"])})
            product_details = {
                "id": str(product["_id"]),
                "name": product["name"]
            } if product else {}

            items.append({
                "productDetails": product_details,
                "qty": item["qty"]
            })

        orders.append({
            "id": str(order["_id"]),
            "items": items,
            "total": sum(i["qty"] * product_collection.find_one({"_id": ObjectId(i["productId"])})["price"] for i in order["items"])
        })

    return {
        "data": orders,
        "page": {
            "next": offset + limit,
            "limit": limit,
            "previous": offset - limit
        }
    }
