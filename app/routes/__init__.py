from fastapi import APIRouter
from .user import router as user_router
from .stocks import router as stocks_router

router = APIRouter()

router.include_router(user_router, prefix="/users", tags=["Users"])
router.include_router(stocks_router, prefix="/stocks", tags=["Stocks"])