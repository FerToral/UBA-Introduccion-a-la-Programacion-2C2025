import unittest
import contratos as c


class Contratos(unittest.TestCase):
    def test_raices_y_subespecificacion(self):
        self.assertTrue(c.raices_admitidas(1, [9, 4], [3, 2]))
        self.assertFalse(c.raices_admitidas(1, [9, 4], [2, 3]))
        self.assertTrue(c.raices_admitidas(2, [9, 4], [2, 3]))
        self.assertTrue(c.raices_admitidas(3, [9, 4], [3, 3]))
        self.assertFalse(c.raices_admitidas(2, [9, 4], [3, 3]))
        self.assertTrue(c.raices_admitidas(4, [-1, 4], [2, 2]))
        self.assertTrue(c.raices_admitidas(5, [9, 4], [3]))
        self.assertTrue(c.raices_admitidas(5, [9, 4], [3, 2, 99]))
        self.assertFalse(c.raices_admitidas(6, [9, 4], [3, 2, 99]))
        self.assertTrue(c.raices_admitidas(6, [9, 4], []))
        self.assertFalse(
            c.raices_admitidas(2, [4, 1, 1], [2, 2, 1])
        )  # aún rige no repetidos
        self.assertTrue(
            c.raices_admitidas(2, [4, 1, 1], [2, 2, 1], exigir_sin_repetidos=False)
        )

    def test_ordenar_con_multiplicidades(self):
        self.assertTrue(c.ordenamiento_valido([4, 3, 3, 5], [3, 3, 4, 5]))
        self.assertFalse(c.ordenamiento_valido([4, 3, 3, 5], [3, 4, 5]))
        self.assertFalse(c.ordenamiento_valido([4, 3, 5], [1, 2, 3]))
        self.assertTrue(c.ordenamiento_valido([], []))

    def test_duplicar_posicional(self):
        self.assertTrue(c.duplicados_posicionales([-2, 0, 3], [-4, 0, 6]))
        self.assertFalse(c.duplicados_posicionales([1, 2], [4, 2]))
        self.assertFalse(c.duplicados_posicionales([1, 2], [8, 10]))

    def test_colectivos_y_empate(self):
        s = [28, 33, 28, 45]
        self.assertEqual(c.cantidad_colectivos(s, 28), 2)
        self.assertEqual(c.mejor_frecuencia(s, 28, 33), 28)
        self.assertEqual(c.mejor_frecuencia([], 33, 34), 33)
        with self.assertRaises(ValueError):
            c.cantidad_colectivos([999], 28)

    def test_calificaciones_ficticias_y_recursadas(self):
        registro = [
            ("Zeta", [("A", 2), ("A", 6), ("B", 6)]),
            ("Alfa", [("A", 8), ("B", 8)]),
        ]
        self.assertAlmostEqual(c.promedio_de_alumno("Zeta", registro), 14 / 3)
        self.assertEqual(c.materias_con_mejor_nota(registro[0][1]), ["A", "B"])
        self.assertEqual(c.aprobaron("A", registro), ["Zeta", "Alfa"])
        self.assertEqual(c.aprobaron("A", registro, True), ["Alfa", "Zeta"])
        self.assertEqual(c.promedios(registro), [14 / 3, 8])
        self.assertEqual(c.aprobaron("C", registro), [])

    def test_precondiciones_calificaciones(self):
        for registro in [
            [("A", [("X", 4), ("X", 5)])],
            [("A", [("X", 11)])],
            [("A", []), ("A", [])],
        ]:
            with self.assertRaises(ValueError):
                c.validar_registro(registro)
        with self.assertRaises(ValueError):
            c.promedio_de_alumno("A", [("A", [])])
        with self.assertRaises(ValueError):
            c.promedio_de_alumno("No está", [])

    def test_se_suman_valores_no_absolutos(self):
        self.assertEqual(c.sumar_abs_mayor_a5([-6, 7]), 1)
        self.assertEqual(c.sumar_abs_mayor_a5([-5, 5]), 0)
