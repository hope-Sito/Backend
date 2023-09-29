from typing import List
from uuid import UUID

from beanie.odm.documents import PydanticObjectId
from beanie.operators import In
from fastapi import APIRouter, Depends, Path, status

from app.auth.oauth2 import guest, member
from app.core.exceptions import IssueNotFoundError, UserNotFoundError, ValidationError
from app.routers.auth import User
from app.routers.auth.schemas import Role, SuccessfulResponse, UserAssignedWorkplace
from app.routers.issue import Issue

from .schemas import UserAssignedIssue

router = APIRouter(tags=["UserAssignedIssue"])


@router.post(
    "/{workplace_id}/issues/{issue_id}/users/{user_id}",
    response_model=SuccessfulResponse,
    status_code=status.HTTP_201_CREATED,
)
async def assign_user(
    workplace_id: UUID = Path(...),
    issue_id: UUID = Path(...),
    user_id: PydanticObjectId = Path(...),
    user: User = Depends(member),
):
    user = await User.find_one(User.id == user_id)
    if user is None:
        raise UserNotFoundError("Такого пользователя не найдено.")
    issue = await Issue.find_one(Issue.id == issue_id)
    if issue is None:
        raise IssueNotFoundError("Такой задачи не найдено.")
    user_assigned_Workplace = await UserAssignedWorkplace.find_one(
        UserAssignedWorkplace.user_id == user_id, UserAssignedWorkplace.workplace_id == workplace_id
    )
    if user_assigned_Workplace is None:
        raise ValidationError("Пользователь не состоит в указанном воркплейсе.")
    if user_assigned_Workplace.role is Role.GUEST:
        raise ValidationError("Гостю нельзя назнасть задачу.")
    user_assigned_issue = await UserAssignedIssue.find_one(
        UserAssignedIssue.issue_id == issue_id, UserAssignedIssue.user_id == user_id
    )
    if user_assigned_issue is not None:
        raise ValidationError("Данный пользователь уже назаначен к этой задаче.")
    user_assigned_issue = UserAssignedIssue(issue_id=issue_id, user_id=user_id)
    await user_assigned_issue.create()
    return SuccessfulResponse()


# TODO поменять User на класс без поля password
@router.get("/{workplace_id}/issues/{issue_id}/users", response_model=List[User], status_code=status.HTTP_200_OK)
async def get_users(issue_id: UUID = Path(...), user: User = Depends(guest)):
    issue = await UserAssignedIssue.find(UserAssignedIssue.issue_id == issue_id).to_list()
    ids = [o.user_id for o in issue]
    users = await User.find(In(User.id, ids)).to_list()
    return users


@router.delete(
    "/{workplace_id}/issues/{issue_id}/users/{user_id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT
)
async def unassign_user(
    issue_id: UUID = Path(...), user_id: PydanticObjectId = Path(...), user: User = Depends(member)
):
    user_assigned_issue = await UserAssignedIssue.find(
        UserAssignedIssue.issue_id == issue_id, UserAssignedIssue.user_id == user_id
    ).first_or_none()
    if user_assigned_issue is None:
        raise ValidationError("Данный пользователь не назаначен к этой задаче.")
    await user_assigned_issue.delete()
    return None
