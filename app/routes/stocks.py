from fastapi import APIRouter, Depends
from app.crud import anaylzePDFTest
from app.schemas.stocks import anaylzePDFTestResponse


router = APIRouter()

@router.get("/anaylzePDFTest", )
def get_anaylzePDFTest():
  return anaylzePDFTest()