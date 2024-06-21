from typing import Annotated

from fastapi import APIRouter, Depends, Query

from adapters.out.workos import WorkOsAdapter
from ports.into.users import UsersPageDTO, GetUsersPageDTO

router = APIRouter(prefix="/users")


@router.get("", response_model=UsersPageDTO)
async def get(
    workos_adapter: Annotated[WorkOsAdapter, Depends(WorkOsAdapter)],
    email: str | None = None,
    before: str | None = None,
    after: str | None = None,
    limit: Annotated[int | None, Query(ge=1, le=100)] = None,
):
    get_page_dto = GetUsersPageDTO(
        email=email, before=before, after=after, page_size=limit
    )
    return workos_adapter.get_users(get_page_dto)
