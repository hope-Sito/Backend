from typing import Optional
from uuid import UUID, uuid4

from beanie import Document
from pydantic import BaseModel, Field


class WorkplaceCreation(BaseModel):
    name: str
    description: Optional[str] = None


class Workplace(Document, WorkplaceCreation):
    id: UUID = Field(default=uuid4())


class SuccessfulResponse(BaseModel):
    details: str = Field("Выполнено", title="Статус операции")
