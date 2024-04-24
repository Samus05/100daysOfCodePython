import art


def suma(n1, n2):
    """Funcion para sumar dos parametros"""
    return n1 + n2


def resta(n1, n2):
    """Funcion para restar dos parametros"""
    return n1 - n2


def multiplicacion(n1, n2):
    """Funcion para multiplicar dos parametros"""
    return n1 * n2


def division(n1, n2):
    """Funcion para dividir dos parametros"""
    return n1 / n2


operaciones = {"=": suma, "-": resta, "*":multiplicacion, "/": division}


def calculator():
    print(art.logo)
    n1 = float(input("Cual es el primer numero?: "))

    for symbol in operaciones:
        print(symbol)

    continua = True
    while continua:
        simbolo_operacion = input("Selecciona una operacion ")
        n2 = float(input("Cual es el siguiente numero?: "))
        resultado = round(operaciones[simbolo_operacion](n1, n2), 2)
        print(f"{n1} {simbolo_operacion} {n2} = {resultado}")

        continua = input(f"Type 'y' por continue calculating with {resultado} or type 'n' fort restart calculator: ")
        n1 = resultado
        if continua == 'n':
            continua = False
            calculator()


calculator()
print("Adios")
