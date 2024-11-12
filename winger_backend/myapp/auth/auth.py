from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from myapp.auth import schemas, crud
from myapp.db.session import get_db

router = APIRouter()

@router.post("/register", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@router.post("/login")
async def register():
    return {"message": "Logged in"}