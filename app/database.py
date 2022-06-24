from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time
import psycopg2

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:password@localhost/fastapi'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='root', password='password', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Connection was successful")
#         break
#     except Exception as error:
#         print("Connection to database failed")
#         print("Error: %s" % error)
#         time.sleep(3)

