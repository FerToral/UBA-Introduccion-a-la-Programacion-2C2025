import unittest
import caja_blanca as c


class CajaBlanca(unittest.TestCase):
    def test_maximo_dos_ramas(self):
        self.assertEqual(c.maximo(0, 0), 0)
        self.assertEqual(c.maximo(0, 1), 1)

    def test_cobertura_no_implica_correctitud(self):
        # Estos dos casos pasan incluso con el defecto, cubriendo ambas ramas.
        self.assertEqual(c.minimo_defectuoso(0, 1), 0)
        self.assertEqual(c.minimo_defectuoso(1, 1), 1)
        self.assertNotEqual(c.minimo_defectuoso(2, 1), 1)
        self.assertEqual(c.minimo(2, 1), 1)

    def test_suma_resta_y_mutante(self):
        self.assertEqual(c.sumar(3, -2), 1)
        self.assertEqual(c.restar_defectuoso(3, 0), 3)
        self.assertNotEqual(c.restar_defectuoso(3, 2), 1)
        self.assertEqual(c.restar(3, 2), 1)

    def test_signo_y_absoluto(self):
        for x, signo in [(-2, -1), (0, 0), (2, 1)]:
            self.assertEqual(c.signo(x), signo)
            self.assertEqual(c.absoluto(x), abs(x))
        self.assertEqual(c.absoluto_defectuoso(-2), 2)
        self.assertEqual(c.absoluto_defectuoso(0), 0)
        self.assertNotEqual(c.absoluto_defectuoso(2), 2)

    def test_bucles(self):
        for x in (-2, 0, 4):
            self.assertEqual(c.mult10(x), 10 * x)
            for y in (-3, 0, 3):
                self.assertEqual(c.sumar_por_unidades(x, y), x + y)
                self.assertEqual(c.mult_by_abs(x, y), x * abs(y))

    def test_mcd(self):
        self.assertEqual(c.mcd(0, 0), 0)
        self.assertEqual(c.mcd(9, 0), 9)
        self.assertEqual(c.mcd(12, 8), 4)

    def test_triangulos(self):
        for lados, esperado in [
            ((0, 2, 2), 4),
            ((1, 1, 2), 4),
            ((2, 2, 2), 1),
            ((2, 2, 3), 2),
            ((3, 4, 5), 3),
        ]:
            self.assertEqual(c.triangle(*lados), esperado)

    def test_secuencias(self):
        for xs in ([], [4], [1, 2, 3]):
            copia = xs[:]
            c.vaciar_secuencia(copia)
            self.assertEqual(copia, [0] * len(xs))
        for xs, e, esperado in [
            ([], 1, False),
            ([1, 2], 3, False),
            ([1, 2], 1, True),
            ([1, 2], 2, True),
        ]:
            self.assertEqual(c.existe_elemento(xs, e), esperado)
