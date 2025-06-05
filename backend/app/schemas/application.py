from uuid import UUID

from pydantic import BaseModel

from ..models.application import AppLifecycle


class ApplicationBase(BaseModel):
    name: str
    lifecycle: AppLifecycle | None = AppLifecycle.NEW


class ApplicationCreate(ApplicationBase):
    pass


class ApplicationOut(ApplicationBase):
    id: UUID

    class Config:
        orm_mode = True
