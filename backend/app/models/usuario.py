import enum

from sqlalchemy import Column, Integer, String, Enum, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class RolUsuario(str, enum.Enum):
    comprador = "comprador"
    proveedor = "proveedor"
    administrador = "administrador"


class EstadoUsuario(str, enum.Enum):
    pendiente = "pendiente"
    activo = "activo"
    rechazado = "rechazado"


class Usuario(Base):
    __tablename__ = "usuario"

    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre1 = Column(String(50), nullable=False)
    nombre2 = Column(String(50), nullable=True)
    apellido1 = Column(String(50), nullable=False)
    apellido2 = Column(String(50), nullable=True)
    correo = Column(String(120), unique=True, index=True, nullable=False)

    # Solo se guarda el hash de la contrasena, nunca el texto plano.
    password_hash = Column(String(255), nullable=False)
    telefono = Column(String(20), nullable=True)

    rol_usuario = Column(
        Enum(RolUsuario, name="rol_usuario_enum"),
        nullable=False,
        default=RolUsuario.comprador,
    )
    estado_usuario = Column(
        Enum(EstadoUsuario, name="estado_usuario_enum"),
        nullable=False,
        default=EstadoUsuario.pendiente,
    )

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    productos = relationship("Producto", back_populates="proveedor")
    carrito = relationship("Carrito", back_populates="usuario", uselist=False)
    reservas = relationship("Reserva", back_populates="usuario")