import logging
from typing import Any, Dict, List, Tuple

from .base import BaseAppSettings
from pydantic import PostgresDsn


class AppSettings(BaseAppSettings):

    debug: bool
    docs_url: str = "/"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = 'Link Shortener'
    version: str = '0.0.1'

    secret_key: str

    api_prefix: str = "/api/v1"

    allowed_hosts: List[str] = ['127.0.0.1:5173', 'localhost:5173']

    logging_level: int = logging.INFO
    loggers: Tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")

    database_url: PostgresDsn
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
