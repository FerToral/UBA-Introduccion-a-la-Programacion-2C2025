import csv
from pathlib import Path
import tempfile
import unittest
import archivos as a


class Archivos(unittest.TestCase):
    def setUp(self):
        self.carpeta = tempfile.TemporaryDirectory()
        self.addCleanup(self.carpeta.cleanup)
        self.entrada = str(Path(self.carpeta.name) / "entrada.txt")
        self.salida = str(Path(self.carpeta.name) / "salida.txt")

    def test_lectura_y_frecuencia(self):
        Path(self.entrada).write_text("banana ana\nx x", encoding="utf-8")
        self.assertEqual(a.contar_lineas(self.entrada), 2)
        self.assertTrue(a.existe_palabra(self.entrada, "ana"))
        self.assertEqual(a.cantidad_de_apariciones(self.entrada, "ana"), 3)
        self.assertEqual(a.agrupar_por_longitud(self.entrada), {6: 1, 3: 1, 1: 2})
        self.assertEqual(a.la_palabra_mas_frecuente(self.entrada), "x")
        with self.assertRaises(ValueError):
            a.existe_palabra(self.entrada, "")

    def test_clonar_e_invertir_sin_ultima_nueva_linea(self):
        Path(self.entrada).write_text(
            "# uno\n  # dos\ntexto # conservar\nfin", encoding="utf-8"
        )
        a.clonar_sin_comentarios(self.entrada, self.salida)
        self.assertEqual(
            Path(self.salida).read_text(encoding="utf-8"), "texto # conservar\nfin"
        )
        a.invertir_lineas(self.salida, self.salida)
        self.assertEqual(
            Path(self.salida).read_text(encoding="utf-8"), "fin\ntexto # conservar\n"
        )

    def test_frases(self):
        Path(self.entrada).write_text("original", encoding="utf-8")
        a.agregar_frase_al_final(self.entrada, "final")
        a.agregar_frase_al_principio(self.entrada, "inicio")
        self.assertEqual(
            Path(self.entrada).read_text(encoding="utf-8"), "inicio\noriginal\nfinal\n"
        )

    def test_binario(self):
        Path(self.entrada).write_bytes(b"\x00abc\x01hello_world\xff12345")
        self.assertEqual(
            a.listar_textos_de_archivo(self.entrada), ["hello_world", "12345"]
        )

    def test_csv_solo_ficticio(self):
        Path(self.entrada).write_text(
            'demo-A,"Materia, I",2025-01-01,8\ndemo-B,B,2025-01-01,6\ndemo-A,A,2025-02-01,10\n',
            encoding="utf-8",
        )
        a.calcular_promedio_por_estudiante(self.entrada, self.salida)
        with open(self.salida, encoding="utf-8", newline="") as archivo:
            self.assertEqual(
                list(csv.reader(archivo)), [["demo-A", "9.0"], ["demo-B", "6.0"]]
            )
        with self.assertRaises(ValueError):
            a.calcular_promedio_por_estudiante(self.entrada, self.entrada)

    def test_vacios(self):
        Path(self.entrada).write_text("", encoding="utf-8")
        self.assertEqual(a.contar_lineas(self.entrada), 0)
        self.assertEqual(a.agrupar_por_longitud(self.entrada), {})
        with self.assertRaises(ValueError):
            a.la_palabra_mas_frecuente(self.entrada)
