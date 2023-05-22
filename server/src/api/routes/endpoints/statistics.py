from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.dependencies.database import get_session
from datetime import date

router = APIRouter()


@router.get('/', response_model=int)
async def get_long_link(
    token: str | None = None,
    db: AsyncSession = Depends(get_session),
):
    return 'ekj jenf;n j'


@router.get('/date/{selected_date}')
async def get_statistics_by_date(
    selected_date: date,
    token: str | None = None,
    db: AsyncSession = Depends(get_session),
):
    return None


@router.get('/locations')
async def get_locations(
    token: str | None = None,
    db: AsyncSession = Depends(get_session),
):

    '''
    This route returns all the locations of users who clicked on the link with the given token.
    (token, db) -> List[Location]
    '''

    return None
