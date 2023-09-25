from enum import StrEnum
from uuid import UUID

from beanie import Document
from beanie.odm.documents import PydanticObjectId


class Role(StrEnum):
    ADMIN = "ADMIN"
    MEMBER = "MEMBER"
    GUEST = "GUEST"


class UserAssignedWorkplace(Document):
    user_id: PydanticObjectId
    workplace_id: UUID
    role: Role
