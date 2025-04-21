from sqlmodel import Field, Relationship
from typing import List
from app.models import Base, UserRole

class RoleBase(Base):
    name: str = Field(index=True, unique=True, nullable=False, min_length=3, max_length=50)

class Role(RoleBase, table=True):
    id: int = Field(default=None, primary_key=True)
    users: List["User"] = Relationship(back_populates="roles", link_model=UserRole)

class RoleCreate(RoleBase):
    pass
