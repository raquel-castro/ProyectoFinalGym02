"""
Módulo de Modelos - Clase
Modela una clase del gimnasio (ej. Spinning, Yoga) con cupo e inscritos.
"""
from typing import List, Any, Optional
from datetime import date, time


class Clase:
    """Representa una clase programada.

    Atributos:
        id (int): identificador
        nombre (str)
        instructor: referencia a Instructor
        cupo_maximo (int)
        fecha (date)
        hora (time)
        inscritos (List): lista de socios inscritos
    """

    def __init__(self, clase_id: int, nombre: str, instructor: Any, cupo_maximo: int, fecha: date, hora: time):
        if cupo_maximo <= 0:
            raise ValueError("El cupo máximo debe ser mayor que 0")

        self.id: int = int(clase_id)
        self.nombre: str = nombre
        self.instructor = instructor
        self.cupo_maximo: int = int(cupo_maximo)
        self.fecha: date = fecha
        self.hora: time = hora
        self.inscritos: List[Any] = []

    def tiene_cupo(self) -> bool:
        return len(self.inscritos) < self.cupo_maximo

    def inscribir(self, socio: Any) -> None:
        if not self.tiene_cupo():
            raise ValueError("La clase está llena.")
        if socio in self.inscritos:
            return
        self.inscritos.append(socio)

    def quitar(self, socio: Any) -> None:
        if socio in self.inscritos:
            self.inscritos.remove(socio)

    def es_de_fecha(self, fecha_referencia: date) -> bool:
        return self.fecha == fecha_referencia

    def __repr__(self) -> str:
        return (
            f"<Clase {self.id}: {self.nombre} {self.fecha} {self.hora}, "
            f"inscritos={len(self.inscritos)}/{self.cupo_maximo}>"
        )
