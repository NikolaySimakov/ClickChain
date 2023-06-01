from fastapi import HTTPException
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

import schemas
from db.models import Link, Click
from resources import strings


async def create_token(session: AsyncSession, link: schemas.Link):

    new_link = Link(token=link.token, long_link=link.long_link,
                    activation_date=link.activation_date, deactivation_date=link.deactivation_date)

    session.add(new_link)

    try:
        await session.commit()
        await session.refresh(new_link)
        return link.token

    except IntegrityError:
        await session.rollback()
        raise HTTPException(
            status_code=501, detail=strings.LINK_WAS_NOT_CREATED
        )


async def get_links(session: AsyncSession):

    try:
        res = await session.execute(select(Link).order_by(Link.activation_date.desc()))
        links = res.scalars().all()
        return links

    except NoResultFound:
        return None


async def get_link(session: AsyncSession, token: str):

    try:
        q = (await session.execute(select(Link).where(Link.token == token))).scalars().one()
        return q

    except NoResultFound:
        return None


async def get_token(session: AsyncSession, link: str) -> str | None:

    try:
        q = (await session.execute(select(Link).where(Link.long_link == link))).scalars().one()
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
    clicks = delete(Click)
    await session.execute(clicks)
    await session.execute(links)
    await session.commit()

    return {"message": "All links have been deleted."}
