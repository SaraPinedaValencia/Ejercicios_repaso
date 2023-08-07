'''3. Crear un programa que genere una lista de números aleatorios y los imprima en pantalla'''

import random

tamaño = int(input("Ingrese el tamaño que desea para su lista: "))
lista = []

for i in range(tamaño):
    lista.append(random.randint(0, 100))

print(lista)
