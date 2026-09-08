"""
UNIVERSIDAD ESTATAL AMAZONICA
Estudiante: Josselin Garcia
Tarea práctica: crear una función basada en un problema de la vida real.
"""
def calcularPrecioFinal(precio, descuento):
    valor_descuento = precio * (descuento / 100)
    precio_final = precio - valor_descuento
    return precio_final


if __name__ == "__main__":
    print("--- CALCULADORA DE DESCUENTOS ---")

    nombre = input("Hola bienvenido , ¿cómo te llamas? ")
    precio_original = float(input("Ingresa el precio original: $"))
    porcentaje_descuento = float(input("Ingresa el % de descuento: "))

    resultado = calcularPrecioFinal(precio_original, porcentaje_descuento)

    print("\n--- RESULTADO ---")
    print(f"Cliente: {nombre}")
    print(f"Precio original: ${precio_original}")
    print(f"Descuento: {porcentaje_descuento}%")
    print(f"Precio final a pagar: ${resultado}")
