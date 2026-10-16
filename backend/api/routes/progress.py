from fastapi import APIRouter, Depends
from services.progress_service import ProgressService
from models.progress import Progress, ProgressCreate, ProgressType, ProgressUpdate
from api.dependencies import get_current_user_id, get_progress_service

router = APIRouter(tags=["Progress Updates"])

@router.post("/journeys/{journey_id}/progress" , response_model=Progress, status_code=201)
def create_progress(journey_id: int ,payload: ProgressCreate, user_id: int = Depends(get_current_user_id), service: ProgressService = Depends(get_progress_service))-> Progress:
    return service.create_progress(journey_id=journey_id, payload=payload, user_id=user_id)

@router.get("/journeys/{journey_id}/progress", response_model=list[Progress])
def get_all_progress_for_journey(journey_id: int, update_type: ProgressType | None = None, viewer_id: int = Depends(get_current_user_id), service: ProgressService = Depends(get_progress_service)) -> list[Progress]:
    return service.get_all_for_journey(journey_id=journey_id, viewer_id=viewer_id, update_type=update_type)

@router.get("/progress/{update_id}", response_model=Progress)
def get_progress_by_id(update_id: int, user_id: int = Depends(get_current_user_id), service: ProgressService = Depends(get_progress_service)) -> Progress:
    return service.get_progress_by_id(progress_id=update_id, viewer_id=user_id) 

@router.get("/progress", response_model=list[Progress])
def list_progress(update_type: ProgressType | None = None, viewer_id: int = Depends(get_current_user_id), service: ProgressService = Depends(get_progress_service)) -> list[Progress]:
    return service.list_progress(viewer_id=viewer_id, update_type=update_type)

@router.patch("/progress/{update_id}", response_model=Progress)
def update_progress(update_id: int, payload: ProgressUpdate, user_id: int=Depends(get_current_user_id), service: ProgressService = Depends(get_progress_service)) -> Progress:
    return service.update_progress(progress_id=update_id, payload=payload, user_id=user_id)

@router.delete("/progress/{update_id}", status_code=204)
def delete_progress(update_id: int, user_id: int = Depends(get_current_user_id), service: ProgressService=Depends(get_progress_service)):
    return service.delete_progress(progress_id=update_id, user_id=user_id)
