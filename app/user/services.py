from sqlmodel import Session, select
from .models import User, UserWithRoles

def get_user(username: str, db: Session):
        user = db.exec(select(User).where(User.username == username)).first()
        return user

def create_user(user: User, db: Session):
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except Exception as e:
        db.rollback()
        return None
    