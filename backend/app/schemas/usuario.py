from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

from backend.app.models.usuario import RolUsuario

class UsuarioBase(BaseModel):
    nombre1: str
    nombre2: Optional[str] = None
    apellido1: str
    apellido2: Optional[str] = None
    telefono: Optional[str] = None  
    email: EmailStr
    
   

class UsuarioCreate(UsuarioBase):
    rol_usuario: RolUsuario = RolUsuario.comprador
    password: str = Field(..., min_length=6, max_length=100)


class UsuarioLogin(BaseModel):
    correo: EmailStr
    password: str



class UsuarioUpdate(BaseModel):

    nombre1: Optional[str] = Field(None, min_length=3, max_length=100)
    nombre2: Optional[str] = Field(None, min_length=3, max_length=100)
    apellido1: Optional[str] = Field(None, min_length=3, max_length=100)
    apellido2: Optional[str] = Field(None, min_length=3, max_length=100)
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=6, max_length=100)
    rol: Optional[str] = None
    activo: Optional[bool] = None


class UsuarioEstadoUpdate(BaseModel):
    """Para que el admin apruebe o rechace un registro (RF: gestion de estado)."""
estado_usuario: EstadoUsuario




class UsuarioResponse(UsuarioBase):
    id: int
    activo: bool
    creado_en: datetime

    class Config:
        from_attributes = True
        
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
        
        
    