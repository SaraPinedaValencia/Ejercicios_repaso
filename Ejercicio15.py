'''15. Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no'''

texto = input("Ingrese una palabra: ")
texto = texto.lower()

lista_inversa = []
for i in texto:
    lista_inversa.insert(0, i)

if lista_inversa == list(texto):
    print("El texto es palindromo")
else:
    print("El texto no es palindromo")
