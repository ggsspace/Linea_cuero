import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Carga las variables de entorno del archivo backend/.env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("Error: La variable DATABASE_URL no está configurada en backend/.env")

# El motor de conexión de SQLAlchemy para PostgreSQL
engine = create_engine(
    DATABASE_URL, 
    pool_pre_ping=True   #'pool_pre_ping=True' ayuda a revivir conexiones caídas automáticamente
)

# Configurar la fábrica de sesiones de base de datos
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

# Clase Base para que todos los modelos hereden de ella
Base = declarative_base()

# Dependencia para inyectar la sesión en los endpoints de FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        