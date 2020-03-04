from fastapi import APIRouter
from loguru import logger
from . import test

router = APIRouter()

router.include_router(test.router, tags=["test"], prefix="/test")
