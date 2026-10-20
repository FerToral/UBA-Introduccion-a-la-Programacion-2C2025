import contextlib
import io
import importlib.util
import unittest
from queue import LifoQueue as Pila
from queue import Queue as Cola
from pathlib import Path


SRC = Path(__file__).parents[1] / "src" / "guia8.py"
spec = importlib.util.spec_from_file_location("guia8", SRC)
guia8 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(guia8)


def pila_desde_tope(elementos):
    pila = Pila()
    for elemento in reversed(elementos):
        pila.put(elemento)
    return pila


def pila_a_tope(pila):
    salida = []
    while not pila.empty():
        salida.append(pila.get())
    for elemento in reversed(salida):
        pila.put(elemento)
    return salida


def cola_desde(elementos):
    cola = Cola()
    for elemento in elementos:
        cola.put(elemento)
    return cola


def cola_a_lista(cola):
    salida = []
    while not cola.empty():
        salida.append(cola.get())
    for elemento in salida:
        cola.put(elemento)
    return salida


class Guia8Tests(unittest.TestCase):
    def test_importar_no_imprime(self):
        salida = io.StringIO()
        with contextlib.redirect_stdout(salida):
            spec.loader.exec_module(importlib.util.module_from_spec(spec))
        self.assertEqual(salida.getvalue(), "")

    def test_pilas_cuentan_maximo_y_restauran(self):
        pila = pila_desde_tope([-4, -9, -1])
        original = [-4, -9, -1]
        self.assertEqual(guia8.cantidad_elementos(pila), 3)
        self.assertEqual(guia8.buscar_el_maximo(pila), -1)
        self.assertEqual(pila_a_tope(pila), original)

    def test_nota_maxima_y_balanceo(self):
        pila = pila_desde_tope([("Ana", 7), ("Beto", 10), ("Cata", 8)])
        self.assertEqual(guia8.buscar_nota_maxima(pila), ("Beto", 10))
        self.assertTrue(guia8.esta_bien_balanceada("1 + (2 * (3 + 4))"))
        self.assertFalse(guia8.esta_bien_balanceada("1 + ) 2 ("))

    def test_postfix_y_pilas_intercaladas(self):
        self.assertEqual(guia8.evaluar_expresion("3 4 + 5 * 2 -"), 33)
        p1 = pila_desde_tope([1, 2, 3])
        p2 = pila_desde_tope([10, 20, 30])
        resultado = guia8.intercalar_pilas(p1, p2)
        self.assertEqual(pila_a_tope(resultado), [10, 1, 20, 2, 30, 3])
        self.assertEqual(pila_a_tope(p1), [1, 2, 3])
        self.assertEqual(pila_a_tope(p2), [10, 20, 30])

    def test_colas_basicas_y_minimo(self):
        cola = cola_desde([("Ana", 7), ("Beto", 3), ("Cata", 9)])
        self.assertEqual(guia8.tam(cola), 3)
        self.assertEqual(guia8.buscar_el_maximov2(cola), ("Cata", 9))
        self.assertEqual(guia8.buscar_nota_minima(cola), ("Beto", 3))
        self.assertEqual(cola_a_lista(cola), [("Ana", 7), ("Beto", 3), ("Cata", 9)])

    def test_colas_intercaladas_y_generacion(self):
        c1, c2 = cola_desde([1, 2]), cola_desde([10, 20])
        resultado = guia8.intercalar_colas(c1, c2)
        self.assertEqual(cola_a_lista(resultado), [1, 10, 2, 20])
        self.assertEqual(cola_a_lista(c1), [1, 2])
        self.assertEqual(cola_a_lista(c2), [10, 20])
        generado = guia8.generar_nros_al_azarv2(20, 6, 9)
        valores = cola_a_lista(generado)
        self.assertEqual(len(valores), 20)
        self.assertTrue(all(6 <= valor <= 9 for valor in valores))

    def test_bingo_100_unicos_y_restauracion(self):
        bolillero = guia8.armar_secuencia_bingo()
        valores = cola_a_lista(bolillero)
        self.assertEqual(len(valores), 100)
        self.assertEqual(set(valores), set(range(100)))
        carton = valores[0:12]
        self.assertEqual(
            guia8.jugar_carton_de_bingo(carton, bolillero),
            max(valores.index(valor) for valor in carton) + 1,
        )
        self.assertEqual(cola_a_lista(bolillero), valores)

    def test_urgentes_clientes_y_diccionarios(self):
        pacientes = cola_desde([(1, "A", "x"), (4, "B", "y"), (3, "C", "z")])
        self.assertEqual(guia8.pacientes_urgentes(pacientes), 2)
        clientes = cola_desde(
            [
                ("resto", 1, False, False),
                ("pref", 2, True, False),
                ("prior", 3, False, True),
                ("prior2", 4, True, True),
            ]
        )
        salida = guia8.atencion_a_clientes(clientes)
        self.assertEqual(
            cola_a_lista(salida),
            [
                ("prior", 3, False, True),
                ("prior2", 4, True, True),
                ("pref", 2, True, False),
                ("resto", 1, False, False),
            ],
        )
        notas = [("Sole", 9.5), ("Maxi", 8.0), ("Sole", 9.0)]
        self.assertEqual(guia8.promedio(notas, "Sole"), 9.25)
        self.assertEqual(
            guia8.calcular_promedio_por_estudiante(notas), {"Sole": 9.25, "Maxi": 8.0}
        )

    def test_historial_e_inventario(self):
        historiales = {}
        guia8.visitar_sitio(historiales, "u", "a")
        guia8.visitar_sitio(historiales, "u", "b")
        self.assertEqual(guia8.navegar_atras(historiales, "u"), "b")
        inventario = {}
        guia8.agregar_producto(inventario, "Camisa", 20.0, 50)
        guia8.agregar_producto(inventario, "Pantalon", 30.0, 30)
        guia8.actualizar_stock(inventario, "Camisa", 10)
        self.assertEqual(guia8.calcular_valor_inventario(inventario), 1100.0)


if __name__ == "__main__":
    unittest.main()
