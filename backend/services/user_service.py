from models.user import User, UserCreate
from repositories.user_repository import UserRepository
from core.security import hash_password, verify_password


class UserAlreadyExistsError(Exception):pass
class InvalidCredentialsError(Exception):pass

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository
    def register(self, data: UserCreate) -> User:
        if self.repository.get_by_username(data.username):
            raise UserAlreadyExistsError(data.username)
        user = User(username=data.username, 
                    email=data.email,
                    password_hash=hash_password(data.password))
        return self.repository.create(user=user)
    def authenticate(self, username: str, password: str) -> User:
        user = self.repository.get_by_username(username)
        if not user or not verify_password(password, user.password_hash):
            raise InvalidCredentialsError()

        return user
