from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
from datetime import date, timedelta

import schemas
from db.models import Click
from resources import strings


async def create_click(session: AsyncSession, click: schemas.Click):

    new_click = Click(link_token=click.link_token,
                      user_ip=click.user_ip, date=click.date)

    session.add(new_click)

    try:
        await session.commit()
        await session.refresh(new_click)
        return new_click

    except IntegrityError:
        await session.rollback()
        raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED, detail=strings.CLICK_WAS_NOT_CREATED
        )


async def read_clicks(session: AsyncSession, token: str):
    try:
        result = await session.execute(select(Click).where(Click.link_token == token))
        clicks = result.scalars().all()
        return clicks

    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=strings.CLICKS_NOT_FOUND
        )


# when start date is not None
async def read_clicks_period_start_only(session: AsyncSession, token: str, start_date: date) -> list[Click]:
    try:
        assert start_date <= date.today()
        result = await session.execute(select(Click).where((Click.date >= start_date) & (Click.link_token == token)))
        clicks = result.scalars().all()
        return clicks
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=strings.CLICKS_NOT_FOUND_BY_PERIOD
        )


# when end date is not None
async def read_clicks_period_end_only(session: AsyncSession, token: str, end_date: date) -> list[Click]:
    try:
        assert end_date <= date.today()
        result = await session.execute(select(Click).where((Click.date <= end_date + timedelta(days=1)) & (Click.link_token == token)))
        clicks = result.scalars().all()
        return clicks
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=strings.CLICKS_NOT_FOUND_BY_PERIOD
        )


# when start and end date are not None
async def read_clicks_period(session: AsyncSession, token: str, start_date: date, end_date: date) -> list[Click]:
    try:
        assert start_date <= end_date
        result = await session.execute(select(Click).where((Click.date >= start_date) & (Click.date <= end_date + timedelta(days=1)) & (Click.link_token == token)))
        clicks = result.scalars().all()
        return clicks
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=strings.CLICKS_NOT_FOUND_BY_PERIOD
        )