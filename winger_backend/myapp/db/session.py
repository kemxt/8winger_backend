from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv


load_dotenv()

# Pobierz DATABASE_URL z pliku .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Inicjalizacja bazy
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Bazowa klasa dla wszystkich modeli
Base = declarative_base()

# Tworzenie sesji do bazy danych
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Funkcja, która pozwala uzyskać nową sesję w każdej operacji
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
