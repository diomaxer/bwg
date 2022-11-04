from sqlalchemy import text

from database.db import Session
from models.pydantic_models import Transaction, Product


class DataBase:

    @staticmethod
    async def get_user(user_id: int, session: Session):
        print(user_id)
        return session.execute(f"SELECT * from users WHERE id = {user_id}").first()

    @staticmethod
    async def get_product(product_id: int, session: Session):
        return session.execute(f"SELECT * from products WHERE id = {product_id}").first()

    @staticmethod
    async def buy(transaction: Transaction, product: Product, session: Session):
        session.execute(text(f"UPDATE products SET amount = amount - {transaction.product_amount} WHERE id = {transaction.product_id}"))
        session.execute(text(f"UPDATE users SET sum = sum - {product.price * transaction.product_amount} WHERE id = {transaction.user_id}"))
        session.execute(text(f"INSERT INTO logs (user_id, product_id, product_amount) VALUES ({transaction.user_id}, {transaction.product_id}, {transaction.product_amount})"))
        session.commit()