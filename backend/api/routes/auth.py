from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from models.user import User, UserCreate, UserRead
from core.security import create_access_token
from api.dependencies import get_user_service, get_current_user
from services.user_service import UserService, UserAlreadyExistsError, InvalidCredentialsError

router = APIRouter(tags=["auth"])

@router.post("/signup", response_model=UserRead, status_code=201)
def signup(payload: UserCreate, service: UserService = Depends(get_user_service)):
    try:
        return service.register(payload)
    except UserAlreadyExistsError:
        raise HTTPException(status_code=409, detail="Username already registered")

@router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends(),
          service: UserService = Depends(get_user_service)):
    try:
        user = service.authenticate(form.username, form.password)
    except InvalidCredentialsError:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return {"access_token": create_access_token(user.username), "token_type": "bearer"}

@router.get("/me", response_model=UserRead)
def me(current_user: User = Depends(get_current_user)):
    return current_user