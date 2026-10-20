import copy
from itertools import product
from queue import Queue
import unittest
import integradora as g


def cola(xs):
    q = Queue()
    for x in xs:
        q.put(x)
    return q


def lista(q):
    res = []
    for _ in range(q.qsize()):
        res.append(q.get())
    for x in res:
        q.put(x)
    return res


class Integradora(unittest.TestCase):
    def test_stock(self):
        self.assertEqual(
            g.stock_productos([("a", 4), ("a", 0), ("b", 2), ("a", 7)]),
            {"a": (0, 7), "b": (2, 2)},
        )
        self.assertEqual(g.stock_productos([]), {})

    def test_codigos(self):
        self.assertEqual(
            g.filtrar_codigos_primos([1101, 1002, 1011, 1100, -1003]),
            [1101, 1002, 1011, -1003],
        )

    def test_pacientes(self):
        self.assertEqual(
            g.subsecuencia_mas_larga(["ave", "perro", "gato", "pez", "gato", "perro"]),
            1,
        )
        self.assertEqual(g.subsecuencia_mas_larga(["perro"]), 0)

    def test_turnos(self):
        grilla = [["Ana", "A"]] * 4 + [
            ["Beto", "B"],
            ["Beto", "B"],
            ["Beto", "C"],
            ["Beto", "B"],
        ]
        self.assertEqual(
            g.un_responsable_por_turno(grilla), [(True, True), (True, False)]
        )

    def test_promedios(self):
        self.assertEqual(
            g.promedio_de_salidas({"A": [0, 61, 60, 30], "B": [0, 61, 0, 61]}),
            {"A": (2, 45.0), "B": (0, 0.0)},
        )

    def test_rapido(self):
        self.assertEqual(g.tiempo_mas_rapido([0, 61, 20, 20, 60]), 2)

    def test_rachas_exhaustivas(self):
        for n in range(1, 7):
            for xs in product((0, 1, 61), repeat=n):
                if 1 not in xs:
                    continue
                candidatos = [
                    (a, b)
                    for a in range(n)
                    for b in range(a, n)
                    if all(x == 1 for x in xs[a : b + 1])
                ]
                esperado = max(candidatos, key=lambda ab: (ab[1] - ab[0], -ab[0]))
                self.assertEqual(g.racha_mas_larga(list(xs)), esperado)

    def test_solitario(self):
        self.assertEqual(
            g.escape_en_solitario([[0, 0, 61, 0], [0, 0, 0, 0], [0, 0, 1, 0]]), [0, 2]
        )

    def test_gallinas(self):
        d, f = "me desvío siempre", "me la banco y no me desvío"
        self.assertEqual(
            g.torneo_de_gallinas({"a": d, "b": f, "c": f}), {"a": -30, "b": 5, "c": 5}
        )
        self.assertEqual(g.torneo_de_gallinas({"a": d, "b": d}), {"a": -10, "b": -10})
        self.assertEqual(g.torneo_de_gallinas({"a": f, "b": f}), {"a": -5, "b": -5})

    def test_vips_nombres_y_preservacion(self):
        entrada = [
            ("Ana", "común"),
            ("Beto", "vip"),
            ("Cami", "vip"),
            ("Dani", "común"),
        ]
        q = cola(entrada)
        self.assertEqual(
            lista(g.reordenar_cola_priorizando_vips(q)), ["Beto", "Cami", "Ana", "Dani"]
        )
        self.assertEqual(lista(q), entrada)
        self.assertEqual(lista(g.reordenar_cola_priorizando_vips(cola([]))), [])

    def test_sufijos(self):
        self.assertEqual(g.cuantos_sufijos_son_palindromos("ababa"), 3)
        self.assertEqual(g.cuantos_sufijos_son_palindromos(""), 0)

    def test_tateti(self):
        for x, o, esperado in [
            (False, False, 0),
            (True, False, 1),
            (False, True, 2),
            (True, True, 3),
        ]:
            t = [[" "] * 5 for _ in range(5)]
            if x:
                for i in range(3):
                    t[i][0] = "X"
            if o:
                for i in range(3):
                    t[i][1] = "O"
            # Equilibrar turnos sin introducir otra terna vertical.
            if x and not o:
                t[3][2] = t[4][3] = "O"
            if o and not x:
                t[0][3] = t[1][4] = t[4][2] = "X"
            antes = copy.deepcopy(t)
            self.assertEqual(g.quien_gano_el_tateti_facilito(t), esperado)
            self.assertEqual(t, antes)

    def test_atencion_preserva_colas(self):
        u, p = cola([1, 2]), cola([3, 4])
        self.assertEqual(lista(g.orden_de_atencion(u, p)), [1, 3, 2, 4])
        self.assertEqual(lista(u), [1, 2])
        self.assertEqual(lista(p), [3, 4])
        self.assertEqual(lista(g.orden_de_atencion(cola([]), cola([]))), [])

    def test_epidemiologia(self):
        self.assertEqual(
            g.alarma_epidemiologica(
                [(1, "a"), (2, "b"), (3, "a"), (1, "c")], ["a", "b"], 0.5
            ),
            {"a": 0.5},
        )
        self.assertEqual(g.alarma_epidemiologica([], ["a"], 0.5), {})

    def test_empleados(self):
        self.assertEqual(g.empleados_del_mes({1: [4, 4], 2: [8], 3: [1]}), [1, 2])
        self.assertEqual(g.empleados_del_mes({}), [])

    def test_ocupacion(self):
        self.assertEqual(
            g.nivel_de_ocupacion(
                [[True, False, True], [False, False, True], [True] * 3]
            ),
            [2 / 3, 1 / 3, 1.0],
        )
