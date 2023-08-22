import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core import get_app_settings
from db.events import connect_to_db, close_db_connection
from api.routes.api import router as api_router


def get_application() -> FastAPI:

    settings = get_app_settings()

    application = FastAPI(**settings.fastapi_kwargs)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allow_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # application.add_event_handler(
    #     "startup",
    #     connect_to_db,
    # )
    # application.add_event_handler(
    #     "shutdown",
    #     close_db_connection,
    # )

    application.include_router(api_router)

    return application


if __name__ == '__main__':
    app = get_application()
