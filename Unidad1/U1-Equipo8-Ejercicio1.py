# #1 – Funciones con n parámetros
# Escribir un programa que contenga una función que reciba n parámetros de tipo numérico y calcule
# el producto total.

# Rogelio Zamarripa Treviño - 18100248

def funcionProductoTotal(n):
    productoTotal = 1
    i = 1

    while i <= n:
        numero = int(input(f"Ingrese el número {i}: "))
        productoTotal = productoTotal * numero
        i += 1
    
    print(f"El producto total de los números ingresados es: {productoTotal}")

n = int(input("Teclee la cantidad de números a ingresar para calcular el producto total: "))
funcionProductoTotal(n)

