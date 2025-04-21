from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class SUserAdd(BaseModel):
    name: str
    position: str


class SUserId(SUserAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class SPagination(BaseModel):
    limit: int = Field(le=0, ge=100),
    offset: int = Field(le=0, ge=100),
