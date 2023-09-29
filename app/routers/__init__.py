from app.routers.auth import User, UserAssignedWorkplace
from app.routers.auth import router as register_router
from app.routers.issue import Issue
from app.routers.issue import router as issue_router
from app.routers.sprint import Sprint
from app.routers.sprint import router as sprint_router
from app.routers.user_assigned_issue import UserAssignedIssue
from app.routers.user_assigned_issue import router as user_assigned_issue_router

list_of_routes = [register_router, sprint_router, issue_router, user_assigned_issue_router]
__beanie_models__ = [User, Sprint, UserAssignedWorkplace, Issue, UserAssignedIssue]


__all__ = [
    "list_of_routes",
    "__beanie_models__",
]
