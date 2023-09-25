from uuid import UUID

from app.auth.oauth2 import get_current_user
from app.auth.roles import admin, guest
from app.core.exceptions import WorkplaceNotFoundError
from app.routers.auth.schemas import User
from app.routers.userassignedworkplace.schemas import Role, UserAssignedWorkplace
from fastapi import APIRouter, Body, Depends, Path, status

from .schemas import SuccessfulResponse, Workplace, WorkplaceCreation

router = APIRouter(tags=["Workplace"])


@router.post("/createworkplace", response_model=SuccessfulResponse, status_code=status.HTTP_200_OK)
async def create(workplace_creation: WorkplaceCreation = Body(...), user: User = Depends(get_current_user)):
    workplace = Workplace(**workplace_creation.model_dump())
    await workplace.create()
    userAssignedWorkplace = UserAssignedWorkplace(user_id=user.id, workplace_id=workplace.id, role=Role.ADMIN)
    await userAssignedWorkplace.create()
    return SuccessfulResponse()


@router.get("/workplaces/{workplace_id}", response_model=Workplace, status_code=status.HTTP_200_OK)
async def get(workplace_id: UUID = Path(...), user: User = Depends(guest)):
    workplace = await Workplace.find(Workplace.id == workplace_id).first_or_none()
    if workplace is None:
        raise WorkplaceNotFoundError("Такого воркплейса не найдено.")
    return workplace


@router.put("/workplaces/{workplace_id}", response_model=SuccessfulResponse, status_code=status.HTTP_200_OK)
async def edit(
    workplace_creation: WorkplaceCreation = Body(...), workplace_id: UUID = Path(...), user: User = Depends(admin)
):
    workplace = await Workplace.find(Workplace.id == workplace_id).first_or_none()
    if workplace is None:
        raise WorkplaceNotFoundError("Такого воркплейса не найдено.")
    await workplace.update({"$set": workplace_creation.model_dump()})
    return SuccessfulResponse()


@router.delete("/workplaces/{workplace_id}", response_model=SuccessfulResponse, status_code=status.HTTP_200_OK)
async def delete(workplace_id: UUID = Path(...), user: User = Depends(admin)):
    workplace = await Workplace.find(Workplace.id == workplace_id).first_or_none()
    if workplace is None:
        raise WorkplaceNotFoundError("Такого воркплейса не найдено.")
    userAssignedWorkplaces = await UserAssignedWorkplace.find(
        UserAssignedWorkplace.workplace_id == workplace.id
    ).to_list()
    for userAssignedWorkplace in userAssignedWorkplaces:
        await userAssignedWorkplace.delete()
    await workplace.delete()
    return SuccessfulResponse()
