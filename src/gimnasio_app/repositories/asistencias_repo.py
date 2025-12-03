class AsistenciasRepo:
    def __init__(self):
        self.asistencias = []

    def agregar(self, asistencia):
        self.asistencias.append(asistencia)

    def historial_por_socio(self, socio):
        return [a for a in self.asistencias if a.socio.dni == socio.dni]

    def asistencias_del_dia(self, fecha):
        return [a for a in self.asistencias if a.fecha == fecha]
