'''2. Escribir una función que calcule el área de un círculo dado su radio.'''

def area(radio):
    area = 3.14*(radio**2)
    print(f"El area del circulo con radio {radio} es: {area}")
    return

radio = float(input("Ingrese el radio de su circulo: "))
area(radio)
