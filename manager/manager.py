from fastapi import HTTPException
from starlette import status

from database.db import Session
from models.pydantic_models import User, Product, Transaction
from service.service import DataBase


class ProductManager:
    @staticmethod
    async def get_product(product_id: int, session: Session) -> Product:
        product = await DataBase.get_product(product_id=product_id, session=session)
        if product:
            return Product(**product)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product doesn't exist")


class UserManager:

    @staticmethod
    async def get_user(user_id: int, session: Session) -> User:
        user = await DataBase.get_user(user_id=user_id, session=session)
        if user:
            return User(**user)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User doesn't exist")

    @staticmethod
    async def buy(transaction: Transaction, session: Session):
        user = await UserManager.get_user(user_id=transaction.user_id, session=session)
        product = await ProductManager.get_product(product_id=transaction.product_id, session=session)

        if product.amount - transaction.product_amount < 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not enough product")

        if user.sum < product.price * transaction.product_amount:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not enough money")

        await DataBase.buy(product=product, transaction=transaction, session=session)
