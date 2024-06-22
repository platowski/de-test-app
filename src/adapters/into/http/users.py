from typing import Annotated

from fastapi import APIRouter, Depends, Query, HTTPException

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
    validate_before_after(after, before)

    get_page_dto = GetUsersPageDTO(
        email=email, before=before, after=after, page_size=limit
    )
    return workos_adapter.get_users(get_page_dto)


def validate_before_after(after, before):
    if before and after and before == after:
        raise HTTPException(
            detail=[
                {
                    "msg": "before and after cannot be the same",
                    "loc": ["query", "before", "after"],
                }
            ],
            status_code=422,
        )
