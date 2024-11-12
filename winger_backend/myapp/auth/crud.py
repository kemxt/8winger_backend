from sqlalchemy.orm import Session
from myapp.auth import models, schemas
from myapp.auth.hashing import Hash  # Jeśli masz moduł do hashowania haseł

# Tworzenie nowego użytkownika
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        email=user.email,
        full_name=user.full_name,
        hashed_password=Hash.bcrypt(user.password)  # Użycie metody haszującej
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Pobieranie użytkownika po e-mailu
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()
