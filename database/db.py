from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:password@localhost/db')
Session = sessionmaker(engine)

new_metadata = MetaData()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()