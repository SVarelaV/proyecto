from paciente import Paciente
from pacientes import Pacientes

class Menu:
    def __init__(self):
        self.lista_pacientes = Pacientes()

    def mostrar_menu(self):
        while True:
            print("\nMenu:")
            print("1. Mostrar lista de pacientes")
            print("2. Agregar paciente")
            print("3. Eliminar paciente")
            print("4. Buscar paciente")
            print("5. Existe paciente")
            print("6. Salir")

            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.lista_pacientes.mostrar_pacientes()
            elif opcion == "2":
                dni = input("Inserta el DNI del paciente: ")
                nombre = input("Inserta el nombre del paciente: ")
                apellido1 = input("Inserta el primer apellido del paciente: ")
                apellido2 = input("Inserta el segundo apellido del paciente: ")
                direccion = input("Inserta la dirección del paciente: ")
                cp = input("Inserta el código postal del paciente: ")
                poblacion = input("Inserta la población del paciente: ")
                pais = input("Inserta el país del paciente: ")
                fechaNacimiento = input("Inserta la fecha de nacimiento del paciente (DD/MM/AAAA): ")
                estadoCivil = input("Inserta el estado civil del paciente: ")
                sexo = input("Inserta el sexo del paciente: ")
                email = input("Inserta el email del paciente: ")
                telefono = input("Inserta el teléfono del paciente: ")
                # Crear un nuevo Paciente y agregarlo a la lista
                nuevo_paciente = Paciente(dni, nombre, apellido1, apellido2, direccion, cp, poblacion, pais, fechaNacimiento, estadoCivil, sexo, email, telefono)
                self.lista_pacientes.agregar_paciente(nuevo_paciente)
                print("Paciente agregado correctamente.")
            elif opcion == "3":
                dni = input("Inserta el DNI del paciente a eliminar: ")
                self.lista_pacientes.eliminar_paciente(dni)
            elif opcion == "4":
                dni = input("Inserta el DNI del paciente a buscar: ")
                paciente = self.lista_pacientes.buscar_paciente(dni)
                if paciente:
                    print(f"Paciente encontrado: DNI: {paciente.dni}, Nombre: {paciente.nombre}, Apellido1: {paciente.apellido1}, Apellido2: {paciente.apellido2}")
                else:
                    print("Paciente no encontrado.")
            elif opcion == "5":
                dni = input("Inserta el DNI del paciente a buscar: ")
                existe = self.lista_pacientes.existe_paciente(dni)
                if existe:
                    print("El paciente existe en la lista.")
                else:
                    print("El paciente no existe en la lista.")
            elif opcion == "6":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, elige una opción válida.")


def main():
    menu = Menu()
    menu.mostrar_menu()

if __name__ == "__main__":
    main()