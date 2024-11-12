from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from myapp.db.session import Base  # Bazowa klasa SQLAlchemy

class User(Base):
    __tablename__ = 'users'  # Nazwa tabeli w bazie danych

    id = Column(Integer, primary_key=True, index=True)  # Kolumna id, klucz główny
    email = Column(String, unique=True, index=True)  # Kolumna email, unikalna
    hashed_password = Column(String)  # Kolumna dla hasła (zahaszowanego)
    full_name = Column(String, index=True)  # Kolumna dla imienia i nazwiska
    is_active = Column(Boolean, default=True)  # Kolumna dla statusu aktywności użytkownika
    posts = relationship("Post", back_populates="owner")

class School(Base):
    __tablename__ = "schools"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)
