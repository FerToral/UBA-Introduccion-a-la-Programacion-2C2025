"""Ejecuta cada guía de forma aislada desde cualquier directorio."""

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys

RAIZ = Path(__file__).resolve().parents[1]


def ejecutar(comando, entorno=None):
    subprocess.run(comando, cwd=RAIZ, env=entorno, check=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--haskell", action="store_true", help="Sólo el bloque funcional"
    )
    parser.add_argument(
        "--python", action="store_true", help="Sólo el bloque imperativo"
    )
    parser.add_argument(
        "--runghc",
        default=shutil.which("runghc"),
        help="Ruta a runghc si no está en PATH",
    )
    args = parser.parse_args()
    if args.haskell and args.python:
        parser.error("Elegir una sección o no indicar ninguna para ejecutar ambas")
    if not args.haskell:
        for guia in sorted((RAIZ / "Guias").glob("Guia-*")):
            if not (guia / "tests").is_dir():
                continue
            env = os.environ.copy()
            env["PYTHONPATH"] = str(guia / "src")
            ejecutar(
                [
                    sys.executable,
                    "-m",
                    "unittest",
                    "discover",
                    "-s",
                    str(guia / "tests"),
                    "-p",
                    "test_*.py",
                ],
                env,
            )
    if not args.python:
        if not args.runghc:
            parser.error("Instalar GHC y agregar runghc a PATH, o indicar --runghc")
        ejecutar(
            [
                args.runghc,
                "-package-env",
                "-",
                "-iGuias/Guia-03/src",
                "-iGuias/Guia-04/src",
                "-iGuias/Guia-05/src",
                "-iGuias/Guia-05-1/src",
                "-iParciales/Simulacro-Funcional/src",
                "pruebas/Haskell.hs",
            ]
        )
