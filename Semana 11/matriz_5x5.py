"""
UNIVERSIDAD ESTATAL AMAZONICA
Estudiante: Josselin Garcia
Tarea Semana 10: Matriz 5x5
Fecha: 05 de Septiembre 2026
"""

# 1. Crear matriz vacía 5x5
matriz = []
for i in range(5):
    fila = []
    for j in range(5):
        fila.append(0)
    matriz.append(fila)

print("=== INGRESO DE DATOS MATRIZ 5x5 ===")
print("Ingrese 25 valores numericos:")

# 2 y 3. Bucles anidados para pedir datos
for i in range(5):
    for j in range(5):
        # Pedir dato al usuario
        valor = int(input(f"Ingrese valor para posicion [{i}][{j}]: "))
        # 4. Guardar en la matriz
        matriz[i][j] = valor

# 5. Mostrar matriz organizada
print("\n=== MATRIZ RESULTANTE 5x5 ===")
for i in range(5):
    for j in range(5):
        # print con espacio para que quede como tabla
        print(f"{matriz[i][j]:5}", end=" ")
    print() # salto de linea por cada fila

print("\nMatriz ingresada correctamente!")