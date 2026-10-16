from fastapi import FastAPI, Request
from db.db import init_db
from api.routes.journey import router as journey_router
from fastapi.responses import JSONResponse
from api.routes.auth import router as auth_router
from api.routes.milestone import router as milestone_router
from api.routes.progress import router as progress_router
from core.errors import AppError

app = FastAPI()


@app.exception_handler(AppError)
async def _app_error(request: Request, exc: AppError):
    return JSONResponse(status_code=exc.status_code, content={"detail": str(exc)})


init_db()


app.include_router(auth_router)
app.include_router(journey_router)
app.include_router(milestone_router)
app.include_router(progress_router)