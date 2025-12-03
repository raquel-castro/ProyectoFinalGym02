class ClasesRepo:
    def __init__(self):
        self.clases = []
        self.next_id = 1

    def agregar(self, clase):
        self.clases.append(clase)

    def buscar_por_id(self, clase_id):
        return next((c for c in self.clases if c.id == clase_id), None)

    def listar(self):
        return self.clases

    def listar_por_fecha(self, fecha):
        return [c for c in self.clases if c.fecha == fecha]
