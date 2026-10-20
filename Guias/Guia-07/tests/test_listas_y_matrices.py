"""Pruebas de pertenencia, matrices y elementos consecutivos."""

import unittest

from guia7 import (
    pertenece,
    pertenecev2,
    pertenecev3,
    columnas_ordenas,
    columnas_ordenasv2,
    filas_ordenadas,
    iguales_consecutivos,
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


class TestIgualesConsecutivos(unittest.TestCase):
    def test_tres_iguales_al_principio(self):
        self.assertTrue(iguales_consecutivos([5, 5, 5, 2, 3]))

    def test_tres_iguales_al_final(self):
        self.assertTrue(iguales_consecutivos([1, 2, 3, 4, 7, 7, 7]))

    def test_tres_iguales_en_el_medio(self):
        self.assertTrue(iguales_consecutivos([1, 2, 9, 9, 9, 3, 4]))

    def test_sin_tres_iguales(self):
        self.assertFalse(iguales_consecutivos([1, 1, 2, 2, 3, 3]))

    def test_lista_vacia(self):
        self.assertFalse(iguales_consecutivos([]))

    def test_lista_con_un_elemento(self):
        self.assertFalse(iguales_consecutivos([7]))

    def test_lista_con_dos_elementos(self):
        self.assertFalse(iguales_consecutivos([8, 8]))

    def test_lista_exactamente_tres_no_iguales(self):
        self.assertFalse(iguales_consecutivos([1, 2, 3]))

    def test_lista_exactamente_tres_iguales(self):
        self.assertTrue(iguales_consecutivos([4, 4, 4]))

    def test_lista_con_valores_negativos(self):
        self.assertTrue(iguales_consecutivos([-2, -2, -2, 0]))

    def test_lista_larga_con_iguales_espaciados(self):
        self.assertFalse(iguales_consecutivos([1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7]))

    def test_lista_con_muchos_repetidos_pero_no_tres_seguidos(self):
        self.assertFalse(iguales_consecutivos([2, 2, 3, 3, 2, 2, 3, 3]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
