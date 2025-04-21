from datetime import timedelta
from typing import Annotated, Any
from fastapi import Depends, HTTPException, status, APIRouter
from sqlmodel import Session
from fastapi.security import OAuth2PasswordRequestForm
from .models import Token
from .services import authenticate_user, create_access_token, get_current_user, get_password_hash
from app.user.models import User, UserCreate, UserWithRoles
from app.user.services import create_user
from app.db import get_session

ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter()

@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Annotated[Session, Depends(get_session)],
) -> Token:
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.get("/user", response_model= UserWithRoles)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_user)],
):
    user=UserWithRoles(**current_user.model_dump(exclude={"hashed_password"}))
    user.roles = [role.name for role in current_user.roles]
    return user

@router.post("/register")
async def register_user(
    form_data: Annotated[UserCreate, Depends()],
    db: Annotated[Session, Depends(get_session)],
):
    # Hash the password
    hashed_password = get_password_hash(form_data.password)
    # Create the user in the database
    db_user = create_user(User(username=form_data.username, hashed_password=hashed_password), db)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists",
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": db_user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")
