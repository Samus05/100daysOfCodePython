import random
from art import logo
from replit import clear


def add_carta():
    my_Hand.append(cards[random.randint(0, 12)])


def add_carta_computer():
    computer_hand.append(cards[random.randint(0, 12)])


def suma_mano():
    score = 0
    if 11 in my_Hand:
        existe = True
    elif not 11 in my_Hand:
        existe = False
    for cartas in my_Hand:
        score += cartas
    if score > 21 and existe == True:
        my_Hand[my_Hand.index(11)] = 1
        suma_mano()
    return score


def suma_Mano_computadora():
    score_Computer = 0
    if 11 in computer_hand:
        existe = True
    elif not 11 in computer_hand:
        existe = False
    for cartas in computer_hand:
        score_Computer += cartas
    if score_Computer > 21 and existe == True:
        print(computer_hand.index(11))
        computer_hand[computer_hand.index(11)] = 1
        suma_mano()
    return score_Computer


def compara(score, scoreComputadora):
    if score == scoreComputadora:
        return "Empate"
    elif score == 21:
        return "Ganaste hiciste blackjack"
    elif score > scoreComputadora and score < 21:
        return "Le ganste a la computadora"
    elif score < 21 and scoreComputadora > 21:
        return "Ganaste el rival se paso"
    elif score < scoreComputadora and scoreComputadora < 21:
        return "perdiste te gano la computadora"
    elif score > 21:
        return "Perdiste te pasaste de 21"
    else:
        return "???????"


def blackJack():
    print(logo)

    # primera mano jugador
    add_carta()
    add_carta()
    # primera mano computadora
    add_carta_computer()
    add_carta_computer()
    add_card = 'y'

    print(f"Your cards: {my_Hand}, current score: {suma_mano()}")
    print(f"Computer's first card: {computer_hand[0]}")

    while add_card == 'y' and suma_mano() < 21:
        add_card = input("Do you want another card? type 'y' to Yes or 'n' for No").lower()
        if add_card == 'y':
            add_carta()
            suma_mano()
            print(f" Your cards are {my_Hand},current score: {suma_mano()}")

    while suma_Mano_computadora() < 18:
        if suma_Mano_computadora() > suma_mano() and suma_Mano_computadora() < 22 or suma_mano() > 21:
            break
        add_carta_computer()

    print(f"Your hand is {my_Hand},current score: {suma_mano()}")
    print(f"Computer's hand is {computer_hand} and his score is {suma_Mano_computadora()}")

    print(compara(suma_mano(), suma_Mano_computadora()))


jugar = True

while jugar == True:
    if input("Do you want to play Blackjack? Type 'Y' to yes or 'N' for Not. \n").lower() == 'y':
        jugar = True
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        my_Hand = []
        computer_hand = []
        clear()
        blackJack()
    else:
        jugar = False
print("Adios")