from itertools import product
import unittest
import logica as l

V, F, I = l.V, l.F, l.I


class Logica(unittest.TestCase):
    def test_sintaxis_de_la_teorica(self):
        candidatos = [
            "(p¬q)",
            "p∨q∧True",
            "(p→¬p→q)",
            "¬(p)",
            "(p∨¬p∧q)",
            "(True∧True∧True)",
            "(¬p)",
            "(p∨False)",
            "(p=q)",
        ]
        validos = []
        for indice, formula in enumerate(candidatos):
            try:
                l.analizar(formula)
                validos.append(indice)
            except ValueError:
                pass
        self.assertEqual(validos, [5, 7])

    def test_clasificacion_y_leyes(self):
        esperado = {
            "a": "VVVV",
            "b": "FFFF",
            "c": "VVVV",
            "d": "VVFV",
            "e": "VVVV",
            "f": "VFVF",
            "g": "VVVV",
            "h": "VVVV",
            "i": "V" * 8,
            "j": "V" * 8,
        }
        for inciso, formula in l.EJERCICIO3.items():
            variables = ("p", "q", "r") if inciso in "ij" else ("p", "q")
            self.assertEqual(l.columna(formula, variables), esperado[inciso])
        self.assertEqual(len(l.LEYES), 22)
        for a, b in l.LEYES.values():
            self.assertTrue(l.equivalentes(a, b, ("p", "q", "r")))

    def test_simplificaciones_y_equivalencias(self):
        simplificaciones = [
            ("((p∧p)∨p)", "p"),
            ("¬(¬p∨¬q)", "(p∧q)"),
            ("(((p∧(¬p∨q))∨q)∨(p∧(p∨q)))", "(p∨q)"),
            ("(¬p→¬(p→¬q))", "p"),
            ("(((p→q)∧(p∧¬q))→q)", "True"),
            ("¬((¬(p∧q)∨(p∨q))→(¬¬p∨¬p))", "False"),
        ]
        for a, b in simplificaciones:
            self.assertTrue(l.equivalentes(a, b, ("p", "q")))
        pares = [
            ("(((p∧p)∧p)→p)", "True"),
            ("(((¬p∨¬q)∨(p∧q))→(p∧q))", "(p∧q)"),
            ("((p∨q)∧(p∨r))", "(¬p→(q∧r))"),
            ("(¬¬p→¬(¬p∧¬q))", "q"),
            ("(((True∧p)∧(¬p∨False))→¬(¬p∨q))", "(p∧¬q)"),
            ("(p∨(¬p∧q))", "(¬p→q)"),
            ("¬(p∧(q∧s))", "(s→(¬p∨¬q))"),
            ("(p→(q∧¬(q→r)))", "((¬p∨q)∧(¬p∨(q∧¬r)))"),
        ]
        self.assertEqual(
            [l.equivalentes(a, b, ("p", "q", "r", "s")) for a, b in pares],
            [True, True, True, False, False, True, True, True],
        )

    def test_tablas_ternarias_y_cortocircuito(self):
        for a, b in product((V, F, I), repeat=2):
            env = {"p": a, "q": b}
            for op in ("∧", "∨", "→"):
                estricto = l.evaluar(l.analizar("(p" + op + "q)"), env)
                secuencial = l.evaluar(l.analizar("(p" + op + "Lq)"), env)
                if a is I or b is I:
                    self.assertIs(estricto, I)
                if a is I:
                    self.assertIs(secuencial, I)
        self.assertIs(l.evaluar(l.analizar("(p∧Lq)"), {"p": F}), F)
        self.assertIs(l.evaluar(l.analizar("(p∨Lq)"), {"p": V}), V)
        self.assertIs(l.evaluar(l.analizar("(p→Lq)"), {"p": F}), V)

    def test_ejercicio17(self):
        formulas = [
            "(¬x∨Lb)",
            "((c∨L(y∧La))∨Lb)",
            "¬(c∨Ly)",
            "(¬(c∨Ly)↔(¬c∧L¬y))",
            "((c∨Ly)∧L(a∨Lb))",
            "(((c∨Ly)∧L(a∨Lb))↔((c∨L(y∧La))∨Lb))",
            "(¬c∧L¬y)",
        ]
        env = dict(a=F, b=V, c=V, x=I, y=I)
        self.assertEqual(
            [l.evaluar(l.analizar(x), env) for x in formulas], [I, V, F, V, V, V, F]
        )

    def test_ejercicio18(self):
        # Constantes aritméticas calculadas en R; log0 se representa por I.
        formulas = [
            "(True∧Lp)",
            "(False→L(p∧Lq))",
            "(True→L(True∨Lr))",
            "(False∨L(r∧L(q∧Lp)))",
            "((p∧Lq)∧Lr)",
            "((p∨Lq)∨Lr)",
            "((p∧Lr)∧L((q→Lq)∨L(p→L(q∧Lr))))",
            "((p∧L¬q)→LFalse)",
            "(p∧L(False↔False))",
            "(¬(p∨Lr)→Lr)",
            "((p→Lu)↔(True∧L(p∧L¬q)))",
            "((p→L(q→Lr))→L((p→Lq)→L(p→Lr)))",
        ]
        env = dict(p=V, q=F, r=I, u=I)
        self.assertEqual(
            [l.evaluar(l.analizar(x), env) for x in formulas],
            [V, V, V, I, F, V, I, F, V, V, I, V],
        )

    def test_ejercicio19_seis_valuaciones_admisibles(self):
        formulas = [
            "(p∨Lq∨L(¬q∧Lr))",
            "¬(p∨Lq∨L(¬q∧Lr))",
            "((p∧L¬q∧L¬(¬q∧Lr))∨L(¬p∧Lq∧L¬(¬q∧Lr))∨L(¬p∧L¬q∧L(¬q∧Lr)))",
            "(p∧Lq∧L¬(¬q∧Lr))",
            "¬(p∧Lq∧L(¬q∧Lr))",
            "((p∨L¬p)∧L(¬q∧Lr))",
        ]
        for p, q in product((V, F), repeat=2):
            for r in (I,) if q is V else (V, F):
                env = dict(p=p, q=q, r=r)
                cantidad = sum(x is V for x in (p, q, r))
                esperado = [
                    cantidad > 0,
                    cantidad == 0,
                    cantidad == 1,
                    p is V and q is V,
                    cantidad < 3,
                    r is V,
                ]
                obtenido = [l.evaluar(l.analizar(x), env) for x in formulas]
                self.assertNotIn(I, obtenido)
                self.assertEqual(obtenido, [V if x else F for x in esperado])

    def test_razonamientos(self):
        premisas = "((f→((e∨m)∧¬(e∧m)))∧(¬f→¬e)∧((f∧e)→m))"
        self.assertEqual(l.columna("(" + premisas + "→¬e)", ("f", "e", "m")), "V" * 8)
        self.assertEqual(
            l.columna("(((p→q)∧(p→(q→r)))→(p→r))", ("p", "q", "r")), "V" * 8
        )
        self.assertFalse(l.equivalentes("((p→q)∧q)", "p", ("p", "q")))

    def test_variables_de_las_tablas_no_inventan_r_por_true(self):
        texto = l.tablas_equivalencias()
        primera = texto.split("## b")[0]
        self.assertNotIn("| p | r |", primera)
        self.assertIn("| p | Izquierda | Derecha |", primera)
        segunda = texto.split("## b")[1].split("## c")[0]
        self.assertNotIn("| p | r |", segunda)
