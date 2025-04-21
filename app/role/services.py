from sqlmodel import Session, select
from .models import Role, UserRole 
from app.user.models import User

def create_role(role: Role, db: Session):
    try:
        db.add(role)
        db.commit()
        db.refresh(role)
        return role
    except Exception as e:
        db.rollback()
        return None