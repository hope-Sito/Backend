from app.routers.auth import User
from app.routers.auth import router as register_router

list_of_routes = [
    register_router,
]
__beanie_models__ = [User]


__all__ = [
    "list_of_routes",
    "__beanie_models__",
]
