'''9. Crear un programa que genere una matriz de números y la imprima en pantalla'''

import random

filas = int(input("Ingrese número de filas: "))
columnas = int(input("Ingrese número de columnas: "))
matriz = []

for i in range(filas):
    matriz.append([0]*columnas)

for i in range(filas):
    for j in range(columnas):
        matriz[i][j] = random.randint(0, 5)

for j in range(len(matriz)):
    print(matriz[j])