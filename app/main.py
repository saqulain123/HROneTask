from fastapi import FastAPI
from app.products import router as product_router
from app.orders import router as order_router

app = FastAPI()

app.include_router(product_router)
app.include_router(order_router)
