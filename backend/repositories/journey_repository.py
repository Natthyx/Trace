from sqlmodel import Session, select
from models.base_model import utcnow
from models.journey import Journey, Visibility

class JourneyRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, journey: Journey) -> Journey:
        self.session.add(journey)
        self.session.commit()
        self.session.refresh(journey)

        return journey

    def get_by_id(self, journey_id:int) -> Journey | None:
        return self.session.get(Journey, journey_id)

    def get_visible_to(self, viewer_id: int | None = None) -> list[Journey]:
        stmt = select(Journey).where(
            (Journey.visibility == Visibility.public) | (Journey.user_id == viewer_id)
        )

        return list(self.session.exec(stmt).all())
    
    def update(self, journey:Journey) -> Journey:
        journey.updated_at = utcnow()
        self.session.commit()
        self.session.refresh(journey)
        return journey

    def delete(self, journey: Journey):
        self.session.delete(journey)
        self.session.commit()