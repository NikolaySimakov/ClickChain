from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError

import schemas
from db.models import Clicks
from resources import strings


async def create_click(session: AsyncSession, click: schemas.Click):

    new_click = Clicks(link_token=click.link_token,
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
        result = await session.execute(select(Clicks).where(Clicks.link_token == token))
        clicks = result.scalars().all()
        return clicks

    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=strings.CLICKS_NOT_FOUND
        )
