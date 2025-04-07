from paciente import Paciente


class Pacientes:
    def __init__(self):
        self.pacientes = []

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)
        
    def mostrar_pacientes(self):
        print("Lista de Pacientes:")
        for i, paciente in enumerate(self.pacientes, 1):
            print(f"{i}. DNI: {paciente.dni}, Nombre: {paciente.nombre}, Apellido1: {paciente.apellido1}, Apellido2: {paciente.apellido2}, Direccion: {paciente.direccion}, CP: {paciente.cp}, Poblacion: {paciente.poblacion}, Pais: {paciente.pais}, Fecha Nacimiento: {paciente.fechaNacimiento}, Estado Civil: {paciente.estadoCivil}, Sexo: {paciente.sexo}, Email: {paciente.email}, Telefono: {paciente.telefono}")

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
