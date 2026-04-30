
#Ejercicio 1
def mostrar_numero(numero:int):
    print(numero)

mostrar_numero(5)

#Ejercicio 2
def pedir_numero():
    numero = input("Ingrese numero: ")

    return numero

#Ejerciciio 3
def resolver_par(numero:int):
    if (numero % 2) == 0:
        par = True
    else:
        par = False

    return par

print(resolver_par(int(input("numero par?: "))))

#Ejercicio 4
def pedir_rango(desde:int, hasta:int):
    numero = int(input(f"Ingrese numero({desde}-{hasta}): "))
    while numero < desde or numero > hasta:
        numero = int(input(f"Error. Ingrese numero({desde}-{hasta}): "))

    return numero

pedir_rango(7, 17)

#Ejercicio 5
def Restar1(numero1:int, numero2:int)-> int:
    resultado = numero1 - numero2
    return resultado

def Restar2() -> int:
    valor1 = int(input("Valor 1: "))
    valor2 = int(input("Valor 2: "))

    resultado = valor1 - valor2
    return resultado

def Restar3(numero1:int, numero2:int):
    resultado = numero1 - numero2
    print(resultado)

def Restar4():
    valor1 = int(input("Valor 1: "))
    valor2 = int(input("Valor 2: "))

    resultado = valor1 - valor2
    print(resultado)

#Ejercicio 6
def realizarDescuento(numero):
    descuento = 5

    resta = (numero * descuento) / 100
    resultado = Restar1(numero, resta)

    return resultado

numero1 = pedir_rango(1,100)
descuentado = realizarDescuento(numero1)
print(descuentado)

#Ejercicio 7
def sumar(numero1:int, numero2:int):
    resultado = numero1 + numero2
    return resultado

numero1 = pedir_rango(10,100)
numero2 = pedir_rango(10,100)

operacion = input("Operacion(s,r): ")
while operacion != "s" and operacion != "r":
    operacion = input("Error. Operacion(s,r): ")

if operacion == "s":
    resultado = sumar(numero1, numero2)
else:
    resultado = Restar1(numero1, numero2)

print(resultado)







    
