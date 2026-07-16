from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.core.database import engine, Base

# Importar los modelos (se deben importar para que Base detecte las tablas al arrancar)
# Cuando tus compañeros los creen, solo los importas aquí:
# from models import user, event, product 

# Inicializar/Crear las tablas en PostgreSQL si aún no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Línea Cuero API",
    description="Backend oficial con SQLAlchemy y PostgreSQL para la gestión de stands virtuales.",
    version="1.0.0"
)

# Configuración de CORS para conectar con React (Vite)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción se cambia por la URL real del frontend
    allow_credentials=True,
    allow_methods=["*"],  # Permite GET, POST, PUT, DELETE
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "status": "online",
        "database": "PostgreSQL (SQLAlchemy Connected)",
        "message": "Estructura base de Línea Cuero lista y funcionando."
    }

# --- REGISTRO DE ENRUTADORES VACÍOS ---
# Tus compañeros solo deberán crear sus archivos de rutas y descomentar estas líneas:
#
# from routes import auth, events, products
# app.include_router(auth.router, prefix="/api/auth", tags=["Autenticación"])
# app.include_router(events.router, prefix="/api/events", tags=["Stands y Eventos"])
# app.include_router(products.router, prefix="/api/products", tags=["Catálogo"])