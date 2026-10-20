"""Ejemplos de funciones, argumentos y alcance de variables."""

import math


def hola_Mundo():
    print("Hola Mundo")


def xx():
    print("xxx")


def perimetro(r: float) -> float:
    return 2 * math.pi * r


def es_Multiplo_De2(n: int, m: int) -> bool:
    return n % m == 0


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


def ejemploArgumento(xArgumento: int):
    print("En ejemploArgumento: ", xArgumento)
    xArgumento = xArgumento + 40


def ejemploVarGlobal():
    global xGlobal
    print("En ejemploVarGlobal: ", xGlobal)
    xGlobal = xGlobal + 30


xGlobal: int = 1


def ejemploReturn(xArgumento: int) -> int:
    print("En ejemploReturn: ", xArgumento)
    xArgumento = xArgumento + 40
    return xArgumento


if __name__ == "__main__":
    ejemploArgumento(xGlobal)  # El argumento local no modifica xGlobal.
    print("En codigo libre: ", xGlobal)  # 1
    ejemploVarGlobal()
    print("En codigo libre: ", xGlobal)  # 31
    ejemploArgumento(xGlobal)
    print("En codigo libre: ", xGlobal)  # 31
    ejemploVarGlobal()
    print("En codigo libre: ", xGlobal)  # 61

    xGlobal = 1
    xGlobal = ejemploReturn(xGlobal)
    print("En codigo libre: ", xGlobal)  # 41
    ejemploVarGlobal()
    print("En codigo libre: ", xGlobal)  # 71
    xGlobal = ejemploReturn(xGlobal)
    print("En codigo libre: ", xGlobal)  # 111
    ejemploVarGlobal()
    print("En codigo libre: ", xGlobal)  # 141
