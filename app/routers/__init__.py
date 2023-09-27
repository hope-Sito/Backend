from app.routers.auth import User, UserAssignedWorkplace
from app.routers.auth import router as register_router
from app.routers.sprint import Sprint
from app.routers.sprint import router as sprint_router
<<<<<<< HEAD
from app.routers.userassignedworkplace import UserAssignedWorkplace
from app.routers.workplace import Workplace
from app.routers.workplace import router as workplace_router
=======
>>>>>>> origin/dev

list_of_routes = [
    register_router,
    sprint_router,
<<<<<<< HEAD
    workplace_router,
]
__beanie_models__ = [User, Workplace, Sprint, UserAssignedWorkplace]
=======
]
__beanie_models__ = [User, Sprint, UserAssignedWorkplace]
>>>>>>> origin/dev


__all__ = [
    "list_of_routes",
    "__beanie_models__",
]
