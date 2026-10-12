from fastapi import APIRouter, Depends
from models.user import User
from services.journey_service import JourneyService
from models.journey import Journey, JourneyCreate, JourneyUpdate
from api.dependencies import get_current_user, get_current_user_id, get_journey_service

router = APIRouter(
    prefix="/journey",
    tags=["journey"]
)

@router.get("/list", response_model=list[Journey])
def list_journey(
    current_user: User = Depends(get_current_user),
    service: JourneyService = Depends(get_journey_service),
):
    return service.list_journey(viewer_id=current_user.user_id)

@router.get("/{journey_id}", response_model=Journey)
def get_journey_by_id(
    journey_id: int,
    current_user: User = Depends(get_current_user),
    service: JourneyService = Depends(get_journey_service),
):
    return service.get_journey_by_id(journey_id=journey_id, viewer_id=current_user.user_id)

@router.post("/", response_model=Journey, status_code=201)
def create_journey(
    payload: JourneyCreate,
    user_id: int = Depends(get_current_user_id),
    service: JourneyService = Depends(get_journey_service),
):
    return service.create_journey(data=payload, user_id=user_id)

@router.patch("/{journey_id}", response_model=Journey)
def update_journey(
    payload: JourneyUpdate,
    journey_id: int,
    user_id: int = Depends(get_current_user_id),
    service: JourneyService = Depends(get_journey_service),
):
    return service.update_journey(journey_id=journey_id, data_in=payload, user_id=user_id)

@router.delete("/{journey_id}", status_code=204)
def delete_journey(
    journey_id: int,
    user_id: int = Depends(get_current_user_id),
    service: JourneyService = Depends(get_journey_service),
):
    service.delete_journey(journey_id=journey_id, user_id=user_id)