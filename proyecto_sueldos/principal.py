import random
from datos import trabajadores, sueldos

def asignar_sueldos():
    sueldos.clear()
    for trabajador in trabajadores:
        sueldos[trabajador] = random.randint(300000, 2500000)
    print("Sueldos asignados correctamente.")

def clasificar_sueldos():
    if not sueldos:
        print("Debe asignar sueldos primero.")
        return

    print("--- Clasificación de sueldos ---")
    for trabajador, sueldo in sueldos.items():
        if sueldo < 800000:
            categoria = "Bajo"
        elif sueldo <= 2000000:
            categoria = "Medio"
        else:
            categoria = "Alto"
        print(f"{trabajador}: ${sueldo:,} ({categoria})")

def ver_estadisticas():
    if not sueldos:
        print("Debe asignar sueldos primero.")
        return

    valores = list(sueldos.values())
    print("--- Estadísticas ---")
    print(f"Sueldo más alto: ${max(valores):,}")
    print(f"Sueldo más bajo: ${min(valores):,}")
    print(f"Promedio: ${int(sum(valores)/len(valores)):,}")

def reporte_sueldos():
    if not sueldos:
        print("Debe asignar sueldos primero.")
        return

    with open("reporte_sueldos.txt", "w", encoding="utf-8") as archivo:
        archivo.write("Reporte de Sueldos\n")
        archivo.write("------------------\n")
        for trabajador, sueldo in sueldos.items():
            archivo.write(f"{trabajador}: ${sueldo:,}\n")

    print("Reporte generado correctamente.")

def menu():
    while True:
        print("""--- Menu de sueldos ---
            1. Asignar sueldos aleatorios
            2. Clasificar sueldos
            3. Ver estadísticas
            4. Reporte de sueldos
            5. Salir """)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            asignar_sueldos()
        elif opcion == "2":
            clasificar_sueldos()
        elif opcion == "3":
            ver_estadisticas()
        elif opcion == "4":
            reporte_sueldos()
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()