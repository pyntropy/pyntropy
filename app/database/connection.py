import psycopg
from psycopg.rows import dict_row
from app.config import settings


def get_connection_string():
    return f"""
        host={settings.DB_HOST},
        port={settings.DB_PORT},
        dbname={settings.DB_NAME},
        user={settings.DB_USER},
        password={settings.DB_PASSWORD}
    """


async def get_async_connection():
    """
    Создает и возвращает асинхронное подключение к БД
    :return:
    """
    conn = await psycopg.AsyncConnection.connect(
        get_connection_string(),
        row_factory=dict_row)
    return conn


def get_sync_connection():
    """
    Создает и возвращает синхронное подключение к БД
    :return:
    """
    conn = psycopg.connect(
        get_connection_string(),
        row_factory=dict_row
    )
    return conn
