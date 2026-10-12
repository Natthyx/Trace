from sqlmodel import SQLModel, Field

from models.base_model import BaseModel

class User(BaseModel, table=True):
    user_id : int | None  = Field(primary_key=True, default=None)
    username: str = Field(unique=True)
    email: str = Field(unique=True)
    password_hash: str
class UserCreate(SQLModel):
    username: str
    email: str
    password: str = Field(min_length=8, max_length=72)
class UserRead(BaseModel):
    user_id: int
    username: str
    email: str
class UserUpdate(SQLModel):
    username: str | None = None
    email: str | None = None
    password: str | None = Field(min_length=8,max_length=72)
