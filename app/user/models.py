from sqlmodel import Field, Relationship
from typing import List
from app.models import Base, UserRole

class UserBase(Base):
    username: str = Field(index=True, unique=True, nullable=False)
    hashed_password: str = Field(nullable=False)

class User(UserBase, table=True):
    id: int = Field(default=None, primary_key=True)
    roles: List["Role"] =  Relationship(back_populates="users", link_model=UserRole)

class UserCreate(Base):
    username: str = Field(min_length=3, max_length=50, nullable=False)
    password: str = Field(min_length=5, max_length=50, nullable=False)

class UserWithRoles(Base):
    id: int
    username: str
    roles: List["str"] = []