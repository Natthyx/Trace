from repositories.comment_repository import CommentRepository
from services.comment_service import CommentService
from repositories.progress_repository import ProgressRepository
from services.progress_service import ProgressService
from repositories.milestone_repository import MilestoneRepository
from services.user_service import UserService
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session
from db.db import get_db
from models.user import User
from repositories.journey_repository import JourneyRepository
from repositories.user_repository import UserRepository
from services.journey_service import JourneyService
from core.security import decode_access_token
from services.milestone_service import MilestoneService


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_user_service(session: Session = Depends(get_db)) -> UserService:
    return UserService(UserRepository(session=session))

def get_current_user(token: str = Depends(oauth2_scheme), service: UserService = Depends(get_user_service)) -> User:
    unauthorized_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    username = decode_access_token(token)
    if username is None:
        raise unauthorized_exception
    user = service.repository.get_by_username(username)
    if user is None:
        raise unauthorized_exception

    return user

def get_current_user_id(current_user: User = Depends(get_current_user)) -> int:
    assert current_user.user_id is not None, "Persisted user must have a primary key"
    return current_user.user_id

def get_journey_service(session: Session = Depends(get_db)) -> JourneyService:
    return JourneyService(JourneyRepository(session=session))

def get_milestone_service(session: Session = Depends(get_db)) -> MilestoneService:
    return MilestoneService(MilestoneRepository(session=session), journey=JourneyRepository(session=session))

def get_progress_service(session: Session = Depends(get_db)) -> ProgressService:
    return ProgressService(ProgressRepository(session=session) , journey=JourneyRepository(session=session))

def get_comment_service(session: Session = Depends(get_db)) -> CommentService:
    return CommentService(CommentRepository(session=session) , progress = ProgressRepository(session=session), journey=JourneyRepository(session=session))