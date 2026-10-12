from sqlmodel import Session, select
from models.user import User

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
    def get_by_username(self, username: str) -> User | None:
        return self.session.exec(select(User).where(User.username == username)).first()