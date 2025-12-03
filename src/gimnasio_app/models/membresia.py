"""
Módulo de Modelos - Membresía
Modela tipos de membresía, activación y vencimiento.
"""
from datetime import date, datetime, timedelta
from typing import Optional


class Membresia:
    """Representa una membresía con duración en días.

    Atributos:
        tipo (str)
        duracion_dias (int)
        fecha_inicio (Optional[date])
        fecha_fin (Optional[date])
    """

    def __init__(self, tipo: str, duracion_dias: int):
        self.tipo: str = tipo
        self.duracion_dias: int = int(duracion_dias)
        self.fecha_inicio: Optional[date] = None
        self.fecha_fin: Optional[date] = None

    def activar(self) -> None:
        self.fecha_inicio = datetime.now().date()
        self.fecha_fin = self.fecha_inicio + timedelta(days=self.duracion_dias)

    def esta_activa(self) -> bool:
        if not self.fecha_inicio or not self.fecha_fin:
            return False
        hoy = datetime.now().date()
        return self.fecha_inicio <= hoy <= self.fecha_fin

    def renovar(self) -> None:
        if not self.fecha_fin:
            self.activar()
        else:
            # comenzar la renovación desde la fecha_fin actual
            self.fecha_inicio = self.fecha_fin
            self.fecha_fin = self.fecha_inicio + timedelta(days=self.duracion_dias)

    def __repr__(self) -> str:
        estado = "Activa" if self.esta_activa() else "Vencida"
        return (
            f"<Membresía {self.tipo}: {estado}, "
            f"{self.fecha_inicio} - {self.fecha_fin}>"
        )
