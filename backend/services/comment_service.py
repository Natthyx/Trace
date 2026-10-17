from core.errors import ForbiddenError, NotFoundError
from models.journey import Visibility
from services.journey_service import JourneyForbiddenError, JourneyNotFoundError
from models.comment import Comment, CommentCreate, CommentUpdate
from repositories.journey_repository import JourneyRepository
from repositories.progress_repository import ProgressNotFoundError, ProgressRepository
from repositories.comment_repository import CommentRepository

class CommentNotFoundError(NotFoundError):
    def __init__(self, comment_id: int):
        super().__init__(f"Comment {comment_id}: not found")
        self.comment_id = comment_id

class CommentForbiddenError(ForbiddenError):
    def __init__(self, comment_id: int):
        super().__init__(f"Not allowed to access comment {comment_id}")
        self.comment_id = comment_id

class CommentService:
    def __init__(self, repository: CommentRepository, progress: ProgressRepository, journey: JourneyRepository):
        self.repository = repository
        self.progress = progress
        self.journey = journey
    
    def _assert_progress_accessible(self, progress_id: int, viewer_id: int) -> None:
        progress = self.progress.get_by_id(progress_id)
        if progress is None:
            raise ProgressNotFoundError(progress_id=progress_id)
        journey = self.journey.get_by_id(progress.journey_id)
        if journey is None:
            raise JourneyNotFoundError(journey_id=progress.journey_id)
        if journey.visibility == Visibility.private and journey.user_id != viewer_id:
            raise JourneyForbiddenError(journey_id=progress.journey_id)

    def _assert_journey_owned(self, progress_id: int, user_id: int, comment_id: int) -> None:
        progress = self.progress.get_by_id(progress_id)
        if progress is None:
            raise ProgressNotFoundError(progress_id=progress_id)
        journey = self.journey.get_by_id(progress.journey_id)
        if journey is None:
            raise JourneyNotFoundError(journey_id=progress.journey_id)
        if journey.user_id != user_id:
            raise CommentForbiddenError(comment_id=comment_id)
    
    def create_comment(self, data: CommentCreate, user_id: int, progress_id: int) -> Comment:
        self._assert_progress_accessible(progress_id=progress_id, viewer_id=user_id)

        comment = Comment(
            content = data.content,
            user_id = user_id,
            progress_id = progress_id
        )

        return self.repository.create(comment)

    def update_comment(self, comment_id: int, data: CommentUpdate, user_id: int) -> Comment:
        comment = self.repository.get_by_id(comment_id)
        if comment is None:
            raise CommentNotFoundError(comment_id=comment_id)
        if comment.user_id != user_id:
            raise CommentForbiddenError(comment_id=comment_id)

        updates = data.model_dump(exclude_unset=True)
        comment.sqlmodel_update(updates)

        return self.repository.update(comment)

    def delete_comment(self, comment_id: int, user_id: int):
        comment = self.repository.get_by_id(comment_id)
        if comment is None:
            raise CommentNotFoundError(comment_id=comment_id)
        if comment.user_id == user_id:
            return self.repository.delete(comment)

        self._assert_journey_owned(progress_id=comment.progress_id, user_id=user_id, comment_id=comment_id)
        return self.repository.delete(comment)
        

    def get_comment(self, comment_id: int, viewer_id: int) -> Comment:
        comment = self.repository.get_by_id(comment_id)
        if comment is None:
            raise CommentNotFoundError(comment_id=comment_id)

        self._assert_progress_accessible(progress_id=comment.progress_id, viewer_id=viewer_id)

        return comment

    def list_comments_for_progress(self, progress_id: int, viewer_id: int) -> list[Comment]:
        self._assert_progress_accessible(progress_id=progress_id, viewer_id=viewer_id)
        return self.repository.list_for_progress(progress_id)