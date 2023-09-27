from datetime import datetime
from uuid import UUID, uuid4

<<<<<<< HEAD
=======
from app.core.exceptions import ValidationError
>>>>>>> origin/dev
from beanie import Document
from pydantic import BaseModel, Field, model_validator


class SprintCreation(BaseModel):
    name: str
    start_date: datetime
    end_date: datetime

    @model_validator(mode="after")
    def validate_date_order(self) -> "SprintCreation":
        if self.start_date > self.end_date:
<<<<<<< HEAD
            raise ValueError("Дата окончания спринта должна быть позже даты начала.")
=======
            raise ValidationError("Дата окончания спринта должна быть позже даты начала.")
>>>>>>> origin/dev
        return self


class Sprint(Document, SprintCreation):
    workplace_id: UUID
<<<<<<< HEAD
    id: UUID = Field(default=uuid4())


class SuccessfulResponse(BaseModel):
    details: str = Field("Выполнено", title="Статус операции")
=======
    id: UUID = Field(default_factory=uuid4)
>>>>>>> origin/dev
