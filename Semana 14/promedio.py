def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio

print("=== CALCULO DE PROMEDIO DE 3 NOTAS ===")


nombre = input("Ingresa tu nombre por favor: ")

n1 = float(input("Ingresa la nota 1: ").replace(',', '.'))
n2 = float(input("Ingresa la nota 2: ").replace(',', '.'))
n3 = float(input("Ingresa la nota 3: ").replace(',', '.'))

mi_promedio = calcular_promedio(n1, n2, n3)

print(f"\nEstimado/a {nombre}, su promedio es: {mi_promedio:.2f}")

if mi_promedio >= 7:
    print(f"¡Felicidades {nombre}, aprobaste!")
else:
    print(f"{nombre}, reprobaste, necesitas mejorar")
