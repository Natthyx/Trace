from datetime import datetime, timezone

from sqlmodel import  SQLModel, Field

def utcnow() -> datetime:
    return datetime.now(timezone.utc)

class BaseModel(SQLModel):
    created_at: datetime | None = Field(default_factory=utcnow)
    updated_at: datetime | None = Field(default_factory=utcnow)