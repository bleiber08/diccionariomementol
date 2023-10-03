#Integrantes del grupo:
# Bleiber Tejada Rivera
# Mauricio Zuluaga Aguirre


# Crear un diccionario de suculentas inicialmente vacío
suculentas = {}

# Función para agregar una suculenta al diccionario
def agregar_suculenta():
    nombre = input("Ingrese el nombre de la suculenta: ")
    descripcion = input("Ingrese una descripción de la suculenta: ")
    suculentas[nombre] = descripcion
    print(f"Suculenta '{nombre}' agregada correctamente.")

# Función para buscar una suculenta por nombre
def buscar_suculenta():
    nombre = input("Ingrese el nombre de la suculenta que desea buscar: ")
    if nombre in suculentas:
        print(f"Descripción de la suculenta '{nombre}': {suculentas[nombre]}")
    else:
        print(f"La suculenta '{nombre}' no se encontró en la lista.")

# Función para actualizar la descripción de una suculenta
def actualizar_suculenta():
    nombre = input("Ingrese el nombre de la suculenta que desea actualizar: ")
    if nombre in suculentas:
        nueva_descripcion = input("Ingrese la nueva descripción: ")
        suculentas[nombre] = nueva_descripcion
        print(f"Descripción de la suculenta '{nombre}' actualizada correctamente.")
    else:
        print(f"La suculenta '{nombre}' no se encontró en la lista.")

# Función para eliminar una suculenta
def eliminar_suculenta():
    nombre = input("Ingrese el nombre de la suculenta que desea eliminar: ")
    if nombre in suculentas:
        del suculentas[nombre]
        print(f"La suculenta '{nombre}' ha sido eliminada.")
    else:
        print(f"La suculenta '{nombre}' no se encontró en la lista.")

# Función principal para mostrar el menú
def main():
    while True:
        print("\nMenú de Suculentas:")
        print("1. Agregar Suculenta")
        print("2. Buscar Suculenta")
        print("3. Actualizar Descripción")
        print("4. Eliminar Suculenta")
        print("5. Salir")
        
        opcion = input("Digite la opción deseada: ")
        
        if opcion == '1':
            agregar_suculenta()
        elif opcion == '2':
            buscar_suculenta()
        elif opcion == '3':
            actualizar_suculenta()
        elif opcion == '4':
            eliminar_suculenta()
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida del menú.")

if __name__ == "__main__":
    main()