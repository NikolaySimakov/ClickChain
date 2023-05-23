from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import delete

import schemas
from db.models import Link, Clicks
from resources import strings


async def create_link(session: AsyncSession, link: schemas.Link):

    new_link = Link(token=link.token, long_link=link.long_link,
                    activation_date=link.activation_date, deactivation_date=link.deactivation_date)
    link_clicks = Clicks(link_token=link.token, clicks_count=0)

    session.add(new_link)
    session.add(link_clicks)

    try:
        await session.commit()
        await session.refresh(new_link)
        await session.refresh(link_clicks)
        return new_link

    except IntegrityError:
        await session.rollback()
        raise HTTPException(
            status_code=501, detail=strings.LINK_WAS_NOT_CREATED
        )


async def get_links(session: AsyncSession):

    try:
        res = (await session.execute(select(Link))).scalars()
        my_objects = res.fetchall()
        return my_objects

    except NoResultFound:
        return None


async def get_link(session: AsyncSession, token: str):

    try:
        q = (await session.execute(select(Link).where(Link.token == token))).scalars().one()
        return q

    except NoResultFound:
        return None


async def get_token(session: AsyncSession, long_link: schemas.LongLink) -> str | None:

    try:
        q = (await session.execute(select(Link).where(Link.long_link == long_link.link))).scalars().one()
        return q.token

    except NoResultFound:
        return None


async def delete_link(session: AsyncSession, token: str):

    result = await session.execute(select(Link).where(Link.token == token))
    link = result.scalar_one()
    await session.delete(link)
    await session.commit()

    # also delete all clicks related to this token


async def delete_links(session: AsyncSession):
    links = delete(Link)
    clicks = delete(Clicks)
    await session.execute(clicks)
    await session.execute(links)
    await session.commit()
    return {"message": "All links have been deleted."}


"""
async def get_clicks(session: AsyncSession, token: str) -> ClicksBase:
    q = await get_link(session, token)
    return q.clicks


async def update_clicks(session: AsyncSession, token: str):
    clicks = await session.query(Clicks).filter(Clicks.link_token == token)
    clicks.update({
        'clicks_count': clicks.first().clicks_count + 1
    })

    try:
        await session.commit()
        return clicks
    except:
        return None
"""
