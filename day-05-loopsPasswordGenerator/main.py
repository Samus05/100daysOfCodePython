import random
import string

letras = list(string.ascii_letters)
numeros = list(string.digits)
simbolos = list(string.punctuation)
# print(simbolos)
# print(len(simbolos))
# print(numeros)
# print(len(numeros))
# print(letras)
# print(len(letras))

password = ""
contador_letras = 0
contador_simbolos = 0
contador_numeros = 0
print("Bienvenido al Generador de Password")
num_letras = int(input("Cuantas letras quieres para tu password? "))
num_simbolos = int(input("Cuantos simbolos quieres para tu password? "))
num_numeros = int(input("Cuantos numeros quieres en tu password? "))

while contador_letras < num_letras:
    password += random.choice(letras)
    contador_letras += 1

while contador_simbolos < num_simbolos:
    password += random.choice(simbolos)
    contador_simbolos += 1

while contador_numeros < num_numeros:
    password += random.choice(numeros)
    contador_numeros += 1

password = ''.join(random.sample(password,  len(password)))
print(f"Tu password es: " + password)


