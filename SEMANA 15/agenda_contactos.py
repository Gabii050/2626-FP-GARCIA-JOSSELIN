# Agenda de Contactos - Tarea Semana 15
# Autor: Josselin García

contactos = {}

def agregar_contacto():
    nombre = input("Por favor ingrese el nombre del contacto: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return
    telefono = input("Número telefónico: ").strip()

    contactos[nombre] = telefono
    print(f"Contacto '{nombre}' guardado correctamente.")

def mostrar_contactos():

    if not contactos:
        print("No hay contactos guardados.")
        return
    print("\n--- LISTA DE CONTACTOS GUARDADOS ---")
    for nombre, telefono in contactos.items():
        print(f"Nombre: {nombre} | Teléfono: {telefono}")
    print(f"Total: {len(contactos)} contactos\n")

def buscar_contacto():

    nombre = input("Nombre a buscar: ").strip()
    if nombre in contactos:
        print(f"Encontrado -> {nombre}: {contactos[nombre]}")
    else:
        print("Contacto no encontrado.")

def eliminar_contacto():

    nombre = input("Nombre a eliminar: ").strip()
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto '{nombre}' eliminado.")
    else:
        print("No existe ese contacto.")

# Menú principal
while True:
    print("\n1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
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
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida.")