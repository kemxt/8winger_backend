# myapp/schools/crud.py
from sqlalchemy.orm import Session
from myapp.schools import models, schemas

def create_school(db: Session, school: schemas.SchoolCreate):
    db_school = models.School(name=school.name, address=school.address)
    db.add(db_school)
    db.commit()
    db.refresh(db_school)
    return db_school

def get_schools(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.School).offset(skip).limit(limit).all()
