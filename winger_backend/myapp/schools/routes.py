from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from myapp.schools import crud, schemas

router = APIRouter()

@router.get("/", response_model=List[schemas.School])
def get_schools(db: Session = Depends(get_db)):
    return crud.get_schools(db)

@router.post("/", response_model=schemas.School)
def create_school(school: schemas.SchoolCreate, db: Session = Depends(get_db)):
    return crud.create_school(db, school)
