"""Gráfico opcional de los tiempos CSV; requiere matplotlib."""

import argparse
import csv
from pathlib import Path
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def graficar(origen: Path, destino: Path):
    series = {}
    with origen.open(encoding="utf-8", newline="") as archivo:
        for fila in csv.DictReader(archivo):
            if fila["estado"] == "medido":
                xs, ys = series.setdefault(fila["metodo"], ([], []))
                xs.append(int(fila["n"]))
                ys.append(float(fila["nanosegundos_por_llamada"]))
    fig, ax = plt.subplots(figsize=(8, 4.5), layout="constrained")
    for metodo, (xs, ys) in series.items():
        ax.loglog(xs, ys, marker="o", label=metodo)
    ax.set(
        xlabel="n (escala logarítmica)",
        ylabel="ns por llamada (escala logarítmica)",
        title="Sumatoria inclusiva · tiempos medidos",
    )
    ax.grid(alpha=0.2)
    ax.legend()
    fig.savefig(destino)
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", type=Path)
    parser.add_argument("salida", type=Path)
    args = parser.parse_args()
    graficar(args.csv, args.salida)
