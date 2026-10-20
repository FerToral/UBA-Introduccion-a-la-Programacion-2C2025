import contextlib
import io
import math
import unittest
import guia6
import alcance_variables
import practicas as p


def salida(f, *args):
    res = io.StringIO()
    with contextlib.redirect_stdout(res):
        f(*args)
    return res.getvalue()


class Practicas(unittest.TestCase):
    def test_constantes_y_salida(self):
        self.assertEqual(salida(p.imprimir_hola_mundo), "¡Hola mundo!\n")
        self.assertEqual(len(salida(p.imprimir_un_verso).splitlines()), 2)
        self.assertEqual(p.raizDe2(), 1.4142)
        self.assertEqual(p.factorial_de_dos(), 2)
        self.assertEqual(p.perimetro(), 2 * math.pi)
        self.assertEqual(salida(p.imprimir_saludo, "Ana"), "Hola Ana\n")
        self.assertEqual(salida(p.imprimir_dos_veces, "eco"), "ecoeco\n")
        self.assertEqual(p.raiz_cuadrada_de(9), 3)

    def test_logica_y_pizzas(self):
        self.assertTrue(p.es_par(0))
        self.assertTrue(p.alguno_es_0(0, 2))
        self.assertFalse(p.ambos_son_0(0, 2))
        self.assertEqual(
            [
                p.cantidad_de_pizzas(0, 2),
                p.cantidad_de_pizzas(4, 2),
                p.cantidad_de_pizzas(3, 3),
            ],
            [0, 1, 2],
        )
        self.assertFalse(p.es_bisiesto(1900))
        self.assertTrue(p.es_bisiesto(2000))

    def test_pinos_y_condicionales(self):
        self.assertEqual(p.peso_pino(2), 600)
        self.assertEqual(p.peso_pino(5), 1300)
        self.assertTrue(p.sirve_pino(2))
        self.assertFalse(p.sirve_pino(5))
        self.assertEqual(p.devolver_valor_si_es_par_sino_el_que_sigue(3), 4)
        self.assertEqual([p.doble_o_triple(n) for n in (18, 3, 2)], [54, 6, 2])
        self.assertEqual(p.lindo_nombre("Ana"), "Tu nombre tiene menos de 5 caracteres")
        self.assertEqual(salida(p.elRango, 7), "")
        self.assertEqual(salida(p.elRango, 20), "Entre 10 y 20\n")
        self.assertEqual(
            salida(p.vacaciones_del_ejercicio, "F", 60), "Andá de vacaciones\n"
        )
        self.assertEqual(
            salida(p.vacaciones_del_ejercicio, "M", 60), "Te toca trabajar\n"
        )

    def test_while_for_equivalentes(self):
        for a, b, args in [
            (p.uno_a_diez, p.uno_a_diez_for, ()),
            (p.eco, p.eco_for, ()),
            (p.viajar, p.viajar_for, (2025, 2022)),
            (p.viaje_aristoteles, p.viaje_aristoteles_for, (2025,)),
        ]:
            self.assertEqual(salida(a, *args), salida(b, *args))
        for modulo in (guia6, alcance_variables):
            self.assertEqual(salida(modulo.cuenta_regresiva, 3), "3\n2\n1\nDespegue\n")
            self.assertEqual(
                salida(modulo.cuenta_regresiva_v2, 3), "3\n2\n1\nDespegue\n"
            )
            self.assertEqual(
                salida(modulo.imprimir_numeros_pares_entre_10_40),
                salida(modulo.imprimir_numeros_pares_entre_10_40_v2),
            )

    def test_alcance(self):
        p.g = 0
        self.assertEqual([p.ro(1) for _ in range(3)], [2, 3, 4])
        self.assertEqual([p.rt(1, 0) for _ in range(3)], [2, 2, 2])
        self.assertEqual(p.g, 3)
