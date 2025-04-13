from fastapi import APIRouter, Depends
from schemas import SBookAdd
from typing import Annotated
from database import get_session, BookModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


SessionDep = Annotated[AsyncSession, Depends(get_session)]

router = APIRouter(prefix='/books', tags=['Книжки'])


@router.post('/')
async def add_book(book: Annotated[SBookAdd, Depends()], session: SessionDep):
    new_book = BookModel(**(book.model_dump()))
    session.add(new_book)
    await session.commit()


@router.get('/')
async def get_books(session: SessionDep):
    query = select(BookModel)
    result = await session.execute(query)
    return result.scalars().all()
