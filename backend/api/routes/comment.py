from fastapi import APIRouter, Depends

from api.dependencies import get_comment_service, get_current_user_id
from services.comment_service import CommentService
from models.comment import Comment, CommentCreate, CommentUpdate


router = APIRouter(tags=["Comments"])


@router.post("/progress/{progress_id}/comments", response_model=Comment, status_code=201)
def create_comment(progress_id: int,
                   payload: CommentCreate,
                   user_id: int = Depends(get_current_user_id),
                   service: CommentService = Depends(get_comment_service)) -> Comment:
    return service.create_comment(data=payload, user_id=user_id, progress_id=progress_id)

@router.get("/progress/{progress_id}/comments", response_model=list[Comment])
def list_comments_for_progress(progress_id: int,
                                viewer_id: int = Depends(get_current_user_id),
                                service: CommentService = Depends(get_comment_service)) -> list[Comment]:
    return service.list_comments_for_progress(progress_id=progress_id, viewer_id=viewer_id)

@router.get("/comments/{comment_id}", response_model=Comment)
def get_comment(comment_id: int,
                viewer_id: int = Depends(get_current_user_id),
                service: CommentService = Depends(get_comment_service)) -> Comment:
    return service.get_comment(comment_id=comment_id, viewer_id=viewer_id)

@router.patch("/comments/{comment_id}", response_model=Comment)
def update_comment(comment_id: int,
                   payload: CommentUpdate,
                   user_id: int = Depends(get_current_user_id),
                   service: CommentService = Depends(get_comment_service)) -> Comment:
    return service.update_comment(comment_id=comment_id, data=payload, user_id=user_id)

@router.delete("/comments/{comment_id}", status_code=204)
def delete_comment(comment_id: int,
                   user_id: int = Depends(get_current_user_id),
                   service: CommentService = Depends(get_comment_service)):
    return service.delete_comment(comment_id=comment_id, user_id=user_id)