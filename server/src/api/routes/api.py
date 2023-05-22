from fastapi import APIRouter

from .endpoints import links_router, statistics_router

router = APIRouter()
router.include_router(links_router, tags=["links"], prefix="/links")
router.include_router(statistics_router, tags=[
                      "statistics"], prefix="/statistics")
