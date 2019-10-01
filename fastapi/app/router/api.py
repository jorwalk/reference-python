from fastapi import APIRouter
from .endpoint.root import router as root_router

router = APIRouter()
router.include_router(root_router)

