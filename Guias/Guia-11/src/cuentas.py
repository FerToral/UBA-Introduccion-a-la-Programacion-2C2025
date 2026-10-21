"""Conteos del pseudocódigo de la guía bajo el modelo de CONTEOS.md.

No miden segundos ni cuentan las instrucciones de estas funciones auxiliares.
"""

from collections import Counter


def productos(n):
    if n < 0:
        raise ValueError("n debe ser no negativo")
    mitad = (n + 1) // 2
    log = 0 if n <= 1 else (n - 1).bit_length()
    return (
        3,
        5 * n + 4,
        5 * mitad + 4,
        6 * n * n + 5 * n + 4,
        7 * n**3 + 5 * n * n + 5 * n + 4,
        5 * log + 4,
        (10 * n + 9) * 2**n + 5,
    )


def comparaciones(xs):
    n = len(xs)
    if not n:
        raise ValueError("máxima diferencia requiere lista no vacía")
    iguales = sum(f * f for f in Counter(xs).values())
    no_positivos = (n * n + iguales) // 2
    pares = n * (n - 1) // 2
    k = (n + 1) // 2
    return {
        "maxima_diferencia": (
            11 * n * n + 5 * n + 4 + no_positivos,
            14 * n - 6,
            11 * n - 5,
        ),
        "suma_de_productos": (7 * n * n + 2 * n + 5, 6 * pares + 6 * n + 4),
        "posiciones_pares": (5 * n + k + 4, 4 * k + 4),
        "multiplicar_por_indice": (5 * pares + 7 * n + 2, 5 * n + 2),
        "diagonal": (4 * n * n + 6 * n + 5, 4 * n + 5),
        "identidad": (5 * n * n + 5 * n + 3, 4 * n * n + 6 * n + 3),
    }


def suma_matriz(filas, columnas):
    if filas < 0 or columnas < 0:
        raise ValueError("dimensiones no negativas")
    r, c = filas, columnas
    return 5 * r * c + 13 * r + 8, 5 * r * c + 9 * r + 4, 5 * r * c + 5 * r + 4


def sumar_pares(xs):
    return 5 * len(xs) + 2 * sum(x % 2 == 0 for x in xs) + 4


def hasta_umbral(xs, umbral):
    k = 0
    while k < len(xs) and xs[k] < umbral:
        k += 1
    return 6 * k + 4 + int(k < len(xs))


def minimos(xs):
    if not xs:
        raise ValueError("secuencia no vacía")
    minimo, cambios = xs[0], 0
    for x in xs[1:]:
        if x < minimo:
            minimo, cambios = x, cambios + 1
    apariciones = xs.count(minimo)
    return 8 * len(xs) + 3 + cambios + 2 * apariciones


def colapsar(texto):
    if not texto:
        raise ValueError("texto no vacío")
    cambios = sum(a != b for a, b in zip(texto, texto[1:]))
    return 5 * len(texto) - 1 + 2 * cambios


def filas_negativas(m):
    if not m or not m[0] or any(len(f) != len(m[0]) for f in m):
        raise ValueError("matriz rectangular no vacía")
    if any(not (all(x > 0 for x in fila) or all(x < 0 for x in fila)) for fila in m):
        raise ValueError("cada fila debe tener signo uniforme estricto")
    negativas = sum(fila[0] < 0 for fila in m)
    elementos = negativas * len(m[0])
    return 4 * len(m) + 5 * elementos + 2 * negativas + 4
