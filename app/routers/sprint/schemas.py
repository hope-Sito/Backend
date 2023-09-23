from datetime import datetime
from uuid import UUID

from beanie import Document
from pydantic import BaseModel, Field, model_validator


class SprintCreation(BaseModel):
    name: str
    start_date: datetime
    end_date: datetime

    @model_validator(mode="after")
    def validate_date_order(self) -> "SprintCreation":
        if (self.start_date or datetime.date.min) > (self.end_date or datetime.date.max):
            msg = "Дата окончания спринта должна быть позже даты начала."
            raise ValueError(msg)
        return self


class Sprint(Document):
    name: str
    start_date: datetime
    end_date: datetime
    workplace_id: UUID


class SuccessfulResponse(BaseModel):
    details: str = Field("Выполнено", title="Статус операции")
