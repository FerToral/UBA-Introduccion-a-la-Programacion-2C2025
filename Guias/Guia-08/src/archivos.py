"""Guía 8, ejercicios 19–27. Texto UTF-8 y datos ficticios en las pruebas."""

import csv
from pathlib import Path


def contar_lineas(nombre_archivo: str) -> int:
    cantidad: int = 0
    with open(nombre_archivo, encoding="utf-8") as archivo:
        for _ in archivo:
            cantidad += 1
    return cantidad


def cantidad_de_apariciones(nombre_archivo: str, palabra: str) -> int:
    if palabra == "":
        raise ValueError("La palabra no debe ser vacía")
    texto: str = Path(nombre_archivo).read_text(encoding="utf-8")
    cantidad: int = 0
    for i in range(len(texto) - len(palabra) + 1):
        if texto[i : i + len(palabra)] == palabra:
            cantidad += 1
    return cantidad


def existe_palabra(nombre_archivo: str, palabra: str) -> bool:
    return cantidad_de_apariciones(nombre_archivo, palabra) > 0


def agrupar_por_longitud(nombre_archivo: str) -> dict[int, int]:
    cantidades: dict[int, int] = {}
    with open(nombre_archivo, encoding="utf-8") as archivo:
        for linea in archivo:
            for palabra in linea.split():
                n: int = len(palabra)
                cantidades[n] = cantidades.get(n, 0) + 1
    return cantidades


def la_palabra_mas_frecuente(nombre_archivo: str) -> str:
    cantidades: dict[str, int] = {}
    with open(nombre_archivo, encoding="utf-8") as archivo:
        for linea in archivo:
            for palabra in linea.split():
                cantidades[palabra] = cantidades.get(palabra, 0) + 1
    mas_frecuente: str = ""
    mayor: int = 0
    for palabra, cantidad in cantidades.items():
        if cantidad > mayor:
            mas_frecuente, mayor = palabra, cantidad
    if mayor == 0:
        raise ValueError("El archivo debe tener al menos una palabra")
    return mas_frecuente


def clonar_sin_comentarios(
    nombre_archivo_entrada: str, nombre_archivo_salida: str
) -> None:
    with open(nombre_archivo_entrada, encoding="utf-8", newline="") as archivo:
        lineas = archivo.readlines()
    with open(nombre_archivo_salida, "w", encoding="utf-8", newline="") as archivo:
        for linea in lineas:
            if not linea.lstrip(" ").startswith("#"):
                archivo.write(linea)


def invertir_lineas(nombre_archivo_entrada: str, nombre_archivo_salida: str) -> None:
    lineas = Path(nombre_archivo_entrada).read_text(encoding="utf-8").splitlines()
    with open(nombre_archivo_salida, "w", encoding="utf-8", newline="\n") as archivo:
        for i in range(len(lineas) - 1, -1, -1):
            archivo.write(lineas[i] + "\n")


def validar_frase(frase: str) -> None:
    if frase == "" or "\n" in frase or "\r" in frase:
        raise ValueError("Se espera una frase no vacía de una sola línea")


def agregar_frase_al_final(nombre_archivo: str, frase: str) -> None:
    validar_frase(frase)
    texto = Path(nombre_archivo).read_text(encoding="utf-8")
    with open(nombre_archivo, "a", encoding="utf-8", newline="\n") as archivo:
        if texto and not texto.endswith("\n"):
            archivo.write("\n")
        archivo.write(frase + "\n")


def agregar_frase_al_principio(nombre_archivo: str, frase: str) -> None:
    validar_frase(frase)
    texto = Path(nombre_archivo).read_text(encoding="utf-8")
    with open(nombre_archivo, "w", encoding="utf-8", newline="\n") as archivo:
        archivo.write(frase + "\n" + texto)


def listar_textos_de_archivo(nombre_archivo: str) -> list[str]:
    res: list[str] = []
    actual: str = ""
    with open(nombre_archivo, "rb") as archivo:
        for byte in archivo.read():
            c: str = chr(byte)
            if "A" <= c <= "Z" or "a" <= c <= "z" or "0" <= c <= "9" or c in " _":
                actual += c
            else:
                if len(actual) >= 5:
                    res.append(actual)
                actual = ""
    if len(actual) >= 5:
        res.append(actual)
    return res


def calcular_promedio_por_estudiante(
    nombre_archivo_notas: str, nombre_archivo_promedios: str
) -> None:
    if Path(nombre_archivo_notas).resolve() == Path(nombre_archivo_promedios).resolve():
        raise ValueError("El archivo de salida debe ser distinto del de entrada")
    acumulados: dict[str, tuple[float, int]] = {}
    with open(nombre_archivo_notas, encoding="utf-8", newline="") as archivo:
        for lu, _, _, nota in csv.reader(archivo):
            total, cantidad = acumulados.get(lu, (0.0, 0))
            acumulados[lu] = total + float(nota), cantidad + 1
    with open(nombre_archivo_promedios, "w", encoding="utf-8", newline="") as archivo:
        salida = csv.writer(archivo)
        for lu, (total, cantidad) in acumulados.items():
            salida.writerow([lu, total / cantidad])
