from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
 
from app.core.database import get_db
from app.schemas.usuario import UsuarioCreate, UsuarioLogin, UsuarioResponse, TokenResponse
from app.services import auth_service

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.post("/register", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def register(usuario_in: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_existente = auth_service.obtener_usuario_por_correo(db, usuario_in.correo)
    if usuario_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ese correo ya esta registrado",
        )
    return auth_service.crear_usuario(db, usuario_in)


@router.post("/login", response_model=TokenResponse)    
def login(usuario_in: UsuarioLogin, db: Session = Depends(get_db)):
    usuario = auth_service.autenticar_usuario(db, credenciales.correo, credenciales.password)
    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo o contrasena incorrectos",
        )
    if usuario.estado_usuario.value == "rechazado":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Tu registro fue rechazado, contacta al administrador",
        )
 
    access_token = auth_service.crear_token_acceso(usuario)
    return TokenResponse(access_token=access_token)