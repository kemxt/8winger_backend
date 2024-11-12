from sqlalchemy import Column, Integer, String
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_schools():
    return {"message": "Get all schools"}


@router.post("/")
async def create_school():
    return {"message": "Create a new school"}
