from typing import Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    full_name: Optional[str] = None # Imię i nazwisko opcjonalne

class UserCreate(UserBase):
    password: str  # Hasło przy tworzeniu użytkownika

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True  # Umożliwia zwrócenie danych z obiektów SQLAlchemy
