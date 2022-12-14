from fastapi import APIRouter

from .endpoints import links_router

router = APIRouter()
router.include_router(links_router, tags=["links"], prefix="/links")
