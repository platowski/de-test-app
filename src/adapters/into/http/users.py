from typing import Annotated

from fastapi import APIRouter, Depends

from adapters.out.workos import WorkOsAdapter


router = APIRouter(prefix="/users")


@router.get("")
async def get(workos_adapter: Annotated[WorkOsAdapter, Depends(WorkOsAdapter)]):
    return workos_adapter.get_users()
