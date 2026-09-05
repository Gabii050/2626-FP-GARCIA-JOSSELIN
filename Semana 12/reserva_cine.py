# UNIVERSIDAD ESTATAL AMAZÓNICA
# Estudiante: Josselin Garcia
# Tarea Semana 12: Listas anidadas - Reserva de Cine
# Fecha: 01  de Septiembre 2026

# 1. Crear matriz 3 filas x 4 columnas con 0 = libre
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
# 2. Mostrar sala inicial
print("=== CINE - SALA 3x4 ===")
print("0 = Libre | 1 = Ocupado\n")
for fila in asientos:
    print(fila)

# 3. Pedir datos al usuario
fila = int(input("\nIngrese la fila que desea (0 a 2): "))
columna = int(input("Ingrese la columna que desea (0 a 3): "))

# 4. Validar y reservar
if 0 <= fila <= 2 and 0 <= columna <= 3:
    if asientos[fila][columna] == 0:
        asientos[fila][columna] = 1
        print(f"\nReserva exitosa en fila {fila}, columna {columna}!")
    else:
        print("\nEse asiento ya esta ocupado.")
else:
    print("\nError: Fila o columna fuera de rango.")

# 5. Mostrar sala final
print("\nEstado final de la sala:")
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()