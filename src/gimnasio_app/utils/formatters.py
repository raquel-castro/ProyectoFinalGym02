"""
Módulo de Utilidades - Formateadores
Define funciones para formatear y presentar datos
"""
from datetime import date, datetime
from typing import List, Dict, Any, Callable


class Formateadores:
    """Clase con métodos estáticos para formatear datos en la aplicación."""

    @staticmethod
    def formatear_fecha(fecha) -> str:
        """Formatea objetos date/datetime a DD/MM/YYYY, o los convierte a str.

        Acepta `date`, `datetime` o cualquier otro objeto convertible a cadena.
        """
        if isinstance(fecha, (date, datetime)):
            return fecha.strftime("%d/%m/%Y")
        return str(fecha)

    @staticmethod
    def formatear_monto(monto: float) -> str:
        """Formatea un valor numérico como moneda local (S/.) con dos decimales."""
        try:
            return f"S/.{float(monto):.2f}"
        except Exception:
            return str(monto)

    @staticmethod
    def formatear_lista(items: List[Any], formateador_item: Callable[[Any], str]) -> str:
        """Formatea una lista de objetos usando una función formateadora por ítem.

        - `items`: lista de objetos (puede estar vacía)
        - `formateador_item`: función que recibe un objeto y devuelve su representación en texto
        """
        if not items:
            return "No hay elementos para mostrar"
        filas = [formateador_item(i) for i in items]
        return "\n".join(filas)

    @staticmethod
    def formatear_lista_simples(strings: List[str]) -> str:
        """Formatea una lista simple de cadenas en varias líneas con numeración."""
        if not strings:
            return "No hay elementos para mostrar"
        return "\n".join(f"{idx+1}. {s}" for idx, s in enumerate(strings))

    @staticmethod
    def formatear_reporte(reporte: Dict[str, Any]) -> str:
        """Formatea un diccionario de reporte genérico para visualizar en consola.

        Se espera un diccionario con claves como `titulo`, `fecha_generacion`, `lineas` (lista)
        y otros campos opcionales. Esta función es genérica y se puede adaptar a reports
        específicos de la aplicación.
        """
        titulo = reporte.get("titulo", "REPORTE")
        fecha = Formateadores.formatear_fecha(reporte.get("fecha_generacion", ""))
        output = "\n" + "=" * 60 + "\n"
        output += f"                {titulo}\n"
        output += "=" * 60 + "\n"
        if fecha:
            output += f"Fecha de Generación: {fecha}\n"
        for k, v in reporte.items():
            if k in ("titulo", "fecha_generacion", "lineas"):
                continue
            output += f"{k.replace('_', ' ').title()}: {v}\n"
        output += "\n"
        lineas = reporte.get("lineas", [])
        if lineas:
            output += "- " + "\n- ".join(str(l) for l in lineas) + "\n"
        else:
            output += "No hay elementos en el reporte.\n"
        output += "=" * 60 + "\n"
        return output


__all__ = ["Formateadores"]
