# #4 – Entrada de datos y estructuración
# Revisar su retícula para escribir un programa que cree un diccionario vacío para que el usuario
# capture las materias y créditos de su semestre preferido (inferior a 8vo) al final imprimir en el
# formato “{asignatura}” tiene “{créditos}” créditos. Y la suma de todos los créditos del semestre.

# Rogelio Zamarripa Treviño - 18100248

asignaturas = {}
continuar = True
sumaCreditosSemestre = 0

semestre = float(input('Ingrese el semestre del que desea capturar sus respectivas materias: '))
if semestre < 8:
    while continuar:
        nombreMateria = input('Ingrese el nombre de una materia: ')
        creditosMateria = float(input('Ingrese su cantidad de créditos correspondiente: '))
        asignaturas[nombreMateria] = creditosMateria
        sumaCreditosSemestre = sumaCreditosSemestre + creditosMateria
        continuar = input('¿Desea capturar otra materia (Si/No)? ') == "Si"
    
    for asignatura, creditos in asignaturas.items():
        print(asignatura, " tiene " ,creditos, " créditos")
    print('Suma de todos los créditos del semestre: ' , sumaCreditosSemestre)

else:
    print("ERROR DE CAPTURA: El semestre que ud. ingresó (", semestre,") NO es inferior a 8vo (octavo).")
