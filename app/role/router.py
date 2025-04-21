from typing import Annotated
from fastapi import Depends, HTTPException, status, APIRouter
from sqlmodel import Session
from app.user.models import User
from app.auth.services import get_current_user
from .models import RoleCreate, Role
from .services import create_role
from app.db import get_session

router = APIRouter()

@router.post("/", response_model=Role)
async def create_new_role(
    payload: Annotated[RoleCreate, Depends()],
    db: Annotated[Session, Depends(get_session)],
    current_user: Annotated[User, Depends(get_current_user)],
):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    db_role = create_role(Role(name=payload.name), db)
    if not db_role:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Role already exists",
        )
    return db_role
