from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from database import Session, engine
from fastapi_jwt_auth import AuthJWT
from models import User, Order
from schemas import OrderModel
from fastapi.encoders import jsonable_encoder

order_router = APIRouter(
    prefix='/orders',
    tags=['orders']
)
session = Session(bind=engine)

@order_router.get('/')
async def order(Authorize: AuthJWT=Depends()):

    try:
        Authorize.jwt_required()

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid token')
    
    return {'message': "hello order"}

@order_router.post('/order', status_code=status.HTTP_200_OK)
async def add_orders(order: OrderModel, Authorize:AuthJWT=Depends()):
    try: 
        Authorize.jwt_required()

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid token')

    current_user =  Authorize.get_jwt_subject()
    user = session.query(User).filter(User.username == current_user).first()

    new_order=Order(
        pizza_size = order.pizza_size,
        quantity = order.quantity
    )

    new_order.user = user
    session.add(new_order)
    session.commit()

    response = {
        "pizza_size":new_order.pizza_size,
        "quantily": new_order.quantity,
        "id":new_order.id,
        "order_status":new_order.order_staus

    }

    return jsonable_encoder(response)