from typing import List
from ..models.asistencia import Asistencia
from ..repositories.asistencias_repo import AsistenciasRepo


class GestionAsistencias:
    """Servicio para registrar y consultar asistencias."""

    def __init__(self):
        self.repo = AsistenciasRepo()

    def registrar_asistencia(self, socio) -> Asistencia:
        asistencia = Asistencia(socio)
        self.repo.agregar(asistencia)
        return asistencia

    def historial_por_socio(self, socio) -> List[Asistencia]:
        return self.repo.historial_por_socio(socio)

    def asistencias_del_dia(self, fecha) -> List[Asistencia]:
        return self.repo.asistencias_del_dia(fecha)
