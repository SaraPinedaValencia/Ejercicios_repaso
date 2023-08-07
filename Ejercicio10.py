'''10. Escribir una función que calcule el factorial de un número dado.'''

numero = int(input("Ingrese el número al que desa sacarle factorial: "))

def factorial(numero):
    factorial = 1
    for i in range(1, numero+1):
        factorial = factorial * i
    print(f"El factorial del número {numero} es: {factorial}")
    return

factorial(numero)