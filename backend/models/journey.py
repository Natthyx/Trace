from datetime import datetime
from enum import Enum

from sqlmodel import SQLModel, Field
from models.base_model import BaseModel

class JourneyStatus(str, Enum):
    active = "active"
    paused = "paused"
    completed = "completed"
    abandoned = "abandoned"

class Visibility(str, Enum):
    private = "private"
    public = "public"

class Journey(BaseModel, table=True):
    journey_id: int | None = Field(primary_key=True, default=None)
    title: str = Field(min_length=1)
    description: str | None = Field(default=None, nullable=True)
    start_date: datetime | None = Field(default=None, nullable=True)
    end_date: datetime | None = Field(default=None, nullable=True)
    status: JourneyStatus = Field(default=JourneyStatus.active)
    visibility: Visibility = Field(default=Visibility.private)
    user_id: int = Field(foreign_key="user.user_id")


class JourneyCreate(SQLModel):
    title: str = Field(min_length=1)
    description: str | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None
    status: JourneyStatus = JourneyStatus.active
    visibility: Visibility = Visibility.private

class JourneyUpdate(SQLModel):
    title: str | None = None
    description: str | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None
    status: JourneyStatus | None = None
    visibility: Visibility | None = None