from sqlalchemy.orm import Session

from fastapi import FastAPI, Depends
from database.db import get_db
from manager.manager import UserManager
from models.pydantic_models import Transaction

app = FastAPI()


@app.post("/")
async def root(transaction: Transaction, session: Session = Depends(get_db)):
   return await UserManager.buy(transaction=transaction, session=session)
