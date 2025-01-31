from fastapi import APIRouter, Depends
from app.crud import anaylzePDFTest


router = APIRouter()

@router.get("/anaylzePDFTest")
def anaylzePDFTest():
  return anaylzePDFTest