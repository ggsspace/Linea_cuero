from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.middlewares.auth import get_current_user, require_role
from app.models.usuario import Usuario, RolUsuario, EstadoUsuario
from app.schemas.usuario import UsuarioResponse, UsuarioEstadoUpdate

router = APIRouter(prefix="/api/usuarios", tags=["usuarios"])


@router.get("/me", response_model=UsuarioResponse)
def obtener_mi_perfil(usuario_actual: Usuario = Depends(get_current_user)):
    return usuario_actual


@router.get(
    "",
    response_model=List[UsuarioResponse],
    dependencies=[Depends(require_role(RolUsuario.administrador))],
)
def listar_usuarios(estado: Optional[EstadoUsuario] = None, db: Session = Depends(get_db)):
    """Solo el admin ve la lista completa; puede filtrar por estado
    (ej. ?estado=pendiente para revisar los proveedores por aprobar)."""
    query = db.query(Usuario)
    if estado is not None:
        query = query.filter(Usuario.estado_usuario == estado)
    return query.all()


@router.patch(
    "/{id_usuario}/estado",
    response_model=UsuarioResponse,
    dependencies=[Depends(require_role(RolUsuario.administrador))],
)
def cambiar_estado_usuario(id_usuario: int, cambio: UsuarioEstadoUpdate, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    if usuario is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")

    usuario.estado_usuario = cambio.estado_usuario
    db.commit()
    db.refresh(usuario)
    return usuario