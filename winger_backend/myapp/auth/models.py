from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from myapp.db.session import Base  # Importuj Base z pliku database.py

class User(Base):
    __tablename__ = 'users'  # Nazwa tabeli w bazie danych

    id = Column(Integer, primary_key=True, index=True)  # ID użytkownika
    email = Column(String, unique=True, index=True)  # Unikalny adres e-mail
    hashed_password = Column(String)  # Hasło (hashed)
    full_name = Column(String, index=True)  # Imię i nazwisko użytkownika
    is_active = Column(Boolean, default=True)  # Status aktywności użytkownika

    # Inne relacje i kolumny możesz dodać w zależności od potrzeb
