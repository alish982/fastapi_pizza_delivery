from fastapi import APIRouter
from database import Session, engine

order_router = APIRouter(
    prefix='/orders',
    tags=['orders']
)

@order_router.get('/')
async def order():
    return {'message': "hello order"}