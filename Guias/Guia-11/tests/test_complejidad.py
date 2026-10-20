from queue import Queue, LifoQueue
import unittest
import complejidad as c


class Complejidad(unittest.TestCase):
    def test_sumatorias_equivalentes(self):
        for n in range(100):
            esperado = sum(range(n + 1))
            self.assertEqual(c.sumatoria_1(n), esperado)
            self.assertEqual(c.sumatoria_2(n), esperado)
            self.assertEqual(c.sumatoria_3(n), esperado)
        self.assertEqual(c.cuentas_sumatorias(0), (4, 5, 2))
        self.assertEqual(c.cuentas_sumatorias(10), (54, 5, 42))

    def test_maximos_preservan_estructura(self):
        for tipo in (Queue, LifoQueue):
            q = tipo()
            for x in (3, 1, 4, 2):
                q.put(x)
            self.assertEqual(c.maximo_cola(q), 4)
            extraidos = [q.get() for _ in range(q.qsize())]
            esperado = [3, 1, 4, 2] if tipo is Queue else [2, 4, 1, 3]
            self.assertEqual(extraidos, esperado)
        self.assertEqual(c.maximo_lista([3, 1, 4, 2]), 4)

    def test_equivalencia_diferencias(self):
        for xs in ([1], [-5, -1, 7, 7], [2, 1], [0, 0]):
            self.assertEqual(
                c.maxima_diferencia_cuadratica(xs), c.maxima_diferencia_lineal(xs)
            )

    def test_listas(self):
        self.assertEqual(c.suma_de_productos([1, 2, 3]), 11)
        self.assertEqual(c.elementos_en_pos_pares([1, 2, 3, 4]), [1, 3])
        xs = [4, 5, 6]
        c.sumar_cantidad_veces_indice(xs)
        self.assertEqual(xs, [0, 5, 12])

    def test_matrices(self):
        m = [[1, 2], [3, 4]]
        self.assertEqual(c.diagonal_principal(m), [1, 4])
        self.assertEqual(c.sumar_elementos_matriz(m), 10)
        c.convertir_en_matriz_identidad(m)
        self.assertEqual(m, [[1, 0], [0, 1]])
