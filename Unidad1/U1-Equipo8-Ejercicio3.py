# #3 – Entrada de datos y manipulación
# Escribir un programa que permita al usuario capturar su nombre completo e imprima su nombre de
# manera inversa letra por letra.

# Rogelio Zamarripa Treviño - 18100248

nombre_completo = input('Ingrese su nombre completo: ')

for i in range(len(nombre_completo) - 1, -1, -1):
    print(nombre_completo[i])