import os
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET", "mi-clave-secreta-de-desarrollo")
ALGORITHM = "HS256"

# Le dice a FastAPI que busque el token en las cabeceras HTTP (Header: Authorization Bearer <TOKEN>)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

def verificar_token(token: str = Depends(oauth2_scheme)) -> dict:
    
    """
    Decodifica el JWT, verifica si es válido o si ya expiró.
    """
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        return payload  # Retorna el diccionario con la info encriptada (sub, email, role)
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Su sesión ha expirado. Por favor, inicie sesión nuevamente."
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token de autenticación no válido."
        )

def verificar_rol(roles_permitidos: list):
    """
    Filtra el acceso a los endpoints de la API según el rol del usuario de SQLAlchemy.
    Ejemplo: verificar_rol(["vendedor", "admin"])
    """
    def dependencia(payload: dict = Depends(verificar_token)):
        usuario_rol = payload.get("role")
        if usuario_rol not in roles_permitidos:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No posees los permisos necesarios para realizar esta acción."
            )
        return payload
    return dependencia