from datetime import datetime
from enum import Enum
from models.base_model import BaseModel
from sqlmodel import Field, SQLModel

class MilestoneStatus(str, Enum):
    pending = "pending"
    completed = "completed"

class Milestone(BaseModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    journey_id: int = Field(foreign_key="journey.journey_id")
    title: str = Field(min_length=1)
    description: str | None = Field(default=None, nullable=True)
    status: MilestoneStatus = Field(default=MilestoneStatus.pending)
    due_date: datetime | None = Field(default=None, nullable=True)
    position: int

class MilestoneCreate(SQLModel):
    title: str = Field(min_length=1)
    description: str | None = None
    due_date: datetime | None = None

class MilestoneUpdate(SQLModel):
    title: str | None = None
    description: str | None = None
    due_date: datetime | None = None
    status: MilestoneStatus | None = None



