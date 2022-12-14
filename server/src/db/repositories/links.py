from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from schemas import LinkBase, LongLink, ClicksBase
from db.models import Link, Clicks
from resources import strings


async def create_link(session: AsyncSession, link: LinkBase):

    new_link = Link(token=link.token, long_link=link.long_link)
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


async def get_link(session: AsyncSession, token: str):

    try:
        q = (await session.execute(select(Link).where(Link.token == token))).scalars().one()
        return q

    except NoResultFound:
        return None


async def get_token(session: AsyncSession, long_link: LongLink) -> str | None:

    try:
        q = (await session.execute(select(Link).where(Link.long_link == long_link.link))).scalars().one()
        return q.token

    except NoResultFound:
        return None

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
