from models.user import User
from models.follow import Follow
from core.errors import ConflictError
from models.journey import Journey, Visibility
from services.journey_service import JourneyForbiddenError, JourneyNotFoundError
from repositories.journey_repository import JourneyRepository
from repositories.follow_repository import  FollowRepository


class ExistingFollowFoundError(ConflictError):
    def __init__(self, user_id: int, journey_id: int) -> None:
        super().__init__(f"You already followed journey {journey_id}")
        self.user_id = user_id
        self.journey_id = journey_id

class FollowService:
    def __init__(self, repository: FollowRepository, journey: JourneyRepository) -> None:
        self.repository = repository
        self.journey = journey

    def follow(self, user_id: int, journey_id: int) -> Follow:
        journey = self.journey.get_by_id(journey_id)
        if journey is None:
            raise JourneyNotFoundError(journey_id)
        if journey.visibility == Visibility.private:
            raise JourneyForbiddenError(journey_id)

        existing = self.repository.get_follow(user_id, journey_id)
        if existing is not None:
            raise ExistingFollowFoundError(user_id, journey_id)

        return self.repository.create(user_id, journey_id)

    def unfollow(self, user_id: int, journey_id: int):
        journey = self.journey.get_by_id(journey_id)
        if journey is None:
            raise JourneyNotFoundError(journey_id)
        return self.repository.delete(user_id, journey_id)

    def list_following(self, user_id: int) -> list[Journey]:

        return self.repository.list_following_of_user(user_id)
        
    def list_followers(self, journey_id: int, viewer_id: int) -> list[User]:
        journey = self.journey.get_by_id(journey_id)
        if journey is None:
            raise JourneyNotFoundError(journey_id)
        if journey.visibility == Visibility.private and journey.user_id != viewer_id:
            raise JourneyForbiddenError(journey_id)
        return self.repository.list_followers_of_journey(journey_id)
            