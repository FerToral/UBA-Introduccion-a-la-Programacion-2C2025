"""Contratos de apoyo y ejemplos propios de especificación; no datos personales."""

from collections import Counter
import math

LINEAS = {28, 33, 34, 37, 45, 107, 160, 166}


def ordenamiento_valido(s, resultado):
    return Counter(s) == Counter(resultado) and all(
        a <= b for a, b in zip(resultado, resultado[1:])
    )


def duplicados_posicionales(s, resultado):
    return len(s) == len(resultado) and all(b == 2 * a for a, b in zip(s, resultado))


def raices_admitidas(version, s, resultado, exigir_sin_repetidos=True):
    if version not in range(1, 7):
        raise ValueError("Versión1..6")
    if exigir_sin_repetidos and version <= 4 and len(set(s)) != len(s):
        return False
    positivos = [x for x in s if x > 0]
    if any(not math.isfinite(x) for x in resultado):
        return False
    if (version == 4 and not positivos) or (version != 4 and len(positivos) != len(s)):
        return False
    raices = [math.sqrt(x) for x in positivos]
    cerca = lambda a, b: math.isclose(a, b, rel_tol=1e-12, abs_tol=1e-12)
    if version in (1, 5, 6):
        posiciones = all(cerca(a, b) for a, b in zip(raices, resultado))
        return posiciones and (
            len(s) == len(resultado)
            if version == 1
            else len(resultado) <= len(s)
            if version == 6
            else True
        )
    pertenecen = all(any(cerca(y, x) for x in raices) for y in resultado)
    cubren = all(any(cerca(x, y) for y in resultado) for x in raices)
    if version == 2:
        return len(resultado) == len(s) and pertenecen and cubren
    if version == 3:
        return len(resultado) == len(s) and pertenecen
    return pertenecen and cubren


def cantidad_colectivos(s, linea):
    if linea not in LINEAS or any(x not in LINEAS for x in s):
        raise ValueError("Línea ajena al dominio")
    return s.count(linea)


def mejor_frecuencia(s, a, b):
    return a if cantidad_colectivos(s, a) >= cantidad_colectivos(s, b) else b


def validar_registro(registro):
    alumnos = set()
    for alumno, cursada in registro:
        if not isinstance(alumno, str) or alumno in alumnos:
            raise ValueError("Alumno inválido o duplicado")
        alumnos.add(alumno)
        aprobadas = set()
        for materia, nota in cursada:
            if (
                not isinstance(materia, str)
                or isinstance(nota, bool)
                or not isinstance(nota, (int, float))
                or not math.isfinite(nota)
                or not 0 <= nota <= 10
                or materia in aprobadas
            ):
                raise ValueError("Cursada inválida")
            if nota >= 4:
                aprobadas.add(materia)


def _promedio(cursada):
    if not cursada:
        raise ValueError("Promedio requiere al menos un intento")
    return sum(nota for _, nota in cursada) / len(cursada)


def promedio_de_alumno(alumno, registro):
    validar_registro(registro)
    for nombre, cursada in registro:
        if nombre == alumno:
            return _promedio(cursada)
    raise ValueError("Alumno no registrado")


def materias_con_mejor_nota(cursada):
    validar_registro([("Alumno ficticio", cursada)])
    if not cursada:
        raise ValueError("Cursada vacía")
    maxima = max(nota for _, nota in cursada)
    return list(dict.fromkeys(materia for materia, nota in cursada if nota == maxima))


def aprobaron(materia, registro, alfabetico=False):
    validar_registro(registro)
    alumnos = [
        alumno
        for alumno, cursada in registro
        if any(m == materia and nota >= 4 for m, nota in cursada)
    ]
    return sorted(alumnos) if alfabetico else alumnos


def promedios(registro):
    validar_registro(registro)
    return [_promedio(cursada) for _, cursada in registro]


def sumar_abs_mayor_a5(s):
    return sum(x for x in s if abs(x) > 5)
