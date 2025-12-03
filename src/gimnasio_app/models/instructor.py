"""
Módulo de Modelos - Instructor
Modela un instructor con su especialidad.
"""
from typing import Any


class Instructor:
    """Representa a un instructor del gimnasio."""

    def __init__(self, instructor_id: int, nombre: str, especialidad: str):
        self.id: int = int(instructor_id)
        self.nombre: str = nombre
        self.especialidad: str = especialidad

    def __repr__(self) -> str:
        return f"<Instructor {self.id}: {self.nombre} ({self.especialidad})>"
