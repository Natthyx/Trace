from sqlmodel import Session, select, func, col
from core.errors import BadRequestError, NotFoundError
from models.base_model import utcnow
from models.milestone import Milestone

class InvalidMilestoneOrderError(BadRequestError):
    def __init__(self, journey_id: int, message: str):
        super().__init__(f"Invalid milestone ordering for journey {journey_id}: {message}")
        self.journey_id = journey_id

class MilestoneNotFoundError(NotFoundError):
    def __init__(self, milestone_id: int):
        super().__init__(f"Milestone {milestone_id}: not found")
        self.milestone_id = milestone_id

class MilestoneRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, milestone: Milestone) -> Milestone:
        self.session.add(milestone)
        self.session.commit()
        self.session.refresh(milestone)
        return milestone

    def get_by_id(self, milestone_id: int) -> Milestone | None:
        return self.session.get(Milestone, milestone_id)

    def update(self, milestone: Milestone) -> Milestone:
        milestone.updated_at = utcnow()
        self.session.add(milestone)
        self.session.commit()
        self.session.refresh(milestone)
        return milestone

    def delete(self, milestone: Milestone):
        self.session.delete(milestone)
        self.session.commit()

    def list_for_journey(self, journey_id: int) -> list[Milestone]:
        stmt = (
            select(Milestone)
            .where(col(Milestone.journey_id) == journey_id)
            .order_by(col(Milestone.position))
        )
        return list(self.session.exec(stmt).all())

    def reorder(self, journey_id: int, ordered_ids: list[int]) -> None:
        expected = set(self.session.exec(
            select(col(Milestone.id))
            .where(col(Milestone.journey_id) == journey_id)
        ).all())

        if set(ordered_ids) != expected or len(ordered_ids) != len(expected):
            raise InvalidMilestoneOrderError(
                journey_id=journey_id,
                message="Ordered list must be a full permutation of the journey's milestones",
            )
        for new_position, milestone_id in enumerate(ordered_ids):
            milestone = self.session.get(Milestone, milestone_id)
            if milestone is None:
                raise MilestoneNotFoundError(milestone_id=milestone_id)
            milestone.position = new_position
            milestone.updated_at = utcnow()
        self.session.commit()

    def next_position(self, journey_id: int) -> int:
        current_max: int | None = self.session.exec(
            select(func.max(col(Milestone.position)))
            .where(col(Milestone.journey_id) == journey_id)
        ).one()
        return (current_max + 1) if current_max is not None else 0 # type: ignore