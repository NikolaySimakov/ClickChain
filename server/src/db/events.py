
from fastapi import FastAPI

from core.settings import AppSettings
from .session import create_db_and_tables


async def connect_to_db() -> None:
    await create_db_and_tables()
    return None


def close_db_connection() -> None:
    pass
