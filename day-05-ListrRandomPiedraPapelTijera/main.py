import random

piedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tijeras = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list = [0,1,2]
jugador = int(input("Juguemos Piedra, Papel o Tijeras: Escribe  0 para Piedra / 1 para Papel / 2 para Tijeras. "))
computadora = random.choice(list)

def imprimeJugador():
    if jugador == 0:
        print(piedra)
    elif jugador == 1:
        print(papel)
    elif jugador == 2:
        print(tijeras)

def imprimeComputadora():
    print("Compuatadora eligio: ")
    if computadora == 0:
        print(piedra)
    elif computadora == 1:
        print(papel)
    elif computadora == 2:
        print(tijeras)

if jugador == computadora:
    imprimeJugador()
    imprimeComputadora()
    print("Empate")

if jugador == 0 and computadora == 1:
    imprimeJugador()
    imprimeComputadora()
    print("Pierdes")
if jugador == 0 and computadora == 2:
    imprimeJugador()
    imprimeComputadora()
    print("Ganaste")
if jugador == 1 and computadora == 0:
    imprimeJugador()
    imprimeComputadora()
    print("Ganaste")
if jugador == 1 and computadora == 2:
    imprimeJugador()
    imprimeComputadora()
    print("Perdiste")
if jugador == 2 and computadora == 0:
    imprimeJugador()
    imprimeComputadora()
    print("Perdiste")
if jugador == 2  and computadora == 1:
    imprimeJugador()
    imprimeComputadora()
    print("Ganaste")
