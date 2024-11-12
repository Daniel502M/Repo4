import time

from fastapi import FastAPI
import psycopg2

from database import engine
from models import Base

from users import users_router


Base.metadata.create_all(bind=engine)


while True:
    try:
        conn = psycopg2.connect(
            user='postgres',
            password='password',
            database='testtest',
            port=5432,
            host='localhost'
        )

        cursor = conn.cursor()
        print("Database connection successfully!")
        break
    except Exception as err:
        print(err)
        time.sleep(3)


app = FastAPI()


@app.get("/")
def main():
    return "Home"


app.include_router(users_router)
