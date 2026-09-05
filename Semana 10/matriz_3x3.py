"""
UNIVERSIDAD ESTATAL AMAZONICA
Estudiante: Josselin Garcia
Tarea: Matriz 3x3 y creacion de cuenta en GitHub
Arreglos Multidimensionales
"""

# Parte 1: Programa con matriz 3x3
# Declarar matriz de 3x3 con numeros enteros
matriz = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
]

print("Matriz 3x3:")
# Recorrer la matriz utilizando ciclos anidados
for i in range(3): # recorre filas
    for j in range(3): # recorre columnas
        # Imprime todos los valores en pantalla
        print(f"{matriz[i][j]}", end=" ")
    print() # salto de linea para cada fila

print("\nRecorrido completo finalizado.")