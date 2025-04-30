from paciente import Paciente
from pacientes import Pacientes

class Menu:
    def __init__(self):
        self.lista_pacientes = Pacientes()
        while True:
            print("---- MENU ----")
            print("1. Mostrar lista de pacientes")
            print("2. Agregar paciente")
            print("3. Buscar paciente")
            print("4. Salir")
            opcion = input("Inserta una opción: ")

            if opcion == "1":
                self.mostrar_pacientes()
            elif opcion == "2":
                self.agregar_paciente()
            elif opcion == "3":
                self.buscar_paciente()
            elif opcion == "4":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, elige una opción válida.")

    def mostrar_pacientes(self):
        """
        Muestra la lista de pacientes registrados.
        """
        pacientes = self.lista_pacientes.mostrar_pacientes()
        if pacientes:
            print("Lista de pacientes:")
            for paciente in pacientes:
                print(f"DNI: {paciente.dni}, Nombre: {paciente.nombre}, Apellido1: {paciente.apellido1}, Apellido2: {paciente.apellido2}")
        else:
            print("No hay pacientes registrados.")

    def agregar_paciente(self):
        """
        Solicita los datos de un nuevo paciente y lo agrega a la lista.
        """
        dni = input("Inserta el DNI del paciente: ")
        if not dni:
            print("Error: El DNI no puede estar vacío.")
            return

        nombre = input("Inserta el nombre del paciente: ")
        apellido1 = input("Inserta el primer apellido del paciente: ")
        apellido2 = input("Inserta el segundo apellido del paciente: ")
        direccion = input("Inserta la dirección del paciente: ")
        cp = input("Inserta el código postal del paciente: ")
        poblacion = input("Inserta la población del paciente: ")
        pais = input("Inserta el país del paciente: ")
        fechaNacimiento = input("Inserta la fecha de nacimiento del paciente (DD/MM/AAAA): ")
        estadoCivil = input("Inserta el estado civil del paciente: ")
        genero = input("Inserta el sexo del paciente: ")
        email = input("Inserta el email del paciente: ")
        telefono = input("Inserta el teléfono del paciente: ")

        # Crear un nuevo paciente y agregarlo a la lista
        nuevo_paciente = Paciente(dni, nombre, apellido1, apellido2, direccion, cp, poblacion, pais, fechaNacimiento, estadoCivil, genero, email, telefono)
        self.lista_pacientes.agregar_paciente(nuevo_paciente)
        print("Paciente agregado correctamente.")

    def buscar_paciente(self):
        """
        Busca un paciente por su DNI y muestra sus datos.
        """
        dni = input("Inserta el DNI del paciente a buscar: ")
        if not dni:
            print("Error: El DNI no puede estar vacío.")
            return

        paciente = self.lista_pacientes.buscar_paciente(dni)
        if paciente:
            print(f"Paciente encontrado: DNI: {paciente.dni}, Nombre: {paciente.nombre}, Apellido1: {paciente.apellido1}, Apellido2: {paciente.apellido2}")
        else:
            print("Paciente no encontrado.")

def main():
    menu = Menu()

if __name__ == "__main__":
    main()