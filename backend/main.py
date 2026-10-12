from fastapi import FastAPI, Request
from db.db import init_db
import models.user     # noqa: F401  ← registers the user table on SQLModel.metadata
import models.journey  # noqa: F401  ← registers the journey table
from api.routes.journey import router as journey_router
from fastapi.responses import JSONResponse
from services.journey_service import JourneyNotFoundError, JourneyForbiddenError
from api.routes.auth import router as auth_router

app = FastAPI()


@app.exception_handler(JourneyNotFoundError)
async def _journey_not_found(request: Request, exc: JourneyNotFoundError):
    return JSONResponse(status_code=404, content={"detail": str(exc)})

@app.exception_handler(JourneyForbiddenError)
async def _journey_forbidden(request: Request, exc: JourneyForbiddenError):
    return JSONResponse(status_code=403, content={"detail": str(exc)})


init_db()
@app.get("/")
async def root():
    return {"message": "Trace APP is running!"}

app.include_router(auth_router)
app.include_router(journey_router)