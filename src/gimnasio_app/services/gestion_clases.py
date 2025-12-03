from datetime import date, time
from typing import List, Optional
from ..models.clase import Clase
from ..repositories.clases_repo import ClasesRepo


class GestionClases:
    """Servicio para gestionar tipos de clases y la inscripción de socios."""

    def __init__(self):
        self.repo = ClasesRepo()
        self.tipos_clase = set()

    def registrar_tipo_clase(self, nombre_tipo: str) -> None:
        self.tipos_clase.add(nombre_tipo)

    def obtener_tipos_clase(self) -> List[str]:
        basicas = {"Spinning", "Zumba", "Yoga", "Pilates", "Boxeo", "Baile"}
        return sorted(list(self.tipos_clase.union(basicas)))

    def crear(self, nombre: str, instructor, cupo_maximo: int, fecha: date, hora_str: str) -> Clase:
        hh, mm = map(int, hora_str.split(":"))
        hora = time(hh, mm)
        clase = Clase(self.repo.next_id, nombre, instructor, cupo_maximo, fecha, hora)
        self.repo.next_id += 1
        self.repo.agregar(clase)
        return clase

    def inscribir_socio(self, clase_id: int, socio) -> Clase:
        clase = self.repo.buscar_por_id(clase_id)
        if not clase:
            raise ValueError("Clase no encontrada")
        clase.inscribir(socio)
        return clase

    def remover_socio(self, clase_id: int, socio) -> Clase:
        clase = self.repo.buscar_por_id(clase_id)
        if not clase:
            raise ValueError("Clase no encontrada")
        clase.quitar(socio)
        return clase

    def listar(self) -> List[Clase]:
        return self.repo.listar()

    def clases_de_hoy(self, fecha_hoy: Optional[date] = None) -> List[Clase]:
        fecha_hoy = fecha_hoy or date.today()
        return self.repo.listar_por_fecha(fecha_hoy)

    def buscar_por_id(self, clase_id: int) -> Optional[Clase]:
        return self.repo.buscar_por_id(clase_id)
