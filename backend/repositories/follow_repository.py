from typing import cast

from sqlmodel import Session, col, select

from models.user import User
from models.journey import Journey, Visibility
from core.errors import NotFoundError
from models.follow import Follow

class FollowNotFoundError(NotFoundError):
    def __init__(self, user_id: int, journey_id: int) -> None:
        super().__init__(f"You don't follow journey {journey_id}")
        self.user_id = user_id
        self.journey_id = journey_id

class FollowRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_follow(self, user_id: int, journey_id: int) -> Follow | None:
        return self.session.get(Follow, (user_id, journey_id))

    def create(self, user_id: int, journey_id: int) -> Follow:
        follow = Follow(journey_id=journey_id, user_id=user_id)
        self.session.add(follow)
        self.session.commit()
        self.session.refresh(follow)

        return follow

    def delete(self, user_id: int, journey_id: int):
        follow = self.get_follow(user_id, journey_id)
        if follow is None:
            raise FollowNotFoundError(user_id, journey_id)
        self.session.delete(follow)
        self.session.commit()

    def list_followers_of_journey(self, journey_id: int) -> list[User]:
        stmt = select(User).join(Follow, col(Follow.user_id) == col(User.user_id)).where(col(Follow.journey_id) == journey_id).order_by(col(Follow.followed_at).desc())
        return cast("list[User]", self.session.exec(stmt).all())

    def list_following_of_user(self, user_id: int) -> list[Journey]:
        stmt = select(Journey).join(Follow, col(Follow.journey_id) == col(Journey.journey_id)).where(col(Follow.user_id) == user_id).where((col(Journey.visibility) == Visibility.public) | (col(Journey.user_id) == user_id)).order_by(col(Follow.followed_at).desc())
        return cast("list[Journey]" ,self.session.exec(stmt).all())