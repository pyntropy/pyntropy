import psycopg
from fastapi import APIRouter, Request
import os

router = APIRouter(
    prefix="/modules",
    tags=["modules"]
)


# @router.get("/{module_id}")
def get_module(module_id: str):

    conn = psycopg.connect(
        host=os.environ.get('DB_HOST'),
        port=os.environ.get('DB_PORT'),
        dbname="pyntropy_db",
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
    )

    ь
    with conn.cursor() as cursor:

        query = """
            SELECT * FROM steps
            """

        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)

get_module("1")