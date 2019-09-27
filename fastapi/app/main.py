from fastapi import FastAPI
from app.router.api import router as api_router
from app.core.config import PROJECT_NAME, DESCRIPTION, VERSION

app = FastAPI(
    title=PROJECT_NAME,
    description=DESCRIPTION,
    version=VERSION)

app.include_router(api_router)