from sqlalchemy import Column, Integer, String
from fastapi import APIRouter

router = APIRouter()

class User:
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)

@router.post('/')
async def add_user():
    return {"message": "Create a new user"}

@router.get('/')
async def get_users():
    return {"message": "All users"}

