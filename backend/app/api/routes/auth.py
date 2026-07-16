from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from core.database import get_db
from core.security import verificar_token
from schemas.usuario import UsuarioCreate, UsuarioResponse
from app.services import AuthService  


router = APIRouter(prefix="/auth", tags=["Autenticación"])

@router.post("/register", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def registrar_usuario(usuario_in: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_existente = AuthService.obtener_usuario_por_email(db, email=usuario_in.email)
    if usuario_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo electrónico ya está registrado"
        )
    return AuthService.crear_usuario(db, usuario_in)

@router.post("/login")
def iniciar_sesion(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = AuthService.autenticar_usuario(db, email=form_data.username, password=form_data.password)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    token_acceso = AuthService.crear_token_acceso(usuario)
    return {
        "access_token": token_acceso,
        "token_type": "bearer"
    }

@router.get("/me", response_model=UsuarioResponse)
def obtener_perfil(usuario_actual: dict = Depends(verificar_token), db: Session = Depends(get_db)):
    usuario = AuthService.obtener_usuario_por_email(db, email=usuario_actual.get("sub"))
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    return usuario