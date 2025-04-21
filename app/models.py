from sqlmodel import SQLModel, Field

class Base(SQLModel):
    pass

class UserRole(Base, table=True):
    __tablename__ = "user_role"
    user_id:  int = Field(default=None, foreign_key="user.id", primary_key=True)
    role_id:  int = Field(default=None, foreign_key="role.id", primary_key=True)