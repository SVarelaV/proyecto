from datoclinico import DatoClinico


class DatosClinicos:
    def __init__(self):
        self.datosclinicos = []

    def agregar_datoclinico(self, datoclinico):
        self.datosclinicos.append(datoclinico)
        
    def mostrar_datoclinico(self):
      return self.datosclinicos

    def buscar_datoclinico(self, dni):
        for datoclinico in self.datosclinicos:
            if datoclinico.dni == dni:
                return datoclinico
        return None

    def existe_datoclinico(self, dni):
        for datoclinico in self.datosclinicos:
            if datoclinico.dni == dni:
                return True
        return False