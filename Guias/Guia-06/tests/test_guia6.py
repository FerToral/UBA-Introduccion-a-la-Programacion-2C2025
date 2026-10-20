"""Pruebas de las funciones de la Guía 6."""

import contextlib
import importlib.util
import io
import math
import unittest

import alcance_variables
from guia6 import (
    suma,
    triada_trigonometrica,
    es_multiplo_de,
    doble_si_es_par,
    fahrenheit_a_celsius,
    es_primo,
    cantidad_primos,
)


class test_sumar(unittest.TestCase):
    def test_suma_positiva(self):
        self.assertEqual(suma(2, 3), 5)

    def test_suma_negativa(self):
        self.assertEqual(suma(-3, -4), -7)

    def test_suma_nula(self):
        self.assertEqual(suma(0, 0), 0)


class test_triada_pitagorica(unittest.TestCase):
    def test_triada_trigonometrica_correcta(self):
        self.assertTrue(triada_trigonometrica(4, 3, 5))

    def test_triada_trigonometrica_incorrecta(self):
        self.assertFalse(triada_trigonometrica(2, 3, 4))

    def test_triada_trigonometrica_ok_desordenada(self):
        self.assertFalse(triada_trigonometrica(5, 4, 3))


class test_par(unittest.TestCase):
    def test_es_par(self):
        self.assertEqual(doble_si_es_par(2), 4)

    def test_impar(self):
        self.assertEqual(doble_si_es_par(3), 3)

    def test_es_nulo(self):
        self.assertEqual(doble_si_es_par(0), 0)

    def test_es_par_negativo(self):
        self.assertEqual(doble_si_es_par(-2), -4)

    def test_es_impar_(self):
        self.assertEqual(doble_si_es_par(-3), -3)


class test_multiplos(unittest.TestCase):
    def test_es_multiplo(self):
        self.assertTrue(es_multiplo_de(4, 2))

    def test_es_el_mismo(self):
        self.assertTrue(es_multiplo_de(4, 4))

    def test_no_es_multiplo(self):
        self.assertFalse(es_multiplo_de(3, 2))


class test_conversion_celsius(unittest.TestCase):
    def test_conversion_correcta(self):
        self.assertEqual(fahrenheit_a_celsius(32), 0)

    def test_conversion_correcta_decimales(self):
        self.assertAlmostEqual(
            fahrenheit_a_celsius(250), 121.111, places=3, delta=None, msg=None
        )

    def test_conversion_correcta_cero_absoluto(self):
        self.assertAlmostEqual(
            fahrenheit_a_celsius(-459.67), -273.15, places=3, delta=None, msg=None
        )

    def test_conversion_incorrecta(self):
        self.assertNotEqual(fahrenheit_a_celsius(32), -1)


class test_primos(unittest.TestCase):
    def test_no_es_primo_negativo(self):
        self.assertFalse(es_primo(-3))

    def test_es_primo2(self):
        self.assertTrue(es_primo(2))

    def test_no_es_primo(self):
        self.assertFalse(es_primo(4))

    def test_es_primo1(self):
        self.assertFalse(es_primo(1))

    def test_primos_impares(self):
        self.assertTrue(es_primo(3))
        self.assertTrue(es_primo(97))

    def test_compuestos_impares(self):
        self.assertFalse(es_primo(9))
        self.assertFalse(es_primo(25))

    def test_cantidad_primos_intervalo_inclusivo(self):
        self.assertEqual(cantidad_primos(1, 10), 4)
        self.assertEqual(cantidad_primos(10, 1), 4)
        self.assertEqual(cantidad_primos(2, 2), 1)
        self.assertEqual(cantidad_primos(-5, 1), 0)


class TestAlcanceVariables(unittest.TestCase):
    def test_perimetro(self):
        self.assertAlmostEqual(alcance_variables.perimetro(2), 4 * math.pi)

    def test_importacion_sin_ejecutar_ejemplos(self):
        spec = importlib.util.spec_from_file_location(
            "alcance_ejemplo", alcance_variables.__file__
        )
        modulo = importlib.util.module_from_spec(spec)
        salida = io.StringIO()
        with contextlib.redirect_stdout(salida):
            spec.loader.exec_module(modulo)
        self.assertEqual(salida.getvalue(), "")
        self.assertEqual(modulo.xGlobal, 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
