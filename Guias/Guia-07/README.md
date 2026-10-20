# Guía 7 · Listas, cadenas y matrices

[guia7.py](src/guia7.py) conserva las respuestas personales de recorridos; [practicas7.py](src/practicas7.py) completa filtrado, matrices y programas interactivos. [Pruebas](tests).

| Bloque | Actividades y contratos |
|---|---|
| 1.1–8 | Tres búsquedas de pertenencia, divisibilidad universal, suma/máximo/mínimo sin equivalentes nativos, orden estricto, primer máximo y último mínimo (−1 en vacío). |
| 1.9–14 | Palabra de más de siete caracteres, palíndromo, tres iguales consecutivos, tres vocales distintas, inicio de la racha ordenada más larga y conteo de cifras impares. |
| 2.1–6 | Poner ceros en índices pares inout o en una copia; quitar/reemplazar vocales; invertir texto y eliminar caracteres repetidos conservando la primera aparición. |
| 3–4 | Estado de materia:1 promoción,2 final,3 desaprobación; ingresos/retiros con saldo inicial0. |
| 5 | Pertenencia por fila: dos variantes con parámetro de salida y una con retorno. El resultado de tamaño exacto satisface también el contrato más débil que admite tamaño mayor. |
| 6.1–6 | Matriz no vacía rectangular; filas/columnas estrictamente ordenadas; extraer columna, transponer y Ta-Te-Ti3×3. O→0, X→1, sin ganador→2. |
| 6.7 opcional | Producto y potencia de una matriz aleatoria con semilla, d,p>0; biblioteca estándar, sin dependencia obligatoria de NumPy. |
| 7.1–4 | Entrada de nombres hasta listo/vacío, historial de monedero, siete y medio y clasificación de una cadena por las reglas de la guía. |

## Precisiones

La racha del ejercicio1.13 es **no decreciente** (≤), aunque el predicado ordenados del1.6 es estricto (<). En empate se elige la primera racha. La búsqueda de palabras y ternas incluye el último elemento: se sigue la descripción, corrigiendo los límites incompletos del PDF.

Vocales son a/e/i/o/u minúsculas en estos ejercicios. Las posiciones pares empiezan en0. El máximo requiere secuencia no vacía; la suma del vacío vale0. Una transposición rectangular conserva todas las celdas.

En la guía se describe el parámetro de salida de filas_ordenadas con una firma distinta de la función histórica, que devuelve la lista: se conserva esa API de retorno y su significado por fila.

## Programas interactivos

- Nombres: devuelve los ingresados, sin el terminador.
- Monedero: guarda C/D y monto positivo; permite un saldo negativo porque la consigna no exige un límite de crédito.
- Siete y medio: cartas1…7 y10…12; figuras valen0.5. Se sigue la nota final del enunciado (no se agrega una carta0). Devuelve el historial, informa pérdida si supera7.5 y permite plantarse.
- Fortaleza: ROJA si longitud<5; VERDE si longitud>8 y contiene minúscula ASCII, mayúscula ASCII y dígito; AMARILLA en otro caso. Es una clasificación didáctica, no una auditoría real de contraseñas.

Las pruebas simulan entradas y cartas para no depender del azar ni esperar interacción.

## Potencias y costo

Multiplicar matrices cuadradas cuesta Θ(d³) en el algoritmo elemental; repetir p−1 productos cuesta Θ(p·d³), además de crecer los enteros. No se usan productos elemento a elemento. El helper multiplicar_matrices permite contrastar potencias pequeñas.

Fuente: guía7 alojada en campus674 durante2C2025; el PDF conserva fecha de compilación22/05/2025. Teoría de secuencias, parámetros in/out y matrices. No se cambia la edición del curso por la fecha del PDF.

Desde la raíz: `python herramientas/comprobar.py --python`.
