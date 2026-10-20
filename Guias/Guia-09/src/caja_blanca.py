"""Programas de estudio y mutantes deliberados para comparar cobertura y corrección."""


def maximo(x, y):
    resultado = 0
    if x < y:
        resultado = y
    else:
        resultado = x
    return resultado


def minimo_defectuoso(x, y):
    if x < y:
        return x
    return x  # Mutante: debía devolver y.


def minimo(x, y):
    if x < y:
        return x
    return y


def sumar(x, y):
    resultado = 0
    resultado += x
    resultado += y
    return resultado


def restar_defectuoso(x, y):
    return x + y


def restar(x, y):
    return x - y


def signo(x):
    resultado = 0
    if x < 0:
        resultado = -1
    elif x > 0:
        resultado = 1
    return resultado


def absoluto_defectuoso(x):
    resultado = 0
    if x < 0:
        resultado = -x
    return resultado


def absoluto(x):
    if x < 0:
        return -x
    return x


def mult10(x):
    resultado = 0
    contador = 0
    while contador < 10:
        resultado += x
        contador += 1
    return resultado


def sumar_por_unidades(x, y):
    if y < 0:
        unidad, cantidad = -1, -y
    else:
        unidad, cantidad = 1, y
    resultado = x
    for _ in range(cantidad):
        resultado += unidad
    return resultado


def mcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


def triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 4
    if not (a + b > c and a + c > b and b + c > a):
        return 4
    if a == b and b == c:
        return 1
    if a == b or b == c or a == c:
        return 2
    return 3


def mult_by_abs(x, y):
    cantidad = absoluto(y)
    if cantidad < 0:
        return -1  # Inalcanzable por el contrato de absoluto.
    resultado = 0
    for _ in range(cantidad):
        resultado += x
    return resultado


def vaciar_secuencia(s):
    for i in range(len(s)):
        s[i] = 0


def existe_elemento(s, e):
    for i in range(len(s)):
        if s[i] == e:
            return True
    return False
