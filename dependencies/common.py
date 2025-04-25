from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_session
from schemas.users import SPagination


SessionDep = Annotated[AsyncSession, Depends(get_session)]
PaginationDep = Annotated[SPagination, Depends(SPagination)]
