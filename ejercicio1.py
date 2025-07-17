import os

alumnos = []

def agregar_alumno():
    global alumnos
    nombre = input("Ingrese el nombre del alumno: ")
    alumnos.append([nombre, [], []])  # [nombre, [nota1], [nota2]]

def registrar_notas():
    global alumnos
    if not alumnos:
        print("No hay alumnos registrados.")
        os.system("pause")
        return

    print("Alumnos registrados:")
    for i, alumno in enumerate(alumnos):
        print(f"{i + 1}. {alumno[0]}")

    try:
        index = int(input("Seleccione el número del alumno para registrar notas: ")) - 1
        if index < 0 or index >= len(alumnos):
            print("Índice fuera de rango.")
            os.system("pause")
            return

        nota1 = float(input("Ingrese la primera nota: "))
        nota2 = float(input("Ingrese la segunda nota: "))
        alumnos[index][1] = nota1
        alumnos[index][2] = nota2
        print("Notas registradas correctamente.")
    except ValueError:
        print("Entrada inválida. Intente nuevamente.")
    
    os.system("pause")

def consultar_nota_final():
    global alumnos
    if not alumnos:
        print("No hay alumnos registrados.")
        os.system("pause")
        return

    print("Listado de alumnos:")
    for i, alumno in enumerate(alumnos):
        print(f"{i + 1}. {alumno[0]}")

    try:
        index = int(input("Seleccione el número del alumno: ")) - 1
        if index < 0 or index >= len(alumnos):
            print("Índice fuera de rango.")
            os.system("pause")
            return

        nota1 = alumnos[index][1]
        nota2 = alumnos[index][2]
        if nota1 == [] or nota2 == []:
            print("No se han registrado notas para este alumno.")
        else:
            final = (nota1 + nota2) / 2
            print(f"La nota final de {alumnos[index][0]} es: {final}")
    except ValueError:
        print("Entrada inválida.")
    
    os.system("pause")

def main_menu() -> int:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Menú de gestión de alumnos")
    print("1. Agregar alumno")
    print("2. Registrar notas")
    print("3. Consultar nota final")
    print("4. Salir")
    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion < 1 or opcion > 4:
            print("Opción no válida. Intente de nuevo.")
            return main_menu()
        return opcion
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        return main_menu()

if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Bienvenido al sistema de gestión de alumnos")
        opcion = main_menu()

        match opcion:
            case 1:
                agregar_alumno()
            case 2:
                registrar_notas()
            case 3:
                consultar_nota_final()
            case 4:
                os.system('pause')
                break
            case _:
                print("Opción no válida. Intente de nuevo.")
