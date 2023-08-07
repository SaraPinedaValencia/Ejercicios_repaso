'''5. Crear una función que convierta grados Fahrenheit a grados Celsius'''

def conversor(grados):
    celsius = (grados - 32)/1.8
    print(f"{grados} grados Fahrenheit son {celsius} grados Celsius")
    return

fahrenheit = float(input("Ingrese los grados Farenheit a convertir: "))
conversor(fahrenheit)