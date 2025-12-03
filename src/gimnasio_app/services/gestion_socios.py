from typing import Optional
from ..models.socio import Socio
from ..repositories.socios_repo import SociosRepo
from ..utils.validadores import Validadores


class GestionSocios:
    """Servicio para gestionar socios (alta, edición y consultas)."""

    def __init__(self):
        self.repo = SociosRepo()

    def registrar(self, dni: str, nombres: str, apellidos: str, telefono: str, correo: str) -> Socio:
        """Registra un nuevo socio tras validar sus datos."""
        Validadores.validar_nombre(nombres)
        Validadores.validar_apellido(apellidos)
        Validadores.validar_correo(correo)
        Validadores.validar_telefono(telefono)

        if self.repo.buscar_por_dni(dni):
            raise ValueError("Ya existe un socio con ese DNI")

        socio = Socio(dni, nombres, apellidos, telefono, correo)
        self.repo.agregar(socio)
        return socio

    def editar(self, dni: str, nombres: Optional[str] = None, apellidos: Optional[str] = None,
               telefono: Optional[str] = None, correo: Optional[str] = None) -> Socio:
        """Edita los datos de un socio existente aplicando validaciones cuando procede."""
        socio = self.repo.buscar_por_dni(dni)
        if not socio:
            raise ValueError("Socio no encontrado")

        if nombres is not None:
            Validadores.validar_nombre(nombres)
            socio.nombres = nombres

        if apellidos is not None:
            Validadores.validar_apellido(apellidos)
            socio.apellidos = apellidos

        if telefono is not None:
            Validadores.validar_telefono(telefono)
            socio.telefono = telefono

        if correo is not None:
            Validadores.validar_correo(correo)
            socio.correo = correo

        return socio

    def buscar_por_dni(self, dni: str) -> Optional[Socio]:
        return self.repo.buscar_por_dni(dni)

    def activar(self, dni: str) -> Socio:
        socio = self.buscar_por_dni(dni)
        if not socio:
            raise ValueError("Socio no encontrado")
        socio.activar()
        return socio

    def desactivar(self, dni: str) -> Socio:
        socio = self.buscar_por_dni(dni)
        if not socio:
            raise ValueError("Socio no encontrado")
        socio.desactivar()
        return socio

    def asignar_membresia(self, dni: str, membresia) -> Socio:
        socio = self.buscar_por_dni(dni)
        if not socio:
            raise ValueError("Socio no encontrado")
        socio.asignar_membresia(membresia)
        membresia.activar()
        return socio

    def listar(self):
        return self.repo.listar()

    def listar_activos(self):
        return self.repo.listar_activos()

    def listar_inactivos(self):
        return self.repo.listar_inactivos()
