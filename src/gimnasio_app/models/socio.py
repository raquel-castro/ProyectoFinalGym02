"""
Módulo de Modelos - Socio
Representa a un socio del gimnasio.
"""
from datetime import datetime
from typing import Optional

from ..utils.validadores import Validadores


class Socio:
    """Entidad que modela un socio.

    Atributos:
        dni (str): Identificador nacional
        nombres (str)
        apellidos (str)
        telefono (str)
        correo (str)
        fecha_inscripcion (str): Fecha de alta en formato YYYY-MM-DD HH:MM:SS
        estado_activo (bool)
        membresia: referencia a la membresía asignada o None
    """

    def __init__(self, dni: str, nombres: str, apellidos: str, telefono: str, correo: str):
        if not dni or not str(dni).strip():
            raise ValueError("El DNI no puede estar vacío")
        # validar nombres/apellidos/teléfono/correo usando Validadores
        Validadores.validar_nombre(nombres)
        Validadores.validar_apellido(apellidos)
        Validadores.validar_telefono(telefono)
        Validadores.validar_correo(correo)

        self.dni: str = str(dni).strip()
        self.nombres: str = nombres.strip()
        self.apellidos: str = apellidos.strip()
        self.telefono: str = telefono.strip()
        self.correo: str = correo.strip()
        # guardar fecha de inscripción como string (estilo profesor)
        self.fecha_inscripcion: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.estado_activo: bool = True
        self.membresia = None

    def asignar_membresia(self, membresia) -> None:
        self.membresia = membresia

    def activar(self) -> None:
        self.estado_activo = True

    def desactivar(self) -> None:
        self.estado_activo = False

    def __str__(self) -> str:
        return f"{self.dni} | {self.nombres} {self.apellidos} | {self.telefono}"

    def __repr__(self) -> str:
        estado = "Activo" if self.estado_activo else "Inactivo"
        return (
            f"<Socio {self.dni}: {self.nombres} {self.apellidos}, "
            f"Estado={estado}, Membresía={self.membresia}>"
        )
