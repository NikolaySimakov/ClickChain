import logging
from typing import Any, Dict, List, Tuple

from .base import BaseAppSettings
from pydantic import PostgresDsn

import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(os.path.dirname(os.path.dirname(current)))
sys.path.append(parent)

from config import DATABASE_URL, SECRET_KEY, DEBUG, ALLOWED_HOSTS


class AppSettings(BaseAppSettings):

    debug: bool = DEBUG
    docs_url: str = "/"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = 'Link Shortener'
    version: str = '0.0.1'

    secret_key: str = SECRET_KEY

    api_prefix: str = "/api/v1"

    allow_origins: List[str] = ALLOWED_HOSTS

    logging_level: int = logging.INFO
    loggers: Tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")

    database_url: PostgresDsn = DATABASE_URL
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
