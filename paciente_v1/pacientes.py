from paciente import Paciente


class Pacientes:
    def __init__(self):
        self.pacientes = []

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def eliminar_paciente(self, dni):
        for paciente in self.pacientes:
            if paciente.dni == dni:
                self.pacientes.remove(paciente)
                print(f"Paciente con DNI {dni} eliminado.")
                return
        print(f"No se encontró el paciente con DNI {dni}.")

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
    
    def mostrar_pacientes(self):
        print("Lista de Pacientes:")
        for i, paciente in enumerate(self.pacientes, 1):
            print(f"{i}. DNI: {paciente.dni}, Nombre: {paciente.nombre}, Apellido1: {paciente.apellido1}, Apellido2: {paciente.apellido2}, Direccion: {paciente.direccion}, CP: {paciente.cp}, Poblacion: {paciente.poblacion}, Pais: {paciente.pais}, Fecha Nacimiento: {paciente.fechaNacimiento}, Estado Civil: {paciente.estadoCivil}, Sexo: {paciente.sexo}, Email: {paciente.email}, Telefono: {paciente.telefono}")

