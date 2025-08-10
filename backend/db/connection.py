# backend/db/connection.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Datos de conexión
DB_USER = "postgres"  # Cambia si tu usuario es distinto
DB_PASSWORD = "Yojansel18"
DB_HOST = "localhost"  # Cambia si tu host es distinto
DB_PORT = 5432
DB_NAME = "Cubicanet"   # ajusta si tu base se llama distinto

# URI de SQLAlchemy
DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Engine y sesión
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """
    Dependency para FastAPI o función de helper en Flask:
    yield una sesión y ciérrala luego.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
