from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from ..core import get_app_settings

engine = create_async_engine(
    get_app_settings().database_url, echo=True)
async_session = sessionmaker(bind=engine, class_=AsyncSession,
                             expire_on_commit=False)
