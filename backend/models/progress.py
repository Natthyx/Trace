from enum import Enum
from sqlmodel import Field, SQLModel
from models.base_model import BaseModel

class ProgressType(str, Enum):
    progress = "progress"
    setback = "setback"
    lesson = "lesson"
    

class Progress(BaseModel, table=True):
    progress_id: int | None = Field(primary_key=True, default=None)
    content: str = Field(min_length=1)
    journey_id : int = Field(foreign_key="journey.journey_id")
    user_id: int = Field(foreign_key="user.user_id")
    update_type : ProgressType = Field(default=ProgressType.progress)

class ProgressCreate(SQLModel):
    content: str= Field(min_length=1)
    update_type: ProgressType

class ProgressUpdate(SQLModel):
    content: str | None = None
    update_type: ProgressType | None = None

