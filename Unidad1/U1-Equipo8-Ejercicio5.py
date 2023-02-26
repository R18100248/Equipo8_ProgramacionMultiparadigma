# #5 – Manejo de información
# Escribir una función que reciba n parámetros de llave valor e imprima la información en formato
# “{llave}”: “{Valor}”.

# Rogelio Zamarripa Treviño - 18100248

def funcionImprimirLlavesValores(n):
    llaves = {}
    i = 1

    while i <= n:
        llave = input(f"Ingrese la llave {i}: ")
        valor = int(input(f"Ingrese el valor de llave {i}: "))

        llaves[llave] = valor
        i+=1
    
    for llave, valorLlave in llaves.items():
        print(f"{llave} : {valorLlave}")

n = int(input("Ingrese la cantidad de datos que desea registar: "))
funcionImprimirLlavesValores(n)
