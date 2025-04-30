from paciente import Paciente

class Pacientes:
    def __init__(self):
        self.pacientes = []

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)
        
    def mostrar_pacientes(self):
        return self.pacientes

    def buscar_paciente(self, dni):
        for paciente in self.pacientes:
            if paciente.dni == dni:
                return paciente
        return None
    
    def existe_paciente(self, dni):
        for paciente in self.pacientes:
            if paciente.dni == dni:
                return True
        return False
