from uuid import UUID

from pydantic import BaseModel


class CostEntryOut(BaseModel):
    id: UUID
    application_id: UUID
    amount: float

    class Config:
        orm_mode = True
