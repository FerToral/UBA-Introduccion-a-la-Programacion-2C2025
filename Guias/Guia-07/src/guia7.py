"""Ejercicios de listas, cadenas y matrices de la Guía 7."""


def pertenece(s: list[int], e: int) -> bool:

    for x in s:
        if x == e:
            return True

    return False


def pertenecev2(s: list[int], e: int) -> bool:

    for i in range(len(s)):
        if s[i] == e:
            return True

    return False


def pertenecev3(s: list[int], e: int) -> bool:
    i: int = len(s) - 1
    while i >= 0 and s[i] != e:
        i -= 1

    return i >= 0


def divide_a_todos(s: list[int], e: int) -> bool:
    # Precondición de la guía: e != 0. En vacío, el universal es verdadero.
    for x in s:
        if x % e != 0:
            return False
    return True


def suma_total(s: list[int]) -> int:
    suma: int = 0
    for x in s:
        suma += x

    return suma


def maximo(s: list[int]) -> int:
    mayor: int = s[0]
    for x in s:
        if x >= mayor:
            mayor = x
    return mayor


def minimo(s: list[int]) -> int:
    minimo: int = s[0]
    for x in s:
        if x <= minimo:
            minimo = x
    return minimo


def ordenados(s: list[int]) -> bool:
    for i in range(len(s) - 1):
        if s[i] >= s[i + 1]:
            return False
    return True


def pos_maximo(s: list[int]) -> int:
    if len(s) == 0:
        return -1
    pos_max: int = 0
    for i in range(len(s)):
        if s[i] > s[pos_max]:
            pos_max = i
    return pos_max


def pos_minimo(s: list[int]) -> int:
    if len(s) == 0:
        return -1
    pos_max: int = 0
    for i in range(len(s)):
        if s[i] <= s[pos_max]:
            pos_max = i
    return pos_max


def long_mayorAsiete(s: list[str]) -> bool:
    for palabra in s:
        if len(palabra) > 7:
            return True
    return False


def es_palindroma(s: str) -> bool:
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True


def iguales_consecutivos(s: list[int]) -> bool:
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] and s[i + 1] == s[i + 2]:
            return True
    return False


def lista_ordenada(s: list[int]) -> bool:
    # Compatibilidad con el nombre auxiliar de los ejercicios históricos.
    return ordenados(s)


def filas_ordenadas(s: list[list[int]]) -> list[bool]:
    list_bool: list[bool] = []
    for i in range(len(s)):
        list_bool.append(lista_ordenada(s[i]))

    return list_bool


def columnas_ordenas(s: list[list[int]]) -> list[bool]:
    list_bool: list[bool] = []
    for j in range(len(s[0])):
        bandera_bool: bool = True
        for i in range(len(s) - 1):
            if s[i][j] >= s[i + 1][j]:
                bandera_bool = False
                break

        list_bool.append(bandera_bool)

    return list_bool


def columnas_ordenasv2(s: list[list[int]]) -> list[bool]:
    list_bool: list[bool] = []
    list_n: list[int] = []

    for j in range(len(s[0])):
        for i in range(len(s)):
            list_n.append(s[i][j])

        list_bool.append(lista_ordenada(list_n))
        list_n.clear()

    return list_bool


if __name__ == "__main__":
    lista: list[list[int]] = [[1, 2, 3], [2, 4, 6], [4, 6, 8]]
    print(filas_ordenadas(lista))
    print(columnas_ordenas(lista))
