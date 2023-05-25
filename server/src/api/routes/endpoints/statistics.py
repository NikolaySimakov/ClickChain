from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.dependencies.database import get_session
from datetime import date

from schemas import Click
from db.repositories import clicks_crud

router = APIRouter()


@router.get('/{token}/clicks', response_model=list[Click] | int)
async def get_clicks(
    token: str,
    period_start: date = None,
    period_end: date = date.today(),
    count: bool = False,
    db: AsyncSession = Depends(get_session),
):
    clicks = await clicks_crud.read_clicks(db, token, period_start, period_end)
        
    if count:
        return len(clicks)

    return clicks


@router.get('/{token}/date/{selected_date}')
async def get_statistics_by_date(
    selected_date: date,
    token: str,
    db: AsyncSession = Depends(get_session),
):
    return None


@router.get('/{token}/locations')
async def get_locations(
    token: str,
    db: AsyncSession = Depends(get_session),
):

    '''
    This route returns all the locations of users who clicked on the link with the given token.
    (token, db) -> List[Location]
    '''

    return None
