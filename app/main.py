from typing import Optional, List
from fastapi import Body, Depends, FastAPI, Response, status, HTTPException
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import get_db, engine
from .routers import post, user, auth


models.Base.metadata.create_all(bind=engine)
app = FastAPI()

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


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get('/')
def root():
    return {"message": "Hello World"}
