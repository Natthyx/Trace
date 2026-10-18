from datetime import datetime, timezone

from sqlmodel import Field, SQLModel


class Follow(SQLModel, table=True):
    user_id: int = Field(foreign_key="user.user_id", primary_key=True)
    journey_id: int = Field(foreign_key="journey.journey_id", primary_key=True)
    followed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))



    

