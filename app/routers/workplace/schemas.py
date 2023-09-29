from typing import List, Optional
from uuid import UUID, uuid4

from beanie import Document
from pydantic import BaseModel, Field


class WorkplaceCreation(BaseModel):
    name: str
    description: Optional[str] = None


class Workplace(Document, WorkplaceCreation):
    id: UUID = Field(default_factory=uuid4)
    list_of_states: List[str] = Field(default=["Backlog", "To do", "In Progress", "In Review", "QA", "Done"])


class SuccessfulResponse(BaseModel):
    details: str = Field("Выполнено", title="Статус операции")
