"""Funciones y estructuras de control de la Guía 6."""

import math


def suma(a: int, b: int) -> int:
    return a + b


def triada_trigonometrica(a: int, b: int, c: int) -> bool:
    return a**2 + b**2 == c**2


def es_multiplo_de(n: int, m: int) -> bool:
    return n % m == 0


def doble_si_es_par(n: int) -> int:
    if n % 2 == 0:
        return 2 * n
    return n


def fahrenheit_a_celsius(t: float) -> float:
    return ((t - 32) * 5) / 9


def es_primo(n: int) -> bool:
    if n < 2:
        return False

    i: int = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True


def cantidad_primos(n: int, m: int) -> int:
    cant: int = 0
    step = 1
    if n > m:
        step = -1

    for n in range(n, m + step, step):
        if es_primo(n) == True:
            cant += 1

    return cant


def hola_Mundo():
    print("Hola Mundo")


def xx():
    print("xxx")


def perimetro(r: float) -> float:
    return 2 * math.pi * r


def es_nombre_largo(name: str) -> bool:
    return 3 <= len(name) and len(name) <= 8


def devolver_el_doble_si_es_par(n: int) -> int:
    if n % 2 == 0:
        return 2 * n
    return n


def imprimir_numeros_pares_entre_10_40():
    n: int = 10
    while n <= 40:
        print(n)
        n = n + 2


def cuenta_regresiva(n: int):
    while n >= 1:
        print(n)
        n = n - 1

    print("Despegue")


def imprimir_numeros_pares_entre_10_40_v2():
    n: int
    for n in range(10, 41, 2):
        print(n)


def cuenta_regresiva_v2(n: int):
    for n in range(n, 0, -1):
        print(n)

    print("Despegue")


"""
def ejemploArgumento(xArgumento: int):
    print("En ejemploArgumento: ", xArgumento)
    xArgumento = xArgumento + 40
def ejemploVarGlobal():
    global xGlobal
    print("En ejemploVarGlobal: ", xGlobal)
    xGlobal = xGlobal + 30

xGlobal: int = 1
ejemploArgumento(xGlobal) # -> 1
print("En codigo libre: ", xGlobal) # 1
ejemploVarGlobal() # -> 1
print("En codigo libre: ", xGlobal) # 31
ejemploArgumento(xGlobal) # 31
print("En codigo libre: ", xGlobal) # 31
ejemploVarGlobal() # 31
print("En codigo libre: ", xGlobal) # 61


def ejemploReturn(xArgumento: int) -> int:
    print("En ejemploReturn: ", xArgumento)
    xArgumento = xArgumento + 40
    return xArgumento
def ejemploVarGlobal():
    global xGlobal
    print("En ejemploVarGlobal: ", xGlobal)
    xGlobal = xGlobal + 30

xGlobal: int = 1
xGlobal = ejemploReturn(xGlobal) #  print 1 -> = 41
print("En codigo libre: ", xGlobal) # 41
ejemploVarGlobal() # 41
print("En codigo libre: ", xGlobal) # 71
xGlobal = ejemploReturn(xGlobal) # print 71 -> = 111
print("En codigo libre: ", xGlobal) # 115
ejemploVarGlobal() # 111
print("En codigo libre: ", xGlobal) # 141

"""
