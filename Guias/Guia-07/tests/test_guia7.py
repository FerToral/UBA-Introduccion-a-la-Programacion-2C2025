"""Casos límite y propiedades de las funciones de la Guía 7."""

import copy
import importlib.util
import io
import itertools
import unittest
from contextlib import redirect_stdout

import guia7 as guia


class TestRegresion(unittest.TestCase):
    def test_divide_lista_vacia(self):
        self.assertIs(guia.divide_a_todos([], 3), True)

    def test_divide_revisa_elementos_posteriores(self):
        self.assertIs(guia.divide_a_todos([2, 3], 2), False)
        self.assertIs(guia.divide_a_todos([4, 8, 9], 2), False)

    def test_divide_negativos_y_cero(self):
        self.assertIs(guia.divide_a_todos([0, -4, 6], -2), True)
        self.assertIs(guia.divide_a_todos([-3, 4], 2), False)

    def test_orden_estricto(self):
        for funcion in (guia.ordenados, guia.lista_ordenada):
            self.assertIs(funcion([1, 1]), False)
            self.assertIs(funcion([-2, 0, 0, 4]), False)
            self.assertIs(funcion([-2, 0, 4]), True)

    def test_orden_vacio_y_unitario(self):
        for funcion in (guia.ordenados, guia.lista_ordenada):
            self.assertIs(funcion([]), True)
            self.assertIs(funcion([3]), True)

    def test_tres_iguales_en_ultima_ventana(self):
        self.assertIs(guia.iguales_consecutivos([1, 2, 3, 9, 9, 9]), True)

    def test_tres_iguales_solapados(self):
        self.assertIs(guia.iguales_consecutivos([1, 2, 2, 2, 2, 3]), True)

    def test_filas_con_repetidos(self):
        self.assertEqual(
            guia.filas_ordenadas([[1, 1], [1, 2], [2, 1]]), [False, True, False]
        )

    def test_columnas_con_repetidos(self):
        for funcion in (guia.columnas_ordenas, guia.columnas_ordenasv2):
            self.assertEqual(funcion([[1, 2], [1, 3], [2, 4]]), [False, True])

    def test_columnas_independientes(self):
        for funcion in (guia.columnas_ordenas, guia.columnas_ordenasv2):
            self.assertEqual(
                funcion([[3, 1, 2], [2, 2, 2], [1, 3, 2]]), [False, True, False]
            )

    def test_matriz_una_fila(self):
        for funcion in (guia.columnas_ordenas, guia.columnas_ordenasv2):
            self.assertEqual(funcion([[3, 1, 1]]), [True, True, True])

    def test_matriz_una_columna(self):
        self.assertEqual(guia.filas_ordenadas([[3], [2], [1]]), [True, True, True])
        for funcion in (guia.columnas_ordenas, guia.columnas_ordenasv2):
            self.assertEqual(funcion([[3], [2], [1]]), [False])

    def test_suma_vacio_y_negativos(self):
        self.assertEqual(guia.suma_total([]), 0)
        self.assertEqual(guia.suma_total([-4, 1, 2]), -1)

    def test_extremos_no_inicializados_en_cero(self):
        self.assertEqual(guia.maximo([-7, -2, -9]), -2)
        self.assertEqual(guia.minimo([7, 2, 9]), 2)

    def test_posiciones_desempates(self):
        self.assertEqual(guia.pos_maximo([9, 1, 9]), 0)
        self.assertEqual(guia.pos_minimo([1, 9, 1]), 2)
        self.assertEqual(guia.pos_maximo([]), -1)
        self.assertEqual(guia.pos_minimo([]), -1)

    def test_palindromos_y_cadenas_vacias(self):
        for texto in ("", "a", "neuquen", "abba"):
            self.assertIs(guia.es_palindroma(texto), True)
        self.assertIs(guia.es_palindroma("abc"), False)

    def test_palabra_larga_en_ultima_posicion(self):
        self.assertIs(guia.long_mayorAsiete(["corta", "abcdefgh"]), True)
        self.assertIs(guia.long_mayorAsiete(["abcdefg"]), False)
        self.assertIs(guia.long_mayorAsiete([]), False)

    def test_listas_in_no_se_modifican(self):
        funciones = [
            guia.suma_total,
            guia.maximo,
            guia.minimo,
            guia.ordenados,
            guia.pos_maximo,
            guia.pos_minimo,
            guia.iguales_consecutivos,
            lambda s: guia.divide_a_todos(s, 2),
            lambda s: guia.pertenece(s, 3),
            lambda s: guia.pertenecev2(s, 3),
            lambda s: guia.pertenecev3(s, 3),
        ]
        for funcion in funciones:
            entrada = [2, 3, 3, 3, -1]
            anterior = entrada.copy()
            funcion(entrada)
            self.assertEqual(entrada, anterior)

    def test_matrices_in_no_se_modifican(self):
        for funcion in (
            guia.filas_ordenadas,
            guia.columnas_ordenas,
            guia.columnas_ordenasv2,
        ):
            entrada = [[3, 1], [2, 2], [1, 3]]
            anterior = copy.deepcopy(entrada)
            funcion(entrada)
            self.assertEqual(entrada, anterior)

    def test_importacion_silenciosa(self):
        spec = importlib.util.spec_from_file_location(
            "guia7_importacion", guia.__file__
        )
        copia = importlib.util.module_from_spec(spec)
        salida = io.StringIO()
        with redirect_stdout(salida):
            spec.loader.exec_module(copia)
        self.assertEqual(salida.getvalue(), "")


class TestPropiedadesAcotadas(unittest.TestCase):
    def test_listas_longitud_cero_a_seis(self):
        # 1093 listas. Oráculos independientes; no son funciones de producción.
        for longitud in range(7):
            for valores in itertools.product((-1, 0, 1), repeat=longitud):
                s = list(valores)
                self.assertEqual(guia.suma_total(s), sum(s), s)
                self.assertEqual(
                    guia.ordenados(s), all(a < b for a, b in zip(s, s[1:])), s
                )
                for divisor in (-2, -1, 1, 2):
                    self.assertEqual(
                        guia.divide_a_todos(s, divisor),
                        all(x % divisor == 0 for x in s),
                        (s, divisor),
                    )
                for elemento in (-2, -1, 0, 1, 2):
                    for funcion in (guia.pertenece, guia.pertenecev2, guia.pertenecev3):
                        self.assertEqual(funcion(s, elemento), elemento in s, s)
                if s:
                    self.assertEqual(guia.maximo(s), max(s), s)
                    self.assertEqual(guia.minimo(s), min(s), s)
                    self.assertEqual(guia.pos_maximo(s), s.index(max(s)), s)
                    self.assertEqual(
                        guia.pos_minimo(s), len(s) - 1 - s[::-1].index(min(s)), s
                    )

    def test_triples_longitud_cero_a_siete(self):
        # 3280 listas; las ventanas se calculan de otra forma que en producción.
        for longitud in range(8):
            for valores in itertools.product((-1, 0, 1), repeat=longitud):
                s = list(valores)
                esperado = any(
                    len(set(s[inicio : inicio + 3])) == 1
                    for inicio in range(max(0, longitud - 2))
                )
                self.assertEqual(guia.iguales_consecutivos(s), esperado, s)

    def test_matrices_rectangulares_acotadas(self):
        # 1560 matrices de tamaños 1x1, 1x2, 2x1, 2x2, 2x3 y 3x2.
        for filas, columnas in ((1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (3, 2)):
            for datos in itertools.product((-1, 0, 1), repeat=filas * columnas):
                matriz = [
                    list(datos[i * columnas : (i + 1) * columnas]) for i in range(filas)
                ]
                esperado_filas = [
                    all(a < b for a, b in zip(fila, fila[1:])) for fila in matriz
                ]
                esperado_columnas = [
                    all(a < b for a, b in zip(columna, columna[1:]))
                    for columna in zip(*matriz)
                ]
                self.assertEqual(guia.filas_ordenadas(matriz), esperado_filas, matriz)
                self.assertEqual(
                    guia.columnas_ordenas(matriz), esperado_columnas, matriz
                )
                self.assertEqual(
                    guia.columnas_ordenasv2(matriz), esperado_columnas, matriz
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
