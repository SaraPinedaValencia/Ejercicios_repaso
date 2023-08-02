'''1. Crear un programa que pida al usuario ingresar su nombre y edad y los imprima en pantalla.'''

def main():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    print(f"El nombre del usuario es {nombre} y tiene {edad} años")
    return

main()