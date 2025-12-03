"""
Módulo de Modelos - Asistencia
Registra la asistencia diaria de un socio.
"""
from datetime import datetime, date, time
from typing import Any


class Asistencia:
    """Representa una asistencia registrada para un socio.

    Atributos:
        socio: referencia al socio
        fecha (date)
        hora (time)
    """

    def __init__(self, socio: Any):
        ahora = datetime.now()
        self.socio = socio
        self.fecha: date = ahora.date()
        self.hora: time = ahora.time()

    def __repr__(self) -> str:
        return f"<Asistencia {self.socio.dni}: {self.fecha} {self.hora}>"
