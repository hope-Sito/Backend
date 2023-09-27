<<<<<<< HEAD
=======
from typing import List
>>>>>>> origin/dev
from uuid import UUID

from app.auth.jwt_token import decode_token
from app.core.exceptions import ForbiddenException, Unauthorized
<<<<<<< HEAD
from app.routers.auth.schemas import User
from app.routers.userassignedworkplace.schemas import Role, UserAssignedWorkplace
=======
from app.routers.auth.schemas import Role, User, UserAssignedWorkplace
>>>>>>> origin/dev
from fastapi import Depends, Path
from fastapi.security import HTTPBearer


oauth2_scheme = HTTPBearer()


async def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    token = decode_token(token.credentials)
    user = await User.by_email(token.email)
    if not user:
        raise Unauthorized()
    return user


class RoleChecker:
<<<<<<< HEAD
    def __init__(self, role: Role):
=======
    def __init__(self, role: List[Role]):
>>>>>>> origin/dev
        self.role = role

    async def __call__(self, user: User = Depends(get_current_user), workplace_id: UUID = Path(...)) -> str:
        workplace = (
            await UserAssignedWorkplace.find(UserAssignedWorkplace.user_id == user.id)
            .find(UserAssignedWorkplace.workplace_id == workplace_id)
            .first_or_none()
        )
        if workplace is not None and workplace.role in self.role:
            return user
<<<<<<< HEAD
        raise ForbiddenException()
=======
        raise ForbiddenException("Нет прав.")


# доступно только админу
admin: RoleChecker = RoleChecker([Role.ADMIN])
# доступно админам и членам
member: RoleChecker = RoleChecker([Role.MEMBER, Role.GUEST])
# доступно админам, членам и гостям
guest: RoleChecker = RoleChecker([Role.GUEST, Role.MEMBER, Role.MEMBER])
>>>>>>> origin/dev
