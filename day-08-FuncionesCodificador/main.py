import string
import logo

continuar = "yes"
def encode():
    global mensaje_salida
    for letra in palabra:
        if letra in simbolos or letra in numeros:
            mensaje_salida += letra
        else:
            mensaje_salida += list[(list.index(letra)+desplazamiento) % 26]
    print(mensaje_salida)


def decode():
    mensaje_salida_decode = ""
    for letra in palabra:
        if letra in numeros or letra in simbolos:
            mensaje_salida_decode += letra
        else:
            if (list.index(letra) - desplazamiento) < 0:
                posicion = (list.index(letra) - desplazamiento) + 26
            else:
                posicion = list.index(letra) - desplazamiento
                mensaje_salida_decode += list[posicion]
    print(mensaje_salida_decode)

while continuar == "yes":
    print(logo.logo)
    action = input("Escribe que deseas hacer Codificar o Decodificar: ").lower()
    palabra = input("Escribe tu mensaje: ")
    desplazamiento = int(input("Desplazamiento:"))

    mensaje_salida = ""

    list = []
    for letra in string.ascii_lowercase:
        list.append(letra)
    simbolos = []
    for simbolo in string.punctuation:
        simbolos.append(simbolo)
    simbolos.append(" ")
    numeros = []
    for numero in string.digits:
        numeros.append(numero)
    if action == "codificar":
        encode()
    elif action == "decodificar":
        decode()
    continuar = input("Desea continuar yes/ no: ")

