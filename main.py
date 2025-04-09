import json
import os
from Contacto import Contacto  # Importamos la clase Contacto desde el otro archivo que creamos

ARCHIVO = "contactos.json"  # Nombre del archivo donde se guardarán los contactos

# Funciones para cargar/guardar
def cargar_contactos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            data = json.load(f)
            return [Contacto.from_dict(item) for item in data]  # Cargamos contactos desde el archivo JSON
    return []

def guardar_contactos():
    with open(ARCHIVO, "w") as f:
        json.dump([c.to_dict() for c in agenda], f, indent=4)  # Guardamos contactos en archivo JSON

# Funciones de operación
def agregar_contacto():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    correo = input("Correo: ")
    telefono = input("Teléfono: ")
    nuevo_contacto = Contacto(nombre, apellido, correo, telefono)  # Creamos un nuevo objeto Contacto
    agenda.append(nuevo_contacto)  # Lo agregamos a la lista de contactos
    guardar_contactos()
    print("Tú contacto fue agregado con éxito.\n")

def mostrar_contactos():
    if not agenda:
        print("No tienes contactos.")  # Mensaje si la lista está vacía
    else:
        for idx, contacto in enumerate(agenda):
            print(f"{idx + 1}. {contacto}")  # Mostramos cada contacto con su número

def buscar_contacto():
    criterio = input("Buscar por nombre o apellido: ").lower()
    encontrados = [c for c in agenda if criterio in c.nombre.lower() or criterio in c.apellido.lower()]  # Buscamos coincidencias
    if encontrados:
        for c in encontrados:
            print(c)
    else:
        print("No se encontraron contactos disponibles.")

def eliminar_contacto():
    mostrar_contactos()
    try:
        idx = int(input("Ingrese el número del contacto a eliminar: ")) - 1
        if 0 <= idx < len(agenda):
            eliminado = agenda.pop(idx)  # Quitamos el contacto de la lista
            guardar_contactos()
            print(f"El Contacto '{eliminado.nombre}' fue eliminado.")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Dato nulo.")  # Si se escribe algo no válido

def actualizar_contacto():
    mostrar_contactos()
    try:
        idx = int(input("Ingrese el número del contacto que deseas actualizar: ")) - 1
        if 0 <= idx < len(agenda):
            c = agenda[idx]
            print("Deja en blanco si no deseas cambiar el valor.")
            nombre = input(f"Nuevo nombre ({c.nombre}): ") or None
            apellido = input(f"Nuevo apellido ({c.apellido}): ") or None
            correo = input(f"Nuevo correo ({c.correo}): ") or None
            telefono = input(f"Nuevo teléfono ({c.telefono}): ") or None
            c.actualizar(nombre, apellido, correo, telefono)  # Llamamos al método para modificar los datos
            guardar_contactos()
            print("Contacto actualizado con exito.")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Dato nulo.")

# Menú principal con las opciones del sistema
def menu():
    while True:
        print("\nGestión de Contactos")
        print("1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Buscar contacto")
        print("4. Eliminar contacto")
        print("5. Actualizar contacto")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            mostrar_contactos()
        elif opcion == "3":
            buscar_contacto()
        elif opcion == "4":
            eliminar_contacto()
        elif opcion == "5":
            actualizar_contacto()
        elif opcion == "6":
            print("¡Hasta luego!")  # Salida del programa
            break
        else:
            print("Opción Nula")

# Inicia el programa cargando los datos del archivo
agenda = cargar_contactos()

if __name__ == "__main__":
    menu()
