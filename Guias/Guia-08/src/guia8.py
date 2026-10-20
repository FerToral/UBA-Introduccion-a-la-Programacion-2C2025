"""Ejercicios 1–18 de la Guía 8: pilas, colas y diccionarios."""

from queue import LifoQueue as Pila
from queue import Queue as Cola
from random import randint, shuffle
from typing import TypeVar


T = TypeVar("T")


def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila:
    pila = Pila()
    for _ in range(cantidad):
        pila.put(randint(desde, hasta))
    return pila


def cantidad_elementos(p: Pila) -> int:
    elementos = []
    while not p.empty():
        elementos.append(p.get())
    for elemento in reversed(elementos):
        p.put(elemento)
    return len(elementos)


def buscar_el_maximo(p: Pila) -> int:
    elementos = []
    while not p.empty():
        elementos.append(p.get())
    for elemento in reversed(elementos):
        p.put(elemento)
    return max(elementos)


def print_pila(p: Pila) -> None:
    elementos = []
    while not p.empty():
        elementos.append(p.get())
    for elemento in elementos:
        print(elemento)
    for elemento in reversed(elementos):
        p.put(elemento)


def buscar_nota_maxima(p: Pila) -> tuple[str, int]:
    elementos = []
    while not p.empty():
        elementos.append(p.get())
    for elemento in reversed(elementos):
        p.put(elemento)
    return max(elementos, key=lambda nota: nota[1])


def esta_bien_balanceada(s: str) -> bool:
    abiertos = Pila()
    for caracter in s:
        if caracter == "(":
            abiertos.put(caracter)
        elif caracter == ")":
            if abiertos.empty():
                return False
            abiertos.get()
    return abiertos.empty()


def es_opeador(c: str) -> bool:
    """Conserva el nombre histórico, incluido su error ortográfico."""
    return c in {"+", "-", "*", "/"}


def operacion(c: str, a: int, b: int) -> float:
    if c == "+":
        return a + b
    if c == "-":
        return a - b
    if c == "*":
        return a * b
    if c == "/":
        return a / b
    raise ValueError(f"operador desconocido: {c}")


def evaluar_expresion(s: str) -> float:
    resultados = Pila()
    for token in s.split():
        if es_opeador(token):
            b = resultados.get()
            a = resultados.get()
            resultados.put(operacion(token, a, b))
        else:
            resultados.put(int(token))
    return resultados.get()


def intercalar_pilas(p1: Pila, p2: Pila) -> Pila:
    """Intercala en orden de tope y deja intactas las dos entradas."""
    pares = []
    while not p1.empty():
        pares.append((p1.get(), p2.get()))
    for a, b in reversed(pares):
        p1.put(a)
        p2.put(b)

    resultado = Pila()
    elementos = []
    for a, b in pares:
        elementos.extend((b, a))
    for elemento in reversed(elementos):
        resultado.put(elemento)
    return resultado


def generar_nros_al_azarv2(cantidad: int, desde: int, hasta: int) -> Cola:
    cola = Cola()
    for _ in range(cantidad):
        cola.put(randint(desde, hasta))
    return cola


def tam(c: Cola) -> int:
    elementos = []
    while not c.empty():
        elementos.append(c.get())
    for elemento in elementos:
        c.put(elemento)
    return len(elementos)


def buscar_el_maximov2(c: Cola) -> int:
    elementos = []
    while not c.empty():
        elementos.append(c.get())
    for elemento in elementos:
        c.put(elemento)
    return max(elementos)


def buscar_nota_minima(c: Cola) -> tuple[str, int]:
    elementos = []
    while not c.empty():
        elementos.append(c.get())
    for elemento in elementos:
        c.put(elemento)
    return min(elementos, key=lambda nota: nota[1])


def intercalar_colas(c1: Cola, c2: Cola) -> Cola:
    pares = []
    while not c1.empty():
        pares.append((c1.get(), c2.get()))
    for a, b in pares:
        c1.put(a)
        c2.put(b)

    resultado = Cola()
    for a, b in pares:
        resultado.put(a)
        resultado.put(b)
    return resultado


# En la copia histórica el segundo ``intercalar`` (el de colas) sobrescribía
# al primero. Se conserva ese nombre para compatibilidad; el de pilas queda
# disponible explícitamente como ``intercalar_pilas``.
intercalar = intercalar_colas


def armar_secuencia_bingo() -> Cola:
    numeros = list(range(100))
    shuffle(numeros)
    bolillero = Cola()
    for numero in numeros:
        bolillero.put(numero)
    return bolillero


def jugar_carton_de_bingo(carton: list[int], bolillero: Cola) -> int:
    carton_pendiente = set(carton)
    extraidas = 0
    elementos = []
    while not bolillero.empty():
        numero = bolillero.get()
        elementos.append(numero)
        extraidas += 1
        carton_pendiente.discard(numero)
        if not carton_pendiente:
            # Se sigue drenando abajo para poder restaurar la cola completa.
            break
    while not bolillero.empty():
        elementos.append(bolillero.get())
    for numero in elementos:
        bolillero.put(numero)
    return extraidas


def pacientes_urgentes(c: Cola) -> int:
    elementos = []
    while not c.empty():
        elementos.append(c.get())
    for paciente in elementos:
        c.put(paciente)
    return sum(paciente[0] < 4 for paciente in elementos)


def atencion_a_clientes(c: Cola) -> Cola:
    prioridad, preferencial, resto = [], [], []
    elementos = []
    while not c.empty():
        cliente = c.get()
        elementos.append(cliente)
        if cliente[3]:
            prioridad.append(cliente)
        elif cliente[2]:
            preferencial.append(cliente)
        else:
            resto.append(cliente)
    for cliente in elementos:
        c.put(cliente)

    resultado = Cola()
    for cliente in prioridad + preferencial + resto:
        resultado.put(cliente)
    return resultado


def print_cola(c: Cola) -> None:
    elementos = []
    while not c.empty():
        elementos.append(c.get())
    for elemento in elementos:
        print(elemento)
    for elemento in elementos:
        c.put(elemento)


def pertenece(s: list[T], e: T) -> bool:
    return e in s


def promedio(notas: list[tuple[str, float]], estudiante: str) -> float:
    valores = [nota for nombre, nota in notas if nombre == estudiante]
    if not valores:
        raise ValueError(f"no hay notas para {estudiante!r}")
    return sum(valores) / len(valores)


def calcular_promedio_por_estudiante(
    notas: list[tuple[str, float]],
) -> dict[str, float]:
    acumulados: dict[str, list[float]] = {}
    for estudiante, nota in notas:
        acumulados.setdefault(estudiante, []).append(nota)
    return {
        estudiante: sum(valores) / len(valores)
        for estudiante, valores in acumulados.items()
    }


def visitar_sitio(historiales: dict[str, Pila], usuario: str, sitio: str) -> None:
    historiales.setdefault(usuario, Pila()).put(sitio)


def navegar_atras(historiales: dict[str, Pila], usuario: str) -> str:
    return historiales[usuario].get()


def agregar_producto(
    inventario: dict[str, dict[str, int | float]],
    nombre: str,
    precio: float,
    cantidad: int,
) -> None:
    inventario[nombre] = {"precio": precio, "cantidad": cantidad}


def actualizar_stock(
    inventario: dict[str, dict[str, int | float]], nombre: str, cantidad: int
) -> None:
    inventario[nombre]["cantidad"] = cantidad


def actualizar_precio(
    inventario: dict[str, dict[str, int | float]], nombre: str, precio: float
) -> None:
    inventario[nombre]["precio"] = precio


def calcular_valor_inventario(inventario: dict[str, dict[str, int | float]]) -> float:
    return sum(datos["precio"] * datos["cantidad"] for datos in inventario.values())


if __name__ == "__main__":
    pila = generar_nros_al_azar(5, 6, 9)
    print_pila(pila)
    print("El max:", buscar_el_maximo(pila))
