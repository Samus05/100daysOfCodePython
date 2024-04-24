import art
import replit



from subprocess import call

print(art.logo)
subasta = True

pujas= {"Sam": 0.01}
pujas["Belen"] = 1.00

while subasta:
    nombre = input("Cual es tu Nombre? ")
    puja = float(input("Cual es tu oferta? "))
    pujas[nombre] = puja
    if input("Terminar subasta? Si / No: ").lower() == "si":
        subasta = False

cantidad = 0
for persona in pujas:
    if pujas[persona] > cantidad:
        cantidad = pujas[persona]
        ganador = persona
replit.clear()
print(f"El ganador es {ganador} con una oferta de {cantidad}")





print(pujas)
