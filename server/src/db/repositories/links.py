from fastapi import HTTPException, status
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from ... import schemas
from ..models import Link, Click
from ...resources import strings
from datetime import timedelta


async def create_token(session: AsyncSession, link: schemas.Link):

    new_link = Link(
        token=link.token, 
        long_link=str(link.long_link),
        activation_date=link.activation_date, 
        deactivation_date=link.deactivation_date
    )
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


async def get_links(session: AsyncSession, token: str=None):

    try:
        if token:
            data = await session.execute(select(Link).where(Link.token == token))
            link = data.scalars().one()
            return link
        else:
            data = await session.execute(select(Link).order_by(Link.activation_date.desc()))
            links = data.scalars().all()
            return links

    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=strings.LINK_DOES_NOT_EXIST)


async def get_token(session: AsyncSession, link: str) -> str | None:

    try:
        q = (await session.execute(select(Link).where(Link.long_link == link))).scalars().one()
        return q.token

    except NoResultFound:
        return None
    

async def update_link_deactivation_date(session: AsyncSession, token: str, duration: int):
    try:
        data = await session.execute(select(Link).where(Link.token == token))
        link = data.scalars().one()
        link.deactivation_date = link.activation_date + timedelta(days=duration)
        await session.commit()
        await session.refresh(link)
        return {"message": "Link deactivation date was successfully updated."}
    
    except NoResultFound:
        return None


async def delete_link(session: AsyncSession, token: str):

    try:
        result = await session.execute(select(Link).where(Link.token == token))
        link = result.scalar_one()
        await session.execute(delete(Click).where(Click.link_token == token))
        await session.delete(link)
        await session.commit()
        return {"message": "Link deleted successfully"}
    
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=strings.LINK_DOES_NOT_EXIST)


async def delete_links(session: AsyncSession):
    links = delete(Link)
    clicks = delete(Click)
    await session.execute(clicks)
    await session.execute(links)
    await session.commit()

    return {"message": "All links have been deleted."}
