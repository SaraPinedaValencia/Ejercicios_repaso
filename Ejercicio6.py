'''6. Crear un programa que calcule la suma de los números de una lista dada'''

import random

tamaño = int(input("Ingrese el tamaño que desea para su lista: "))
lista = []

for i in range(tamaño):
    lista.append(random.randint(0, 100))

def suma(lista, tamaño):
    suma = 0
    for i in range(tamaño):
        suma += lista[i]
    print(f"La suma de los elementos de la lista {lista} es: {suma}")
    return

print()
suma(lista, tamaño)

