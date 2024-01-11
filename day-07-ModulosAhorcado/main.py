import arte_ahorcado
import palabras_ahorcado
import random
print(arte_ahorcado.logo)
palabra = random.choice(palabras_ahorcado.lista_palabras)
print("PSSST.... la palabra es: " + palabra)
end_game = True
vidas = 6
display = []
for _ in range(len(palabra)):
    display += "_"

while end_game:

    print(' '.join(display))
    print(arte_ahorcado.niveles[vidas])

    # print(display)
    letra_usuario = input("Intenta adivinar una letra: ")

    if letra_usuario in display:
        print("Ya adivinaste esa letra")
        print(arte_ahorcado.niveles)

    for posicion in range(len(palabra)):
        letra = palabra[posicion]
        if letra == letra_usuario:
            display[posicion] = letra

    if letra_usuario not in palabra:
        print("Esa letra no es parte de palabra")
        vidas -= 1
        # print(arte_ahorcado.niveles[vidas])
        if vidas == 0:
            end_game = False

    if "_" not in display:
        print("Ganaste")
        end_game = False

print(' '.join(display))
print(arte_ahorcado.niveles[vidas])