from app.routers.auth import User
from app.routers.auth import router as register_router
from app.routers.sprint import Sprint
from app.routers.sprint import router as sprint_router
from app.routers.workplace import UserAssignedWorkplace

list_of_routes = [
    register_router,
    sprint_router,
]
__beanie_models__ = [User, Sprint, UserAssignedWorkplace]


__all__ = [
    "list_of_routes",
    "__beanie_models__",
]
