"""Pruebas de pertenencia y orden estricto de filas y columnas."""

import unittest

from guia7 import (
    pertenece,
    pertenecev2,
    pertenecev3,
    columnas_ordenas,
    columnas_ordenasv2,
    filas_ordenadas,
)


class test_sumar(unittest.TestCase):
    def test_pertenece(self):
        self.assertFalse(pertenece([], 1))
        self.assertTrue(pertenece([1], 1))
        self.assertFalse(pertenece([1], 2))
        self.assertTrue(pertenece([1, 2, 3, 4], 3))

    def test_pertenecev2(self):
        self.assertFalse(pertenecev2([], 1))
        self.assertTrue(pertenecev2([1], 1))
        self.assertFalse(pertenecev2([1], 2))
        self.assertTrue(pertenecev2([1, 2, 3, 4], 3))

    def test_pertenecev3(self):
        self.assertFalse(pertenecev3([], 1))
        self.assertTrue(pertenecev3([1], 1))
        self.assertFalse(pertenecev3([1], 2))
        self.assertTrue(pertenecev3([1, 2, 3, 4], 3))


class test_matriz_ordenada(unittest.TestCase):
    def test_filas_ordenadas(self):
        self.assertEqual(
            filas_ordenadas([[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [4, 6, 8, 14]]),
            [True, True, True],
        )
        self.assertEqual(
            filas_ordenadas([[1, 2, 5, 4, 5], [2, 4, 3, 8, 10], [42, 6, 8, 14]]),
            [False, False, False],
        )

    def test_columnas_ordenadas(self):
        self.assertEqual(
            columnas_ordenasv2([[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [4, 6, 8, 10, 12]]),
            [True, True, True, True, True],
        )
        self.assertEqual(
            columnas_ordenasv2([[1, 2, 5, 4, 5], [2, 4, 3, 8, 10], [42, 1, 3, 8, 14]]),
            [True, False, False, False, True],
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
