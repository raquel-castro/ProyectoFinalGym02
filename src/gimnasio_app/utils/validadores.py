"""
Módulo de Utilidades - Validadores
Define funciones para validar entrada de datos
"""
import re


class Validadores:
    """Clase con métodos estáticos para validaciones de campos comunes."""

    @staticmethod
    def validar_nombre(nombre: str) -> bool:
        """Valida que el nombre sea texto, tenga más de 3 caracteres y solo contenga letras.

        Acepta letras (incluye acentos), espacios y guiones.
        Lanza ValueError en caso de invalididad.
        """
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser texto")
        nombre = nombre.strip()
        if len(nombre) <= 3:
            raise ValueError("El nombre debe tener más de 3 caracteres")
        # Permitir letras latinas con acentos, espacios y guiones
        if not re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s\-]+$", nombre):
            raise ValueError("El nombre solo debe contener letras, espacios o guiones")
        return True

    @staticmethod
    def validar_dni(dni: str) -> bool:
        """Valida que el DNI contenga exactamente 8 dígitos numéricos."""
        if not isinstance(dni, str):
            raise ValueError("El DNI debe ser texto")
        dni = dni.strip()
        if not re.match(r"^\d{8}$", dni):
            raise ValueError("El DNI debe contener exactamente 8 dígitos")
        return True

    @staticmethod
    def validar_apellido(apellido: str) -> bool:
        """Valida que el apellido sea texto, tenga más de 3 caracteres y solo contenga letras.

        Comportamiento igual que `validar_nombre`.
        """
        if not isinstance(apellido, str):
            raise ValueError("El apellido debe ser texto")
        apellido = apellido.strip()
        if len(apellido) <= 3:
            raise ValueError("El apellido debe tener más de 3 caracteres")
        if not re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s\-]+$", apellido):
            raise ValueError("El apellido solo debe contener letras, espacios o guiones")
        return True

    @staticmethod
    def validar_telefono(telefono: str) -> bool:
        """Valida que el teléfono contenga exactamente 9 dígitos y solo números.

        Lanza ValueError en caso de invalididad.
        """
        if not isinstance(telefono, str):
            raise ValueError("El teléfono debe ser texto")
        telefono = telefono.strip()
        if not re.match(r"^\d{9}$", telefono):
            raise ValueError("El teléfono debe contener exactamente 9 dígitos y solo números")
        return True

    @staticmethod
    def validar_correo(correo: str) -> bool:
        """Valida correo : longitud > 3, contiene '@' y termina en .com o .pe.
        """
        if not isinstance(correo, str):
            raise ValueError("El correo debe ser texto")
        correo = correo.strip()
        if len(correo) <= 3:
            raise ValueError("El correo debe tener más de 3 caracteres")
        if "@" not in correo:
            raise ValueError("El correo debe contener '@'")
        dominio = correo.lower().split("@")[-1]
        if not (dominio.endswith(".com") or dominio.endswith(".pe")):
            raise ValueError("El correo debe terminar en .com o .pe")
        # comprobación básica adicional 
        if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", correo):
            raise ValueError("Formato de correo inválido")
        return True


__all__ = ["Validadores"]
