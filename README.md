# bwg

Я думал что проверка будет с моего компьютера, так что не использовал alembic, а создал бд вручную

CREATE TABLE products(
    id serial,
    title varchar,
    price float
)

CREATE TABLE users(
    id serial,
    username varchar,
    price float
)

CREATE TABLE logs(
    id serial,
    user_id int,
    product_id int,
    product_amount int
)
Так же в модуле database.db необходимо прописать подключение к бд
И установить зависимости

  pip install -r requirements.txt

Запускается сервис командой

    uvicorn main:app --relaod 
    
 
 Местоположение сервиса 
  
    localhost:8000/docs
    
 Чтобы совершить покупку необходимо отправить POST запрос на localhost:8000/
 
   {
    "user_id": 3,
    "product_id": 1,
    "product_amount": 1
   }
