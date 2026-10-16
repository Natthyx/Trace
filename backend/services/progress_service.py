from models.journey import Visibility
from services.journey_service import JourneyForbiddenError, JourneyNotFoundError
from models.progress import Progress, ProgressCreate, ProgressType, ProgressUpdate
from repositories.journey_repository import JourneyRepository
from repositories.progress_repository import ProgressNotFoundError, ProgressRepository



class ProgressService:
    def __init__(self, repository: ProgressRepository, journey: JourneyRepository):
        self.repository = repository
        self.journey = journey

    def create_progress(self, journey_id: int, payload: ProgressCreate, user_id: int) -> Progress:
        journey = self.journey.get_by_id(journey_id=journey_id)
        if journey is None:
            raise JourneyNotFoundError(journey_id)
        if journey.user_id != user_id:
            raise JourneyForbiddenError(journey_id=journey_id)

        progress = Progress(
            journey_id=journey_id,
            user_id=user_id,
            content=payload.content,
            update_type=payload.update_type
        )
        return self.repository.create(progress)

    def update_progress(self, progress_id: int, payload: ProgressUpdate, user_id:int) -> Progress:
        progress = self.repository.get_by_id(progress_id)
        if progress is None:
            raise ProgressNotFoundError(progress_id=progress_id)
        
        journey = self.journey.get_by_id(journey_id=progress.journey_id)
        if journey is None:
            raise JourneyNotFoundError(progress.journey_id)
        if journey.user_id != user_id:
            raise JourneyForbiddenError(journey_id=progress.journey_id)

        updated = payload.model_dump(exclude_unset=True)
        progress.sqlmodel_update(updated)

        return self.repository.update(progress)

    def delete_progress(self, progress_id: int, user_id: int):
        progress = self.repository.get_by_id(progress_id)
        if progress is None:
            raise ProgressNotFoundError(progress_id=progress_id)
        journey = self.journey.get_by_id(progress.journey_id)
        if journey is None or journey.user_id != user_id:
            raise JourneyForbiddenError(journey_id=progress.journey_id)

        return self.repository.delete(progress)
    
    def get_all_for_journey(
        self, journey_id: int, viewer_id: int, update_type: ProgressType | None = None
    ) -> list[Progress]:
        journey = self.journey.get_by_id(journey_id=journey_id)
        if journey is None:
            raise JourneyNotFoundError(journey_id)
        if journey.visibility == Visibility.private and journey.user_id != viewer_id:
            raise JourneyForbiddenError(journey_id=journey_id)

        return self.repository.list_visible(
            viewer_id=viewer_id, journey_id=journey_id, update_type=update_type
        )
        
    def get_progress_by_id(self, progress_id: int, viewer_id: int) -> Progress:
        progress = self.repository.get_by_id(progress_id)
        if progress is None:
            raise ProgressNotFoundError(progress_id=progress_id)
        journey = self.journey.get_by_id(progress.journey_id)
        if journey is None or (journey.visibility == Visibility.private and journey.user_id != viewer_id):
            raise JourneyForbiddenError(journey_id=progress.journey_id)

        return progress

    def list_progress(
        self, viewer_id: int, update_type: ProgressType | None = None
    ) -> list[Progress]:
        return self.repository.list_visible(viewer_id=viewer_id, update_type=update_type)

