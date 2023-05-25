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


async def read_clicks(session: AsyncSession, token: str, start_date: date=None, end_date: date=None) -> list[Click]:
    
    query_conditions = Click.link_token == token
    
    try:
        if start_date and end_date:
            assert start_date <= end_date
            query_conditions = query_conditions & (Click.date >= start_date) & (Click.date <= end_date + timedelta(days=1))
        elif start_date:
            assert start_date <= date.today()
            query_conditions = query_conditions & (Click.date >= start_date)
        elif end_date:
            assert end_date <= date.today()
            query_conditions = query_conditions & (Click.date <= end_date + timedelta(days=1))
    except:
        raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=strings.CLICKS_UNPROCESSABLE_ENTITY
            )
    
    try:
        result = await session.execute(select(Click).where(query_conditions))
        clicks = result.scalars().all()
        return clicks

    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=strings.CLICKS_NOT_FOUND
        )