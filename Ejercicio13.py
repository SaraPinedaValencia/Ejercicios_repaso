'''13. Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y 
división.'''

num1 = int(input("Ingrese el primer número a operar: "))
num2 = int(input("Ingrese el segundo número a operar: "))

def suma(a, b):
    suma = a + b
    print(f"La suma entre los número es de {suma}")
    return

def resta(a, b):
    resta = a - b
    print(f"La resta entre los número es de {resta}")
    return

def multiplicacion(a, b):
    producto = a * b
    print(f"La multiplicación entre los número es de {producto}")
    return

def division(a, b):
    division = a / b
    print(f"La división entre los número es de {division}")
    return

suma(num1, num2)
resta(num1, num2)
multiplicacion(num1, num2)
division(num1, num2)