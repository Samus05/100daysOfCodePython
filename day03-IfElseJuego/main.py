print("bienvenido al juego de la isla del Tesoro. Tu mision es encontrar el tesoro")

desicion1 = input("Que camino deseas tomar derecha o izquierda?").lower()
if desicion1 == "derecha":
    print("En este camino hay un dragon :( moriste quemado")
elif desicion1 == "izquierda":
    desicion2 = input("Llegaste a un rio, quieres nadar o esperar?").lower()
    if desicion2 == "nadar":
        print("el rio estaba infestado de tiburones y te comieron")
    elif desicion2 == "esperar":
        desicion3 = input("Aparecio un anciano en su bote y te llevo hasta el otro lado del rio. en la orila hay tres puertas. Cual eliges roja, amarilla o azul?").lower()
        if desicion3 == "roja":
            print("detras de la puerta roja hay una gallina")
        elif desicion3 =="azul":
            print("detras de la puerta azul hay un pozo sin fondo")
        elif desicion3 == "amarilla":
            print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************''')