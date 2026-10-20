import contextlib
import io
import random
import unittest
from unittest.mock import Mock, patch
import practicas7 as p


class Practicas7(unittest.TestCase):
    def test_recorridos(self):
        self.assertTrue(p.vocales_distintas("murcielago"))
        self.assertFalse(p.vocales_distintas("aaee"))
        self.assertEqual(p.pos_secuencia_ordenada_mas_larga([1, 2, 2, 0, 1, 2]), 0)
        self.assertEqual(p.cantidad_digitos_impares([57, 2383, 812, 246, 0]), 5)

    def test_modificaciones(self):
        xs = [1, 2, 3, 4]
        self.assertEqual(p.ceros_en_posiciones_pares2(xs), [0, 2, 0, 4])
        self.assertEqual(xs, [1, 2, 3, 4])
        p.ceros_en_posiciones_pares(xs)
        self.assertEqual(xs, [0, 2, 0, 4])
        self.assertEqual(p.sin_vocales("aeioxyz"), "xyz")
        self.assertEqual(p.reemplaza_vocales("hola"), "h l ")
        self.assertEqual(p.da_vuelta_str("abc"), "cba")
        self.assertEqual(p.eliminar_repetidos("abaca"), "abc")

    def test_notas_saldo(self):
        self.assertEqual(
            [p.resultadoMateria(xs) for xs in ([7, 7], [4, 6], [3, 10])], [1, 2, 3]
        )
        self.assertEqual(
            p.saldoActual([("I", 2000), ("R", 20), ("R", 1000), ("I", 300)]), 1280
        )

    def test_parametro_salida(self):
        res = [True, True, True]
        for funcion in (
            p.pertenece_a_cada_uno_version1,
            p.pertenece_a_cada_uno_version2,
        ):
            funcion([[1], [], [1, 2]], 2, res)
            self.assertEqual(res, [False, False, True])
        self.assertEqual(p.pertenece_a_cada_uno_version3([], 2), [])

    def test_matrices(self):
        self.assertTrue(p.es_matriz([[1, 2]]))
        for m in ([], [[]], [[1], [2, 3]]):
            self.assertFalse(p.es_matriz(m))
        m = [[1, 2, 3], [2, 3, 4]]
        self.assertEqual(p.columna(m, 1), [2, 3])
        self.assertEqual(p.columnas_ordenadas(m), [True, True, True])
        self.assertEqual(p.transponer(m), [[1, 2], [2, 3], [3, 4]])
        self.assertEqual(
            p.quien_gana_tateti([["X", " ", "O"], [" ", "X", "O"], [" ", " ", "X"]]), 1
        )
        self.assertEqual(
            p.quien_gana_tateti([["O", "O", "O"], ["X", " ", "X"], [" ", " ", " "]]), 0
        )
        self.assertEqual(p.quien_gana_tateti([[" "] * 3 for _ in range(3)]), 2)

    def test_potencia_opcional(self):
        rng = random.Random(2025)
        base = [[rng.randrange(10) for _ in range(2)] for _ in range(2)]
        self.assertEqual(p.exponenciacion_matriz(2, 1), base)
        self.assertEqual(
            p.exponenciacion_matriz(2, 2), p.multiplicar_matrices(base, base)
        )

    def test_interactivos(self):
        with patch("builtins.input", side_effect=["Ana", "Beto", "listo"]):
            self.assertEqual(p.nombres_estudiantes(), ["Ana", "Beto"])
        with patch("builtins.input", side_effect=["C", "100", "D", "20", "X"]):
            self.assertEqual(p.monedero(), [("C", 100), ("D", 20)])
        rng = Mock()
        rng.choice.side_effect = [7, 10]
        with (
            patch("builtins.input", side_effect=["S", "N"]),
            contextlib.redirect_stdout(io.StringIO()),
        ):
            self.assertEqual(p.siete_y_medio(rng), [7, 10])
        rng.choice.side_effect = [7, 1]
        with (
            patch("builtins.input", return_value="S"),
            contextlib.redirect_stdout(io.StringIO()) as out,
        ):
            self.assertEqual(p.siete_y_medio(rng), [7, 1])
        self.assertIn("Perdiste", out.getvalue())

    def test_fortaleza(self):
        self.assertEqual(p.fortaleza_contrasena("Ab1"), "ROJA")
        self.assertEqual(p.fortaleza_contrasena("Ab123456"), "AMARILLA")
        self.assertEqual(p.fortaleza_contrasena("Ab1234567"), "VERDE")
        self.assertEqual(p.fortaleza_contrasena("ñÑ1234567"), "AMARILLA")
