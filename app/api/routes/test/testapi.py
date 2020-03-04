from fastapi import APIRouter

from app.module import Functions

from app.module import ResultModel

from typing import List
from loguru import logger

router = APIRouter()


@logger.catch
@router.get("", response_model=ResultModel)
async def search(query: str = ""):
    func = Functions()
    return func.process(query)
