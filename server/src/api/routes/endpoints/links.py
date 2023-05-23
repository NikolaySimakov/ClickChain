from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import ValidationError
from datetime import datetime, timedelta
from hashids import Hashids

from api.dependencies.database import get_session
from db.repositories import links as links_crud
from schemas import Link, LongLink
from resources import strings, constants

router = APIRouter()


@router.get('/', response_model=str, name="Original URL", description="Returns original link by token.")
async def get_link(
    token: str | None = None,
    db: AsyncSession = Depends(get_session),
):
    link = await links_crud.get_link(db, token)

    if not link:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=strings.LINK_DOES_NOT_EXIST
        )

    else:
        return link.long_link


@router.get('/all', name="All Links", description="In future I'm going to separate this method for admins and other users. Users will see history of shortened links.")
async def get_all_links(
    limit: int | None = None,
    db: AsyncSession = Depends(get_session),
):
    res = await links_crud.get_links(db)
    return res[:limit] if limit else res


@router.post('/', status_code=status.HTTP_201_CREATED, name="Short Link", description="Creates token for short link and returns it.")
async def post_short_link(
    long_link: LongLink,
    days: int = 1,
    db: AsyncSession = Depends(get_session),
):

    # TODO: add start datetime and end datetime

    created_token = await links_crud.get_token(db, long_link)

    if bool(created_token):
        return created_token

    else:
        hashids = Hashids(salt=long_link.link,
                          min_length=constants.LINK_TOKEN_MIN_LENGTH)
        token = hashids.encode(constants.LINK_TOKEN_ENCODE_DATA)

        # TODO: - Token validation (I'll make recursive method for it)

        try:
            link_data = Link(
                token=token,
                long_link=long_link.link,
                activation_date=datetime.now(),
                deactivation_date=datetime.now() + timedelta(days=days),
            )
            
            print(link_data)

            return await links_crud.create_link(db, link_data)

        except ValidationError as e:
            print(e)


@router.delete('/', status_code=204)
async def delete_link(
    token: str | None = None,
    db: AsyncSession = Depends(get_session),
):
    await links_crud.delete_link(db, token)
    return None


@router.delete('/all', status_code=204, description="Deletes all links. Dangerous!")
async def delete_links(
    db: AsyncSession = Depends(get_session),
):
    return await links_crud.delete_links(db)

"""
@router.get('/{token}')
async def get_short_link_info(
    token: str,
    q: str | None = None,
    db: AsyncSession = Depends(get_session),
):
    if not q:
        return 'all info'
    else:
        if q == 'clicks':
            clicks = await links_crud.get_clicks(db, token)

            if not clicks:
                raise HTTPException(
                    status_code=404, detail=strings.CLICKS_ERROR
                )
            else:
                return clicks.clicks_count
        else:
            return None


@router.put('/{token}/clicks')
async def update_clicks(
    token: str,
    db: AsyncSession = Depends(get_session),
):
    await links_crud.update_clicks(db, token)

"""
