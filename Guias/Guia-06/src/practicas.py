"""Actividades de la guía 6 que completan las prácticas personales."""

import math
from guia6 import es_multiplo_de, es_nombre_largo, fahrenheit_a_celsius


def imprimir_hola_mundo() -> None:
    print("¡Hola mundo!")


def imprimir_un_verso() -> None:
    # Versos propios para practicar saltos de línea.
    print("Trazo un camino al andar,\ny otra pregunta al llegar.")


def raizDe2() -> float:
    return round(math.sqrt(2), 4)


def factorial_de_dos() -> int:
    return 2


def perimetro() -> float:
    return 2 * math.pi


def imprimir_saludo(nombre: str) -> None:
    print("Hola " + nombre)


def raiz_cuadrada_de(numero: float) -> float:
    return math.sqrt(numero)


def imprimir_dos_veces(estribillo: str) -> None:
    print(estribillo * 2)


def es_par(numero: int) -> bool:
    return es_multiplo_de(numero, 2)


def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
    return (comensales * min_cant_de_porciones + 7) // 8


def alguno_es_0(a: float, b: float) -> bool:
    return a == 0 or b == 0


def ambos_son_0(a: float, b: float) -> bool:
    return a == 0 and b == 0


def es_bisiesto(anio: int) -> bool:
    return anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0)


def peso_pino(altura: float) -> float:
    return 300 * min(altura, 3) + 200 * max(altura - 3, 0)


def es_peso_util(peso: float) -> bool:
    return 400 <= peso <= 1000


def sirve_pino(altura: float) -> bool:
    return es_peso_util(peso_pino(altura))


def devolver_valor_si_es_par_sino_el_que_sigue(numero: int) -> int:
    if es_par(numero):
        return numero
    return numero + 1


def doble_o_triple(numero: int) -> int:
    if numero % 9 == 0:
        return 3 * numero
    if numero % 3 == 0:
        return 2 * numero
    return numero


def lindo_nombre(nombre: str) -> str:
    if len(nombre) >= 5:
        return "Tu nombre tiene muchas letras!"
    return "Tu nombre tiene menos de 5 caracteres"


def elRango(numero: int) -> None:
    if numero < 5:
        print("Menor a 5")
    elif 10 <= numero <= 20:
        print("Entre 10 y 20")
    elif numero > 20:
        print("Mayor a 20")


def vacaciones_del_ejercicio(sexo: str, edad: int) -> None:
    """Regla simplificada de la consigna; no asesoramiento previsional."""
    if edad < 18 or (sexo == "F" and edad >= 60) or (sexo == "M" and edad >= 65):
        print("Andá de vacaciones")
    else:
        print("Te toca trabajar")


def uno_a_diez() -> None:
    n: int = 1
    while n <= 10:
        print(n)
        n += 1


def uno_a_diez_for() -> None:
    for n in range(1, 11):
        print(n)


def eco() -> None:
    n: int = 0
    while n < 10:
        print("eco")
        n += 1


def eco_for() -> None:
    for _ in range(10):
        print("eco")


def viajar(partida: int, llegada: int) -> None:
    anio: int = partida
    while anio > llegada:
        anio -= 1
        print("Viajó un año al pasado, estamos en el año:", anio)


def viajar_for(partida: int, llegada: int) -> None:
    for anio in range(partida - 1, llegada - 1, -1):
        print("Viajó un año al pasado, estamos en el año:", anio)


def viaje_aristoteles(partida: int) -> None:
    saltos: int = (partida + 384 + 9) // 20
    anio: int = partida
    while saltos > 0:
        anio -= 20
        saltos -= 1
        print("Viajó veinte años al pasado, estamos en el año:", anio)


def viaje_aristoteles_for(partida: int) -> None:
    saltos: int = (partida + 384 + 9) // 20
    for anio in range(partida - 20, partida - 20 * saltos - 1, -20):
        print("Viajó veinte años al pasado, estamos en el año:", anio)


g: int = 0


def rt(x: int, g: int) -> int:
    g = g + 1
    return x + g


def ro(x: int) -> int:
    global g
    g = g + 1
    return x + g
