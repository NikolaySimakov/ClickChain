from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timedelta
from hashids import Hashids

from api.dependencies.database import get_session
from db.repositories import links_crud, clicks_crud
from schemas import Link, LongLink, Click
from resources import strings, constants

router = APIRouter()


@router.get(
    '/',
    name="All Links",
    description="""
    In future I'm going to separate this method for admins and other users. 
    Users will see history of shortened links.
    """
)
async def get_all_links(
    limit: int | None = None,
    db: AsyncSession = Depends(get_session),
):
    res = await links_crud.get_links(db)
    return res[:limit] if limit else res


@router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    name="Short Link",
    description="Creates token for short link and returns it."
)
async def post_short_link(
    long_link: LongLink,
    days: int = 1,
    db: AsyncSession = Depends(get_session),
):
    if created_token := await links_crud.get_token(db, long_link):
        return created_token
    else:
        hashids = Hashids(salt=long_link.link,
                          min_length=constants.LINK_TOKEN_MIN_LENGTH)
        token = hashids.encode(constants.LINK_TOKEN_ENCODE_DATA)

        link_data = Link(
            token=token,
            long_link=long_link.link,
            activation_date=datetime.now(),
            deactivation_date=datetime.now() + timedelta(days=days),
        )

        return await links_crud.create_link(db, link_data)


@router.delete(
    '/',
    status_code=status.HTTP_204_NO_CONTENT,
    name="Delete all",
    description="Deletes all links. Dangerous!"
)
async def delete_links(
    db: AsyncSession = Depends(get_session),
):
    return await links_crud.delete_links(db)


@router.get('/{token}', response_model=Link | str, status_code=status.HTTP_200_OK)
async def get_link(
    token: str,
    only_link: bool = False,
    db: AsyncSession = Depends(get_session),
):
    if link := await links_crud.get_link(db, token):
        if only_link:
            return link.long_link  # returns orignal link
        return link  # returns all link data
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=strings.LINK_DOES_NOT_EXIST
        )


@router.post('/{token}', name="Click")
async def post_click(
    token: str,
    user_ip: str,
    db: AsyncSession = Depends(get_session),
):

    click_data = Click(
        link_token=token,
        user_ip=user_ip,
        date=datetime.now(),
    )

    return await clicks_crud.create_click(db, click_data)


@router.delete('/{token}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_link(
    token: str,
    db: AsyncSession = Depends(get_session),
):
    await links_crud.delete_link(db, token)
    return None


@router.get('/{token}/clicks', response_model=list[Click], status_code=status.HTTP_200_OK)
async def get_link_clicks(
    token: str,
    db: AsyncSession = Depends(get_session),
):
    if (clicks := await clicks_crud.read_clicks(db, token)) != None:
        return clicks
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=strings.LINK_DOES_NOT_EXIST
        )
