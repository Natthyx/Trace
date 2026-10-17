from sqlmodel import Field, SQLModel

from models.base_model import BaseModel


class Comment(BaseModel, table=True):
    comment_id : int | None = Field(primary_key=True, default=None)
    content: str = Field(min_length=1)
    user_id: int = Field(foreign_key="user.user_id")
    progress_id: int = Field(foreign_key="progress.progress_id")


class CommentCreate(SQLModel):
    content: str = Field(min_length=1)

class CommentUpdate(SQLModel):
    content: str | None = None


