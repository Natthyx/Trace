from fastapi import APIRouter, Depends
from services.milestone_service import MilestoneService
from models.milestone import Milestone, MilestoneCreate, MilestoneUpdate
from api.dependencies import get_current_user_id, get_milestone_service

router = APIRouter(
    tags=["Milestones"]
)

@router.post("/journeys/{journey_id}/milestones", response_model=Milestone, status_code=201)
def create_milestone(payload: MilestoneCreate,
                     journey_id: int,
                     user_id: int = Depends(get_current_user_id),
                     service: MilestoneService = Depends(get_milestone_service) 
                     ) -> Milestone:
    return service.create_milestone(data=payload, journey_id=journey_id, user_id=user_id)

@router.get("/journeys/{journey_id}/milestones", response_model=list[Milestone])
def list_milestone_for_journey(journey_id: int, user_id: int = Depends(get_current_user_id), service: MilestoneService = Depends(get_milestone_service)) -> list[Milestone]:
    return service.list_milestones_for_journey(journey_id=journey_id, viewer_id=user_id)

@router.get("/milestones/{milestone_id}", response_model=Milestone)
def get_milestone_by_id(milestone_id: int, user_id: int = Depends(get_current_user_id), service: MilestoneService = Depends(get_milestone_service)) -> Milestone:
    return service.get_milestone_by_id(milestone_id=milestone_id, viewer_id=user_id)

@router.patch("/milestones/{milestone_id}", response_model=Milestone)
def update_milestone(milestone_id: int,
                     payload: MilestoneUpdate,
                     user_id: int = Depends(get_current_user_id),
                     service: MilestoneService = Depends(get_milestone_service)) -> Milestone:
    return service.update_milestone(data=payload, milestone_id=milestone_id, user_id=user_id)

@router.delete("/milestones/{milestone_id}", status_code=204)
def delete_milestone(milestone_id: int,
                     user_id:int = Depends(get_current_user_id),
                     service: MilestoneService = Depends(get_milestone_service)):
    return service.delete_milestone(milestone_id=milestone_id, user_id=user_id)

@router.put("/journeys/{journey_id}/milestones/reorder", response_model=list[Milestone])
def reorder_milestones(journey_id: int,
                       payload: list[int],
                       user_id: int = Depends(get_current_user_id),
                       service: MilestoneService = Depends(get_milestone_service)) -> list[Milestone]:
    return service.reorder_milestones(journey_id=journey_id,milestone_ids=payload, user_id=user_id)