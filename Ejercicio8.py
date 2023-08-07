'''8. Crear una función que invierta el orden de los elementos en una lista dada'''

import random

tamaño = int(input("Ingrese el tamaño que desea para su lista: "))
lista = []

for i in range(tamaño):
    lista.append(random.randint(0, 100))

def invertir(lista):
    lista_inversa = []
    for i in lista:
        lista_inversa.insert(0, i)
    print(f"La lista invertida de {lista} es: {lista_inversa}")
    return

invertir(lista)