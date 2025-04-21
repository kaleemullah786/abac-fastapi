from typing import Annotated
from fastapi import Depends, HTTPException, status, APIRouter
from app.auth.services import get_current_user
from app.authz.utils import has_permission
from app.user.models import UserWithRoles

router = APIRouter()

@router.get("/{user_id}/{id}", response_model=str)
async def get_todo(
    user_id: int,
    id: int,
    current_user: Annotated[UserWithRoles , Depends(get_current_user)],
):
    # This is a mock example of a todo item. In a real application, you would fetch this from a database.
    if not has_permission(current_user, "todos", "view", {"user_id":user_id}):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not enough permissions",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return f"Todo item {id} details"  # Replace with actual todo item details
