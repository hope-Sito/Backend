from uuid import UUID

from beanie import Document
from beanie.odm.documents import PydanticObjectId


class UserAssignedIssue(Document):
    user_id: PydanticObjectId
    issue_id: UUID
