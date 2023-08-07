'''4. Escribir un programa que determine si un número dado es par o impar.'''

numero = int(input("Ingrese el número que desea analizar: "))

if numero % 2 == 0:
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")