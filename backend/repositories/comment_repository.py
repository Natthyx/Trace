from sqlmodel import Session, col, select

from models.base_model import utcnow
from models.comment import Comment


class CommentRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, comment: Comment) -> Comment:
        self.session.add(comment)
        self.session.commit()
        self.session.refresh(comment)

        return comment

    def update(self, comment: Comment) -> Comment:
        comment.updated_at = utcnow()
        self.session.add(comment)
        self.session.commit()
        self.session.refresh(comment)
        
        return comment

    def delete(self, comment: Comment):
        self.session.delete(comment)
        self.session.commit()

    def get_by_id(self, comment_id: int) -> Comment | None:
        return self.session.get(Comment, comment_id)

    def list_for_progress(self, progress_id: int) -> list[Comment]:
        stmt = (
            select(Comment)
            .where(col(Comment.progress_id) == progress_id)
            .order_by(col(Comment.created_at).asc())
            )
        return list(self.session.exec(stmt).all())