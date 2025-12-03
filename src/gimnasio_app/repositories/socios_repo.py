class SociosRepo:
    def __init__(self):
        self.socios = []

    def agregar(self, socio):
        self.socios.append(socio)

    def buscar_por_dni(self, dni):
        return next((s for s in self.socios if s.dni == dni), None)

    def listar(self):
        return self.socios

    def listar_activos(self):
        return [s for s in self.socios if s.estado_activo]

    def listar_inactivos(self):
        return [s for s in self.socios if not s.estado_activo]
