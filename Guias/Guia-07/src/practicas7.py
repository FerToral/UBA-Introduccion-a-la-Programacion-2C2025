"""Actividades de listas, matrices y programas interactivos de la guía 7."""

import random
from guia7 import pertenece, ordenados


def vocales_distintas(s: str) -> bool:
    vistas: list[str] = []
    for c in s:
        if c in "aeiou" and c not in vistas:
            vistas.append(c)
    return len(vistas) >= 3


def pos_secuencia_ordenada_mas_larga(s: list[int]) -> int:
    inicio = mejor_inicio = 0
    longitud = mejor_longitud = 1
    for i in range(1, len(s)):
        if s[i - 1] <= s[i]:
            longitud += 1
        else:
            inicio, longitud = i, 1
        if longitud > mejor_longitud:
            mejor_inicio, mejor_longitud = inicio, longitud
    return mejor_inicio


def cantidad_digitos_impares(numeros: list[int]) -> int:
    cantidad: int = 0
    for n in numeros:
        while n > 0:
            if (n % 10) % 2 == 1:
                cantidad += 1
            n //= 10
    return cantidad


def ceros_en_posiciones_pares(s: list[int]) -> None:
    for i in range(0, len(s), 2):
        s[i] = 0


def ceros_en_posiciones_pares2(s: list[int]) -> list[int]:
    res = s[:]
    ceros_en_posiciones_pares(res)
    return res


def sin_vocales(s: str) -> str:
    res: str = ""
    for c in s:
        if c not in "aeiou":
            res += c
    return res


def reemplaza_vocales(s: str) -> str:
    res: str = ""
    for c in s:
        if c in "aeiou":
            res += " "
        else:
            res += c
    return res


def da_vuelta_str(s: str) -> str:
    res: str = ""
    for i in range(len(s) - 1, -1, -1):
        res += s[i]
    return res


def eliminar_repetidos(s: str) -> str:
    res: str = ""
    for c in s:
        if c not in res:
            res += c
    return res


def resultadoMateria(notas: list[int]) -> int:
    total: int = 0
    for nota in notas:
        if nota < 4:
            return 3
        total += nota
    if total >= 7 * len(notas):
        return 1
    return 2


def saldoActual(movimientos: list[tuple[str, int]]) -> int:
    saldo: int = 0
    for tipo, monto in movimientos:
        if tipo == "I":
            saldo += monto
        else:
            saldo -= monto
    return saldo


def pertenece_a_cada_uno_version1(s: list[list[int]], e: int, res: list[bool]) -> None:
    # Un resultado de tamaño exacto también satisface el contrato más débil ≥.
    pertenece_a_cada_uno_version2(s, e, res)


def pertenece_a_cada_uno_version2(s: list[list[int]], e: int, res: list[bool]) -> None:
    res.clear()
    for fila in s:
        res.append(pertenece(fila, e))


def pertenece_a_cada_uno_version3(s: list[list[int]], e: int) -> list[bool]:
    res: list[bool] = []
    pertenece_a_cada_uno_version2(s, e, res)
    return res


def es_matriz(s: list[list[int]]) -> bool:
    if len(s) == 0 or len(s[0]) == 0:
        return False
    for fila in s:
        if len(fila) != len(s[0]):
            return False
    return True


def columna(m: list[list[int]], c: int) -> list[int]:
    res: list[int] = []
    for fila in m:
        res.append(fila[c])
    return res


def columnas_ordenadas(m: list[list[int]]) -> list[bool]:
    res: list[bool] = []
    for c in range(len(m[0])):
        res.append(ordenados(columna(m, c)))
    return res


def transponer(m: list[list[int]]) -> list[list[int]]:
    res: list[list[int]] = []
    for c in range(len(m[0])):
        res.append(columna(m, c))
    return res


def quien_gana_tateti(m: list[list[str]]) -> int:
    lineas = m[:] + [[m[i][j] for i in range(3)] for j in range(3)]
    lineas.append([m[i][i] for i in range(3)])
    lineas.append([m[i][2 - i] for i in range(3)])
    for fila in lineas:
        if fila[0] == fila[1] == fila[2] == "O":
            return 0
        if fila[0] == fila[1] == fila[2] == "X":
            return 1
    return 2


def multiplicar_matrices(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    res: list[list[int]] = []
    for fila in a:
        nueva: list[int] = []
        for j in range(len(b[0])):
            valor: int = 0
            for k in range(len(b)):
                valor += fila[k] * b[k][j]
            nueva.append(valor)
        res.append(nueva)
    return res


def exponenciacion_matriz(d: int, p: int, semilla: int = 2025) -> list[list[int]]:
    rng = random.Random(semilla)
    base = [[rng.randrange(10) for _ in range(d)] for _ in range(d)]
    res = [fila[:] for fila in base]
    for _ in range(1, p):
        res = multiplicar_matrices(res, base)
    return res


def nombres_estudiantes() -> list[str]:
    res: list[str] = []
    nombre: str = input("Nombre (listo o vacío para terminar): ")
    while nombre != "" and nombre != "listo":
        res.append(nombre)
        nombre = input("Nombre (listo o vacío para terminar): ")
    return res


def monedero() -> list[tuple[str, int]]:
    historial: list[tuple[str, int]] = []
    opcion: str = input("C cargar, D descontar, X finalizar: ").upper()
    while opcion != "X":
        if opcion == "C" or opcion == "D":
            monto: int = int(input("Monto positivo: "))
            if monto > 0:
                historial.append((opcion, monto))
        opcion = input("C cargar, D descontar, X finalizar: ").upper()
    return historial


def siete_y_medio(rng=None) -> list[int]:
    if rng is None:
        rng = random
    historial: list[int] = []
    total: float = 0.0
    seguir: str = "S"
    while seguir == "S":
        carta: int = rng.choice([1, 2, 3, 4, 5, 6, 7, 10, 11, 12])
        historial.append(carta)
        if carta >= 10:
            total += 0.5
        else:
            total += carta
        print("Carta:", carta, "Total:", total)
        if total > 7.5:
            print("Perdiste")
            break
        seguir = input("¿Otra carta? S/N: ").upper()
    return historial


def fortaleza_contrasena(texto: str) -> str:
    if len(texto) < 5:
        return "ROJA"
    minuscula = mayuscula = numero = False
    for c in texto:
        minuscula = minuscula or "a" <= c <= "z"
        mayuscula = mayuscula or "A" <= c <= "Z"
        numero = numero or "0" <= c <= "9"
    if len(texto) > 8 and minuscula and mayuscula and numero:
        return "VERDE"
    return "AMARILLA"
