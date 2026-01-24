from fastapi import APIRouter

from .routers.root import router as root_router
from .routers.modules import router as modules_router
from .routers.steps import router as steps_router

router = APIRouter(
    prefix=""
)

router.include_router(root_router)
router.include_router(modules_router)
router.include_router(steps_router)

