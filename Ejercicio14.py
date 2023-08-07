'''14. Escribir una función que calcule la media aritmética de una lista de números'''

import random

tamaño = int(input("Ingrese el tamaño que desea para su lista: "))
lista = []

for i in range(tamaño):
    lista.append(random.randint(0, 5))

def promedio(lista, tamaño):
    suma = 0
    for i in range(tamaño):
        suma += lista[i]
    promedio = suma / tamaño
    print(f"La media aritmética de la lista {lista} es: {promedio}")
    return

promedio(lista, tamaño)