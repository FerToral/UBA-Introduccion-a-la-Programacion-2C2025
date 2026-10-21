"""Fórmulas y tablas de la guía1. Analizador propio: no usa eval."""

from enum import Enum
from itertools import product
import re


class Valor(Enum):
    F = 0
    V = 1
    I = None


F, V, I = Valor.F, Valor.V, Valor.I
NEG = {F: V, V: F, I: I}
OPERADORES = {"∧", "∨", "→", "↔", "∧L", "∨L", "→L"}


def analizar(texto):
    patron = r"∧L|∨L|→L|[¬∧∨→↔()]|[A-Za-z][A-Za-z0-9_]*"
    tokens = re.findall(patron, texto)
    if "".join(tokens) != re.sub(r"\s+", "", texto):
        raise ValueError("Símbolo ajeno al lenguaje")
    posicion = 0

    def formula():
        nonlocal posicion
        if posicion >= len(tokens):
            raise ValueError("Fórmula incompleta")
        token = tokens[posicion]
        posicion += 1
        if token == "¬":
            return ("¬", formula())
        if token == "(":
            izquierda = formula()
            if posicion >= len(tokens) or tokens[posicion] not in OPERADORES:
                raise ValueError("Se requiere un conector entre paréntesis")
            op = tokens[posicion]
            posicion += 1
            partes = [izquierda, formula()]
            if op in {"∧", "∨", "∧L", "∨L"}:
                while posicion < len(tokens) and tokens[posicion] == op:
                    posicion += 1
                    partes.append(formula())
            if posicion >= len(tokens) or tokens[posicion] != ")":
                raise ValueError("Agrupación incompleta o mezcla de conectores")
            posicion += 1
            return (op, *partes)
        if token in OPERADORES or token == ")":
            raise ValueError("Se esperaba una fórmula")
        if token in {"True", "False"}:
            return ("const", V if token == "True" else F)
        return ("var", token)

    resultado = formula()
    if posicion != len(tokens):
        raise ValueError("Símbolos sin agrupar")
    return resultado


def evaluar(arbol, valores):
    op, *args = arbol
    if op == "const":
        return args[0]
    if op == "var":
        valor = valores[args[0]]
        if not isinstance(valor, Valor):
            raise TypeError("Usar V,F,I, no bool implícito")
        return valor
    a = evaluar(args[0], valores)
    if op == "¬":
        return NEG[a]
    for otra in args[1:]:
        if op.endswith("L"):
            if a is I:
                return I
            if op == "∧L" and a is F:
                return F
            if op == "∨L" and a is V:
                return V
            if op == "→L" and a is F:
                return V
        b = evaluar(otra, valores)
        if a is I or b is I:
            a = I
        elif op in {"∧", "∧L"}:
            a = V if a is V and b is V else F
        elif op in {"∨", "∨L"}:
            a = V if a is V or b is V else F
        elif op in {"→", "→L"}:
            a = F if a is V and b is F else V
        elif op == "↔":
            a = V if a is b else F
    return a


def tabla(texto, variables):
    arbol = analizar(texto)
    return [
        (dict(zip(variables, fila)), evaluar(arbol, dict(zip(variables, fila))))
        for fila in product((V, F), repeat=len(variables))
    ]


def columna(texto, variables):
    return "".join(resultado.name for _, resultado in tabla(texto, variables))


def equivalentes(a, b, variables):
    return columna(a, variables) == columna(b, variables)


# Formas agrupadas: conservan significado y distinguen el ejercicio de sintaxis.
EJERCICIO3 = {
    "a": "(p∨¬p)",
    "b": "(p∧¬p)",
    "c": "((¬p∨q)↔(p→q))",
    "d": "((p∨q)→p)",
    "e": "(¬(p∧q)↔(¬p∨¬q))",
    "f": "((¬p∧q)↔(¬p∨¬q))",
    "g": "(p→p)",
    "h": "((p∧q)→p)",
    "i": "((p∧(q∨r))↔((p∧q)∨(p∧r)))",
    "j": "((p→(q→r))→((p→q)→(p→r)))",
}
LEYES = {
    "a": ("(False∧p)", "False"),
    "b": ("(True∨p)", "True"),
    "c": ("(True∧p)", "p"),
    "d": ("(False∨p)", "p"),
    "e": ("(p∧p)", "p"),
    "f": ("(p∨p)", "p"),
    "g": ("(p∨¬p)", "True"),
    "h": ("(p∧¬p)", "False"),
    "i": ("¬¬p", "p"),
    "j": ("(p∧(p∨q))", "p"),
    "k": ("(p∨(p∧q))", "p"),
    "l": ("¬(p∧q)", "(¬p∨¬q)"),
    "m": ("¬(p∨q)", "(¬p∧¬q)"),
    "n": ("(p∧q)", "(q∧p)"),
    "ñ": ("(p∨q)", "(q∨p)"),
    "o": ("(p∧(q∧r))", "((p∧q)∧r)"),
    "p": ("(p∨(q∨r))", "((p∨q)∨r)"),
    "q": ("(p∧(q∨r))", "((p∧q)∨(p∧r))"),
    "r": ("(p∨(q∧r))", "((p∨q)∧(p∨r))"),
    "s": ("(p→q)", "(¬q→¬p)"),
    "t": ("(p→q)", "(¬p∨q)"),
    "u": ("(p↔q)", "((p→q)∧(q→p))"),
}


def tablas_equivalencias():
    lineas = [
        "# Tablas del ejercicio6",
        "",
        "Generadas por logica.py: todas las valuaciones, ambos lados.",
        "",
    ]
    for inciso, (a, b) in LEYES.items():
        variables = sorted(set(re.findall(r"\b[pqr]\b", a + " " + b)))
        lineas += [
            "## " + inciso + " · " + a + " ≡ " + b,
            "",
            "| " + " | ".join(variables + ["Izquierda", "Derecha"]) + " |",
            "|" + "---|" * (len(variables) + 2),
        ]
        for (env, izq), (_, der) in zip(tabla(a, variables), tabla(b, variables)):
            lineas.append(
                "| "
                + " | ".join([env[x].name for x in variables] + [izq.name, der.name])
                + " |"
            )
        lineas.append("")
    return "\n".join(lineas)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--salida", type=Path, help="Guardar las tablas generadas")
    args = parser.parse_args()
    salida = tablas_equivalencias()
    if args.salida:
        args.salida.write_text(salida, encoding="utf-8")
    else:
        print(salida)
