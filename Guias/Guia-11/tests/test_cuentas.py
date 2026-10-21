from itertools import product
import unittest
import cuentas as c


class Cuentas(unittest.TestCase):
    def test_productos_bordes(self):
        self.assertEqual(c.productos(0), (3, 4, 4, 4, 4, 4, 14))
        self.assertEqual(c.productos(1), (3, 9, 9, 15, 21, 4, 43))
        self.assertEqual(c.productos(8)[5], 19)
        self.assertEqual(c.productos(9)[5], 24)

    def test_auxiliar_valor_absoluto_depende_de_iguales(self):
        self.assertEqual(c.comparaciones([1])["maxima_diferencia"], (21, 8, 6))
        self.assertLess(
            c.comparaciones([1, 2])["maxima_diferencia"][0],
            c.comparaciones([1, 1])["maxima_diferencia"][0],
        )
        self.assertEqual(c.suma_matriz(2, 3), (64, 52, 44))

    def test_extremos_en_todas_las_listas_pequenas(self):
        for n in range(1, 6):
            pares, umbral, minimos, colapsar = [], [], [], []
            for xs in product((-1, 0, 1), repeat=n):
                pares.append(c.sumar_pares(xs))
                umbral.append(c.hasta_umbral(xs, 0))
                minimos.append(c.minimos(xs))
                colapsar.append(c.colapsar("".join(map(str, [x + 1 for x in xs]))))
            self.assertEqual((min(pares), max(pares)), (5 * n + 4, 7 * n + 4))
            self.assertEqual((min(umbral), max(umbral)), (5, 6 * n + 4))
            self.assertEqual((min(minimos), max(minimos)), (8 * n + 5, 10 * n + 3))
            self.assertEqual((min(colapsar), max(colapsar)), (5 * n - 1, 7 * n - 3))

    def test_signos_por_fila_y_vacio(self):
        self.assertEqual(c.hasta_umbral([], 10), 4)
        self.assertEqual(c.filas_negativas([[1, 2], [3, 4]]), 12)
        self.assertEqual(c.filas_negativas([[-1, -2], [-3, -4]]), 36)
        with self.assertRaises(ValueError):
            c.filas_negativas([[1, -1]])
