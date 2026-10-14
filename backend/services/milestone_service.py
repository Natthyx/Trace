from models.journey import Visibility
from services.journey_service import JourneyForbiddenError, JourneyNotFoundError
from repositories.journey_repository import JourneyRepository
from models.milestone import Milestone, MilestoneCreate, MilestoneUpdate
from repositories.milestone_repository import MilestoneNotFoundError, MilestoneRepository


class MilestoneService:
    def __init__(self, repository: MilestoneRepository, journey: JourneyRepository):
        self.repository = repository
        self.journey = journey

    def create_milestone(self, data: MilestoneCreate, journey_id: int, user_id: int) -> Milestone:
        journey = self.journey.get_by_id(journey_id)
        if journey is None:
            raise JourneyNotFoundError(journey_id=journey_id)
        if journey.user_id != user_id:
            raise JourneyForbiddenError(journey_id=journey_id)

        next_position = self.repository.next_position(journey_id=journey_id)
        milestone = Milestone(
            title=data.title,
            description=data.description,
            due_date=data.due_date,
            journey_id=journey_id,
            position=next_position
        )

        return self.repository.create(milestone)

    def update_milestone(self, data: MilestoneUpdate, milestone_id: int, user_id: int) -> Milestone:
        milestone = self.repository.get_by_id(milestone_id)
        if milestone is None:
            raise MilestoneNotFoundError(milestone_id=milestone_id)
        journey = self.journey.get_by_id(milestone.journey_id)
        if journey is None or journey.user_id != user_id:
            raise JourneyForbiddenError(journey_id=milestone.journey_id)

        updates = data.model_dump(exclude_unset=True)
        milestone.sqlmodel_update(updates)
        return self.repository.update(milestone)

    def get_milestone_by_id(self, milestone_id: int, viewer_id: int) -> Milestone:
        milestone = self.repository.get_by_id(milestone_id)
        if milestone is None:
            raise MilestoneNotFoundError(milestone_id=milestone_id)
        journey = self.journey.get_by_id(milestone.journey_id)
        if journey is None or (journey.visibility == Visibility.private and journey.user_id != viewer_id):
            raise JourneyForbiddenError(journey_id=milestone.journey_id)
        return milestone
    
    def delete_milestone(self, milestone_id: int, user_id: int):
        milestone = self.repository.get_by_id(milestone_id)
        if milestone is None:
            raise MilestoneNotFoundError(milestone_id=milestone_id)
        journey = self.journey.get_by_id(milestone.journey_id)
        if journey is None or journey.user_id != user_id:
            raise JourneyForbiddenError(journey_id=milestone.journey_id)

        return self.repository.delete(milestone)

    def reorder_milestones(self, journey_id: int, milestone_ids: list[int], user_id: int) -> list[Milestone]:
        journey = self.journey.get_by_id(journey_id)
        if journey is None:
            raise JourneyNotFoundError(journey_id=journey_id)
        if journey.user_id != user_id:
            raise JourneyForbiddenError(journey_id=journey_id)

        self.repository.reorder(journey_id=journey_id, ordered_ids=milestone_ids)
        return self.repository.list_for_journey(journey_id=journey_id)

    def list_milestones_for_journey(self, journey_id: int, viewer_id: int) -> list[Milestone]:
        journey = self.journey.get_by_id(journey_id)
        if journey is None:
            raise JourneyNotFoundError(journey_id=journey_id)
        if journey.visibility == Visibility.private and journey.user_id != viewer_id:
            raise JourneyForbiddenError(journey_id=journey_id)

        return self.repository.list_for_journey(journey_id=journey_id)