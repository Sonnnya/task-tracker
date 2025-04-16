
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STask(STaskAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class STaskId(BaseModel):
    ok: bool = True
    id: int

    model_config = ConfigDict(from_attributes=True)


class SBookAdd(BaseModel):
    title: str
    author: str


class SBookId(SBookAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class SPagination(BaseModel):
    limit: int = Field(le=0, ge=100),
    offset: int = Field(le=0, ge=100),
