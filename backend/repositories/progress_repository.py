from models.journey import Journey, Visibility
from sqlmodel import Session, col, select

from core.errors import NotFoundError
from models.base_model import utcnow
from models.progress import Progress, ProgressType

class ProgressNotFoundError(NotFoundError):
    def __init__(self, progress_id: int):
        super().__init__(f"Progress {progress_id}: not found")
        self.progress_id = progress_id

class ProgressRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, progress: Progress) -> Progress:
        self.session.add(progress)
        self.session.commit()
        self.session.refresh(progress)

        return progress

    def update(self, progress: Progress) -> Progress:
        progress.updated_at = utcnow()
        self.session.add(progress)
        self.session.commit()
        self.session.refresh(progress)
        return progress

    def delete(self, progress: Progress):
        self.session.delete(progress)
        self.session.commit()

    def get_by_id(self, progress_id: int) -> Progress | None:
        return self.session.get(Progress, progress_id)

    def list_visible(
        self,
        viewer_id: int,
        journey_id: int | None = None,
        update_type: ProgressType | None = None,
    ) -> list[Progress]:
        stmt = (
            select(Progress)
            .join(Journey, col(Progress.journey_id) == col(Journey.journey_id))
            .where(
                (col(Journey.visibility) == Visibility.public)
                | (col(Journey.user_id) == viewer_id)
            )
        )
        if journey_id is not None:
            stmt = stmt.where(col(Progress.journey_id) == journey_id)
        if update_type is not None:
            stmt = stmt.where(col(Progress.update_type) == update_type)
        stmt = stmt.order_by(col(Progress.created_at).desc())
        return list(self.session.exec(stmt).all())

                           
