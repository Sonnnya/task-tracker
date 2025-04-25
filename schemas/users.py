from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class SUserAdd(BaseModel):
    name: str
    position: str


class SUser(SUserAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class SPagination(BaseModel):
    limit: int = Field(10, ge=0, le=100)
    offset: int = Field(0, ge=0, le=100)
