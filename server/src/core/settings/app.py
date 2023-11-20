import logging
from typing import Any, Dict, List, Tuple

from pydantic_settings import BaseSettings
from pydantic import Field, PostgresDsn
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(".env"))


class AppSettings(BaseSettings):

    debug: bool = Field(alias='DEBUG')
    docs_url: str = "/"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = 'Link Shortener'
    version: str = '0.0.1'

    secret_key: str = Field(alias='SECRET_KEY')

    api_prefix: str = "/api/v1"

    allow_origins: List[str] = Field(alias='ALLOWED_HOSTS')

    logging_level: int = logging.INFO
    loggers: Tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")

    database_url: str = Field(alias='DATABASE_URL')
    min_connection_count: int = 5
    max_connection_count: int = 10

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
        }
