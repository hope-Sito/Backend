from uuid import UUID

from app.auth.oauth2 import get_current_user
from app.routers.auth import User
from fastapi import APIRouter, Body, Depends, Path, status

from .schemas import Sprint, SprintCreation, SuccessfulResponse

router = APIRouter(tags=["Sprint"])


@router.post("/{workplace_id}/createsprint", response_model=SuccessfulResponse, status_code=status.HTTP_200_OK)
async def create(
    sprint_creation: SprintCreation = Body(...), workplace_id: UUID = Path(...), user: User = Depends(get_current_user)
):
    # TODO Проверить что существует workplace c id

    sprint = Sprint(**sprint_creation.dict(), workplace_id=workplace_id)
    await sprint.create()
    return SuccessfulResponse()
