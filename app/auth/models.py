from app.models import Base

class Token(Base):
    access_token: str
    token_type: str

class TokenData(Base):
    username: str | None = None

