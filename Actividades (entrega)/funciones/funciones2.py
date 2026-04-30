#1
def calcular_area_cuadrado(base:int, altura:int):
    area = base * altura
    return area

#2
def calcular_area_circulo(radio:int):
    area = radio * 360
    return area

#3
def definir_par(numero:int):
    if (numero % 2) == 0:
        mensaje = "El numero es par"
    else:
        mensaje = "El numero es impar"

    print(mensaje)

#4
def resolver_par(numero:int):
    if (numero % 2) == 0:
        par = True
    else:
        par = False

    return par

#5
def resolver_max(num1:int, num2:int, num3:int):
    max = num1
    if num2 > max:
        max = num2
    if num3 > max:
        max = num3

    return max

#6
def calcular_potencia(base, exponente):
    if exponente == 0:
        resultado = 1
    else:
        resultado = base
        for i in range(exponente - 1):
            resultado = resultado * base
    
    return resultado

#7
def definir_primo(num:int):
    if num == 1 or num == 0:
        primo = False
    else:
        divisor = 2
        while num % divisor != 0 and divisor != num:
            divisor +=1

        if divisor == num:
            primo = True
        else:
            primo = False

    return primo

#8
def mostrar_primos(hasta:int):
    primos = 0
    for i in range(2, hasta):
        if definir_primo(i) == True:
            print(i)
            primos += 1
    
    return primos

#print(f"Primos encontrados: {mostrar_primos(20)}")

#9
def mostrar_tabla(num:int, inicio = 1, fin = 10):
    for i in range(inicio, fin+1):
        print(f"{num}x{i} = {num * i}")

#10
def pedir_entero():
    retorno = input("Entero: ")
    return retorno

#11 
def pedir_flotante():
    retorno = input("Flotante: ")
    return retorno

#12            
def pedir_cadena():
    retorno = input("Cadena: ")
    return retorno


