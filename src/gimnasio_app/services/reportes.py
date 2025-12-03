"""
Módulo de Servicios - Reportes (Gimnasio)
Genera métricas y reportes sobre socios, asistencias y clases.
"""
from typing import Dict, Any, Optional
from datetime import datetime, date
from ..repositories.socios_repo import SociosRepo
from ..repositories.asistencias_repo import AsistenciasRepo
from ..repositories.clases_repo import ClasesRepo
from ..services.gestion_membresias import GestionMembresias


class GeneradorReportes:
    """Generador de reportes específicos del dominio gimnasio.

    Recibe los repositorios necesarios para calcular métricas:
    - socios_repo: lista y filtros de socios
    - asistencias_repo: asistencias registradas
    - clases_repo: clases programadas
    """

    def __init__(self, socios_repo: SociosRepo, asistencias_repo: AsistenciasRepo,
                 clases_repo: ClasesRepo, membresias_service: Optional[GestionMembresias] = None):
        self.socios_repo = socios_repo
        self.asistencias_repo = asistencias_repo
        self.clases_repo = clases_repo
        # servicio opcional para obtener membresías (si existe en la aplicación)
        self.membresias_service = membresias_service

    def total_socios(self) -> int:
        return len(self.socios_repo.listar())

    def total_socios_activos(self) -> int:
        return len(self.socios_repo.listar_activos())

    def total_socios_inactivos(self) -> int:
        return len(self.socios_repo.listar_inactivos())

    def asistencias_del_dia(self, fecha: date) -> int:
        return len(self.asistencias_repo.asistencias_del_dia(fecha))

    def clases_en_fecha(self, fecha: date) -> int:
        return len(self.clases_repo.listar_por_fecha(fecha))

    def reporte_resumen(self, fecha: Optional[date] = None) -> Dict[str, Any]:
        """Genera un resumen con métricas clave para la fecha indicada (por defecto hoy)."""
        fecha = fecha or date.today()
        fecha_generacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        resumen = {
            "fecha_generacion": fecha_generacion,
            "fecha_consulta": fecha.strftime("%Y-%m-%d"),
            "total_socios": self.total_socios(),
            "socios_activos": self.total_socios_activos(),
            "socios_inactivos": self.total_socios_inactivos(),
            "asistencias_hoy": self.asistencias_del_dia(fecha),
            "clases_hoy": self.clases_en_fecha(fecha),
        }

        # métricas de membresías (si se proporcionó el servicio)
        if self.membresias_service is not None:
            try:
                resumen["total_membresias"] = len(self.membresias_service.listar())
                resumen["membresias_activas"] = sum(1 for m in self.membresias_service.listar() if getattr(m, "esta_activa", lambda: False)())
            except Exception:
                resumen["total_membresias"] = 0
                resumen["membresias_activas"] = 0

        return resumen

