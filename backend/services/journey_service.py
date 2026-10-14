from core.errors import ForbiddenError, NotFoundError
from models.journey import Journey, JourneyCreate, JourneyUpdate, Visibility
from repositories.journey_repository import JourneyRepository


class JourneyNotFoundError(NotFoundError):
    def __init__(self, journey_id: int):
        super().__init__(f"Journey {journey_id} not found")
        self.journey_id = journey_id


class JourneyForbiddenError(ForbiddenError):
    def __init__(self, journey_id: int):
        super().__init__(f"Not allowed to access journey {journey_id}")
        self.journey_id = journey_id


class JourneyService:
    def __init__(self, repository: JourneyRepository):
        self.repository = repository

    def create_journey(self, data: JourneyCreate, user_id: int) -> Journey:
        journey = Journey(
            title=data.title,
            description=data.description,
            start_date=data.start_date,
            end_date=data.end_date,
            status=data.status,
            user_id=user_id,
            visibility=data.visibility
        )
        return self.repository.create(journey)

    def list_journey(self, viewer_id : int | None = None) -> list[Journey]:
        return self.repository.get_visible_to(viewer_id=viewer_id)

    def get_journey_by_id(self, journey_id: int, viewer_id: int | None = None) -> Journey:
        journey = self.repository.get_by_id(journey_id=journey_id)
        if journey is None:
            raise JourneyNotFoundError(journey_id=journey_id)
        if journey.visibility == Visibility.private and journey.user_id != viewer_id:
            raise JourneyForbiddenError(journey_id=journey_id)
        return journey

    def update_journey(self, journey_id: int, data_in: JourneyUpdate, user_id: int) -> Journey:
        journey = self.repository.get_by_id(journey_id=journey_id)
        if journey is None:
            raise JourneyNotFoundError(journey_id=journey_id)
        if journey.user_id != user_id:
            raise JourneyForbiddenError(journey_id=journey_id)
        
        updates = data_in.model_dump(exclude_unset=True)
        journey.sqlmodel_update(updates)

        return self.repository.update(journey)

    def delete_journey(self, journey_id: int, user_id: int):
        journey = self.repository.get_by_id(journey_id=journey_id)
        if journey is None:
            raise JourneyNotFoundError(journey_id=journey_id)
        if journey.user_id != user_id:
            raise JourneyForbiddenError(journey_id=journey_id)

        self.repository.delete(journey)