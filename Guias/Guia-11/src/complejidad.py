"""Experimentos acotados: no confundir tiempo medido con orden de crecimiento."""

import argparse
import csv
from pathlib import Path
from queue import Queue, LifoQueue
import random
import time


def sumatoria_1(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total


def sumatoria_2(n):
    total = n * (n + 1) // 2
    return total


def sumatoria_3(n):
    if n == 0:
        return 0
    return n + sumatoria_3(n - 1)


def cuentas_sumatorias(n):
    """Modelo de operaciones del README; no se ejecuta la recursión."""
    if n < 0:
        raise ValueError("n debe ser no negativo")
    return 5 * n + 4, 5, 4 * n + 2


def maximo_lista(xs):
    mayor = xs[0]
    for x in xs[1:]:
        if x > mayor:
            mayor = x
    return mayor


def maximo_cola(q):
    """También sirve con LifoQueue y preserva su orden."""
    extraidos = []
    while not q.empty():
        extraidos.append(q.get())
    if not extraidos:
        raise ValueError("La secuencia debe ser no vacía")
    mayor = maximo_lista(extraidos)
    restaurar = extraidos
    if isinstance(q, LifoQueue):
        restaurar = extraidos[::-1]
    for x in restaurar:
        q.put(x)
    return mayor


def maxima_diferencia_cuadratica(xs):
    mayor = 0
    for x in xs:
        for y in xs:
            diferencia = abs(x - y)
            if diferencia > mayor:
                mayor = diferencia
    return mayor


def maxima_diferencia_lineal(xs):
    menor = mayor = xs[0]
    for x in xs[1:]:
        if x < menor:
            menor = x
        if x > mayor:
            mayor = x
    return mayor - menor


def suma_de_productos(xs):
    total = 0
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            total += xs[i] * xs[j]
    return total


def elementos_en_pos_pares(xs):
    res = []
    for i in range(0, len(xs), 2):
        res.append(xs[i])
    return res


def sumar_cantidad_veces_indice(xs):
    for i in range(len(xs)):
        xs[i] *= i


def diagonal_principal(m):
    res = []
    for i in range(len(m)):
        res.append(m[i][i])
    return res


def convertir_en_matriz_identidad(m):
    for i in range(len(m)):
        for j in range(len(m)):
            m[i][j] = int(i == j)


def sumar_elementos_matriz(m):
    total = 0
    for fila in m:
        for x in fila:
            total += x
    return total


def medir(funcion, argumento, repeticiones=5):
    inicio = time.perf_counter_ns()
    for _ in range(repeticiones):
        funcion(argumento)
    return (time.perf_counter_ns() - inicio) / repeticiones


def experimentar(destino):
    destino.mkdir(parents=True, exist_ok=True)
    with (destino / "sumatorias.csv").open(
        "w", newline="", encoding="utf-8"
    ) as archivo:
        writer = csv.writer(archivo)
        writer.writerow(
            ["n", "metodo", "nanosegundos_por_llamada", "resultado", "estado"]
        )
        for n in (10, 100, 400, 1000, 10000, 1000000):
            for nombre, funcion in (
                ("ciclo", sumatoria_1),
                ("formula", sumatoria_2),
                ("recursion", sumatoria_3),
            ):
                if nombre == "recursion" and n > 400:
                    writer.writerow([n, nombre, "", "", "omitido_limite_pila"])
                else:
                    writer.writerow(
                        [n, nombre, medir(funcion, n), funcion(n), "medido"]
                    )
    rng = random.Random(2025)
    with (destino / "maximos.csv").open("w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(
            ["n", "maximo_posicion", "estructura", "nanosegundos_por_llamada"]
        )
        for n in (10, 1000, 10000):
            base = rng.sample(range(1, n * 10), n)
            for posicion in ("aleatoria", "principio", "final"):
                xs = base[:]
                if posicion == "principio":
                    xs.insert(0, n * 10 + 1)
                elif posicion == "final":
                    xs.append(n * 10 + 1)
                for nombre, tipo in (
                    ("lista", None),
                    ("cola", Queue),
                    ("pila", LifoQueue),
                ):
                    argumento = xs
                    funcion = maximo_lista
                    if tipo:
                        argumento = tipo()
                        for x in xs:
                            argumento.put(x)
                        funcion = maximo_cola
                    writer.writerow(
                        [len(xs), posicion, nombre, medir(funcion, argumento)]
                    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "destino", type=Path, help="Carpeta nueva o de resultados de los CSV"
    )
    experimentar(parser.parse_args().destino)
