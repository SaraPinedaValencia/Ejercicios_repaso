'''7. Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada'''

import random

tamaño = int(input("Ingrese el tamaño que desea para su lista: "))
lista = []

for i in range(tamaño):
    lista.append(random.randint(0, 100))

def mayor(lista, tamaño):
    mayor = lista[0]
    for i in range(tamaño):
        if lista[i] > mayor:
            mayor = lista[i]
    print(f"El mayor de la lista {lista} es: {mayor}")
    return

def menor(lista, tamaño):
    menor = lista[0]
    for i in range(tamaño):
        if lista[i] < menor:
            menor = lista[i]
    print(f"El menor de la lista {lista} es: {menor}")
    return

mayor(lista, tamaño)
menor(lista, tamaño)