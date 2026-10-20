# Guía 5 · Recursión sobre listas

[Guia05.hs](src/Guia05.hs) reúne los ejercicios 1–7; [Matrices.hs](src/Matrices.hs), el ejercicio 8. Separar módulos permite conservar las dos funciones llamadas `contarPalabras`, que tienen contratos diferentes.

| Ejercicio | Actividades |
|---|---|
| 1 | Longitud, último, principio y reverso. Último/principio requieren lista no vacía. |
| 2 | Pertenencia, igualdad global, elementos distintos/repetidos, quitar una/todas las apariciones, deduplicar, igualdad de conjuntos y capicúa. |
| 3 | Suma/producto, máximo no vacío, sumar a cada elemento, sumar primero/último, pares, múltiplos de divisor no nulo y orden creciente con repeticiones. |
| 4 | Colapsar espacios, separar/contar palabras, palabra más larga, concatenar y unir con uno o n espacios. n≥0. |
| 5 | Sumas de prefijos y factores primos con multiplicidad. Se admite 2, incluido por el ejemplo del PDF aunque el requiere diga “mayores a 2”. |
| 6 | Agenda: consultar, agregar/actualizar y eliminar por nombre; auxiliares nombre/teléfono. Los nombres son únicos. |
| 7 | Lockers: existencia, ubicación, disponibilidad y ocupación; **True significa libre**. Consultar u ocupar requiere un identificador existente; ocupar requiere que esté libre. |
| 8.1–4 | Suma matricial, contar un entero, contar una palabra exacta y conteo polimórfico. |
| 8.5–6 | Producto por escalar preservando dimensiones y concatenación de cada fila de textos. |
| 8.7–10 | Fila, columna, identidad y pares de una columna; índices **desde cero**. Matrices rectangulares no vacías. |

## Decisiones de los contratos

Las listas vacías tienen suma 0, producto 1 y cumplen “todos iguales/distintos” vacíamente. Quitar elimina sólo la primera aparición; deduplicar conserva la primera. `mismosElementos` ignora multiplicidades, mientras ordenar las conserva.

Un blanco es el carácter espacio. La separación ignora espacios iniciales/finales; colapsar conserva uno en cada borde si lo había. La palabra más larga requiere al menos una palabra; en empate se elige la primera. `Texto` es un alias, no un tipo nuevo: las firmas de caracteres pueden usarlo sin cambiar implementación.

La selección repetida del máximo es O(n²). Reverso por concatenación también es cuadrático: se conserva la construcción recursiva elemental del ejercicio.

Fuente: guía 5 del campus 674, compilada el 20/09/2025; teórico de listas y recursión estructural. Pruebas: `python herramientas/comprobar.py --haskell`.
