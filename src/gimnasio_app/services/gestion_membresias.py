from typing import List
from ..models.membresia import Membresia


class GestionMembresias:
    """Servicio para crear y gestionar membresías."""

    def __init__(self):
        self.membresias_creadas: List[Membresia] = []

    def crear(self, etiqueta: str, dias: int) -> Membresia:
        """Crea y activa una nueva membresía."""
        m = Membresia(etiqueta, dias)
        m.activar()
        self.membresias_creadas.append(m)
        return m

    def renovar(self, membresia: Membresia) -> Membresia:
        """Renueva la membresía pasada."""
        membresia.renovar()
        return membresia

    def verificar_activa(self, membresia: Membresia) -> bool:
        """Devuelve True si la membresía está activa."""
        return membresia.esta_activa()

    def listar(self) -> List[Membresia]:
        return self.membresias_creadas
