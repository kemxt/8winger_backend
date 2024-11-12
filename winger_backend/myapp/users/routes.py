from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from myapp.users import crud, schemas

router = APIRouter()

@router.get("/{user_id}", response_model=schemas.UserInDB)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/update/{user_id}", response_model=schemas.UserInDB)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    # Update user logic
    db_user.email = user.email
    db_user.hashed_password = get_password_hash(user.password)
    db.commit()
    db.refresh(db_user)
    return db_user
