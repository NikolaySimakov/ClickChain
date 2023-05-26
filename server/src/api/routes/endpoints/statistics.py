from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.dependencies.database import get_session
from datetime import date

from schemas import Click
from db.repositories import clicks_crud
from resources.enums import ClickStatistics

router = APIRouter()


@router.get('/{token}/clicks', response_model=list[Click] | float | int)
async def get_clicks(
    token: str,
    period_start: date = None,
    period_end: date = date.today(),
    additional_settings: ClickStatistics = ClickStatistics.NONE,
    db: AsyncSession = Depends(get_session),
):
    clicks = await clicks_crud.read_clicks(db, token, period_start, period_end)
    count = len(clicks)
    
    if additional_settings == ClickStatistics.COUNT:
        return count
    elif additional_settings == ClickStatistics.AVERAGE:
        if period_end and period_start:
            days = (period_end - period_start).days + 1
            return round(count/days, 2)
        return round(count/7, 2) # default calculate clicks per week
    return clicks


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
