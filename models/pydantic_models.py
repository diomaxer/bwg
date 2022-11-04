from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    sum: float


class Log(BaseModel):
    id: int
    user_id: int
    product_id: int
    product_amount: int


class Product(BaseModel):
    id: int
    title: str
    price: float
    amount: int


class Transaction(BaseModel):
    user_id: int
    product_id: int
    product_amount: int
