from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import ValidationError
from hashids import Hashids

from api.dependencies.database import get_session
from db.repositories import links as links_crud
from schemas.links import LinkBase, LongLink
from resources import strings, constants

router = APIRouter()


@router.get('/', response_model=str)
async def get_long_link(
    token: str | None = None,
    db: AsyncSession = Depends(get_session),
):
    link = await links_crud.get_link(db, token)

    if not link:
        raise HTTPException(
            status_code=404, detail=strings.LINK_DOES_NOT_EXIST
        )

    else:
        return link.long_link


@router.post('/')
async def post_short_link(
    long_link: LongLink,
    db: AsyncSession = Depends(get_session),
):
    created_token = await links_crud.get_token(db, long_link)

    if bool(created_token):
        return created_token

    else:
        hashids = Hashids(salt=long_link.link,
                          min_length=constants.LINK_TOKEN_MIN_LENGTH)
        token = hashids.encode(constants.LINK_TOKEN_ENCODE_DATA)

        # TODO: - Token validation (I'll make recursive method for it)

        try:
            link_data = LinkBase(
                token=token,
                long_link=long_link.link,
            )

            return await links_crud.create_link(db, link_data)

        except ValidationError as e:
            print(e)


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
