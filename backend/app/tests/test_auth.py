# Estos tests asumen un fixture `client` (TestClient de FastAPI) definido
# en conftest.py, apuntando a una base de datos de pruebas.


def test_registro_usuario_exitoso(client):
    respuesta = client.post("/api/auth/register", json={
        "nombre1": "Juan",
        "apellido1": "Perez",
        "correo": "juan.perez@example.com",
        "password": "clave123",
        "rol_usuario": "comprador",
    })
    assert respuesta.status_code == 201
    data = respuesta.json()
    assert data["correo"] == "juan.perez@example.com"
    assert "password" not in data
    assert "password_hash" not in data


def test_registro_correo_duplicado(client):
    payload = {
        "nombre1": "Ana",
        "apellido1": "Gomez",
        "correo": "ana@example.com",
        "password": "clave123",
    }
    client.post("/api/auth/register", json=payload)
    respuesta = client.post("/api/auth/register", json=payload)
    assert respuesta.status_code == 400


def test_login_credenciales_correctas(client):
    client.post("/api/auth/register", json={
        "nombre1": "Luisa",
        "apellido1": "Diaz",
        "correo": "luisa@example.com",
        "password": "clave123",
    })
    respuesta = client.post("/api/auth/login", json={
        "correo": "luisa@example.com",
        "password": "clave123",
    })
    assert respuesta.status_code == 200
    assert "access_token" in respuesta.json()


def test_login_credenciales_incorrectas(client):
    respuesta = client.post("/api/auth/login", json={
        "correo": "no-existe@example.com",
        "password": "loquesea",
    })
    assert respuesta.status_code == 401