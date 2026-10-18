from fastapi import APIRouter, Depends

from api.dependencies import get_follow_service, get_current_user_id
from services.follow_service import FollowService
from models.follow import Follow
from models.journey import Journey
from models.user import User, UserRead


router = APIRouter(tags=["Follow"])


@router.post("/journeys/{journey_id}/follow", response_model=Follow, status_code=201)
def follow_journey(journey_id: int,
                   user_id: int = Depends(get_current_user_id),
                   service: FollowService = Depends(get_follow_service)) -> Follow:
    return service.follow(user_id=user_id, journey_id=journey_id)

@router.delete("/journeys/{journey_id}/follow", status_code=204)
def unfollow_journey(journey_id: int,
                     user_id: int = Depends(get_current_user_id),
                     service: FollowService = Depends(get_follow_service)) -> None:
    service.unfollow(user_id=user_id, journey_id=journey_id)

@router.get("/journeys/{journey_id}/followers", response_model=list[UserRead])
def list_followers(journey_id: int,
                   viewer_id: int = Depends(get_current_user_id),
                   service: FollowService = Depends(get_follow_service)) -> list[User]:
    return service.list_followers(journey_id=journey_id, viewer_id=viewer_id)

@router.get("/users/me/following", response_model=list[Journey])
def list_following(user_id: int = Depends(get_current_user_id),
                   service: FollowService = Depends(get_follow_service)) -> list[Journey]:
    return service.list_following(user_id=user_id)
