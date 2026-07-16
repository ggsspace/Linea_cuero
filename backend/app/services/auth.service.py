from datetime import datetime, timedelta
from typing import Optional
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from models.usuario import Usuario
from schemas.usuario import UsuarioCreate

# Configuración de encriptación de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Configuración de JWT (Se deberían leer de app/core/config.py)
SECRET_KEY = "mi-clave-secreta-de-desarrollo"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

class AuthService:

    @staticmethod
    def verificar_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def obtener_password_hash(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def obtener_usuario_por_email(db: Session, email: str) -> Optional[Usuario]:
        return db.query(Usuario).filter(Usuario.email == email).first()

    @staticmethod
    def crear_usuario(db: Session, usuario_in: UsuarioCreate) -> Usuario:
        db_usuario = Usuario(
            nombre=usuario_in.nombre,
            email=usuario_in.email,
            password_hash=AuthService.obtener_password_hash(usuario_in.password),
            rol=usuario_in.rol
        )
        db.add(db_usuario)
        db.commit()
        db.refresh(db_usuario)
        return db_usuario

    @staticmethod
    def autenticar_usuario(db: Session, email: str, password: str) -> Optional[Usuario]:
        usuario = AuthService.obtener_usuario_por_email(db, email)
        if not usuario:
            return None
        if not AuthService.verificar_password(password, usuario.password_hash):
            return None
        return usuario

    @staticmethod
    def crear_token_acceso(usuario: Usuario) -> str:
        tiempo_expiracion = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        datos_payload = {
            "sub": usuario.email,
            "id": usuario.id,
            "rol": usuario.rol,
            "exp": tiempo_expiracion
        }
        token_jwt = jwt.encode(datos_payload, SECRET_KEY, algorithm=ALGORITHM)
        return token_jwt