print("Hola bienvenido a la calculadora de propinas")
total = float(input("Cual es el total de tu cuenta"))
porcentajePropina = int(input("Cual es el porcentaje que deseas dejar de propina? 10% 12% o 15% ?"))
personas = int(input("Con cuantas personas dividiras la cuenta?"))

propina = (total / personas)*(porcentajePropina*0.01)

print(f"cada persona debe pagar {propina}")