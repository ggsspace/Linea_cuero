import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from core.database import Base, get_db
from core.security import verificar_token



# Configuración de Base de Datos Temporal para Pruebas (SQLite)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_temp.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function", autouse=True)
def setup_db():
    """Crea las tablas antes de cada test y las elimina al finalizar."""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def override_get_db():
    """Reemplaza la dependencia de base de datos real por la de pruebas."""
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# se pasa de la base de datos a la base de pruebas para que no afecte la base de datos real
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


# pruebas unitarias 


def test_registro_usuario_exitoso():
    """Prueba que un usuario se pueda registrar correctamente."""
    payload = {
        "email": "test@compusena.edu.co",
        "password": "securepassword123",
        "nombre": "Pedro Perez"
    }
    
    response = client.post("/api/auth/register", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == payload["email"]
    assert "id" in data


def test_login_exitoso():
    """Prueba que un usuario registrado reciba un JWT Token al loguearse."""
    # 1. Registrar usuario primero
    payload = {
        "email": "pedro@compusena.edu.co",
        "password": "mypassword",
        "nombre": "Pedro Perez"
    }
    client.post("/api/auth/register", json=payload)

    # 2. Intentar hacer Login
    login_data = {
        "username": payload["email"],  # FastAPI OAuth2 usa 'username'
        "password": payload["password"]
    }
    response = client.post("/api/auth/login", data=login_data)
    assert response.status_code == 200
    
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_credenciales_incorrectas():
    """Prueba que el sistema rechace inicios de sesión con contraseñas erróneas."""
    login_data = {
        "username": "usuario_inexistente@correo.com",
        "password": "wrong_password"
    }
    response = client.post("/api/auth/login", data=login_data)
    assert response.status_code == 401  # Unauthorized
    assert response.json()["detail"] == "Credenciales incorrectas"


def test_acceso_ruta_protegida_sin_token():
    """Prueba que las rutas protegidas bloqueen peticiones sin credenciales."""
    response = client.get("/api/usuarios/me")  # Endpoint protegido típico
    assert response.status_code == 401


def test_acceso_ruta_protegida_con_token_valido():
    """Prueba que un JWT legítimo dé acceso exitoso a recursos protegidos."""
    # 1. Creamos y registramos un usuario
    payload = {
        "email": "pedro.perez@compusena.edu.co",
        "password": "password123",
        "nombre": "Pedro Perez"
    }
    client.post("/api/auth/register", json=payload)

    # 2. Obtenemos el token
    login_res = client.post("/api/auth/login", data={"username": payload["email"], "password": payload["password"]})
    token = login_res.json()["access_token"]

    # 3. Consumimos el endpoint protegido enviando el Header de Autorización
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/api/usuarios/me", headers=headers)
    
    assert response.status_code == 200
    assert response.json()["email"] == payload["email"]