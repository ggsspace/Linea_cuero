from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import verificar_token
from app.models.usuario import Usuario, RolUsuario

# Le dice a FastAPI (y a /docs) donde se obtiene el token: en el login.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> Usuario:
    """
    Dependencia base: cualquier ruta protegida la usa.
    verificar_token() (en core/security.py) ya lanza 401 si el token
    esta vencido, alterado o corrupto.
    """
    payload = verificar_token(token)
    id_usuario = payload.get("sub")
    if id_usuario is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token invalido",
        )

    usuario = db.query(Usuario).filter(Usuario.id_usuario == int(id_usuario)).first()
    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no encontrado",
        )
    return usuario


def require_role(*roles_permitidos: RolUsuario):
    """
    Uso: dependencies=[Depends(require_role(RolUsuario.administrador))]
    Encadena get_current_user y ademas verifica el rol (RBAC).
    """
    def wrapper(usuario_actual: Usuario = Depends(get_current_user)) -> Usuario:
        if usuario_actual.rol_usuario not in roles_permitidos:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No tienes permiso para realizar esta accion",
            )
        return usuario_actual
    return wrapper