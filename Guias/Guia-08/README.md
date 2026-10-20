# Guía 8 · Pilas, colas, diccionarios y archivos

[guia8.py](src/guia8.py) contiene los ejercicios1–18; [archivos.py](src/archivos.py),19–27. [Pruebas](tests).

| Actividades | Contenido |
|---|---|
| 1–4 | Pila aleatoria, tamaño sin qsize, máximo y tupla con nota máxima; las consultas restauran la entrada. |
| 5–7 | Paréntesis balanceados mediante pila; expresiones postfijas con enteros y + − * /; intercalación con tope de la segunda pila. Entradas de igual tamaño. |
| 8–12 | Equivalentes con cola: azar, tamaño sin qsize, máximo, nota mínima e intercalación comenzando por la primera cola. |
| 13 | Bolillero con los cien valores0…99 sin repetir; mínimo de extracciones para completar un cartón de doce números. Se conserva el bolillero de entrada. |
| 14–15 | Prioridad hospitalaria menor que4; atención bancaria estable: prioridad personal, luego cuenta preferencial y luego resto. |
| 16 | Diccionario de promedios por nombre; no confundir la función en memoria con la exportación CSV del27. |
| 17–18 | Historial por usuario mediante pilas e inventario anidado con precio/cantidad, actualización y valoración total. |
| 19 | Cantidad de líneas; existencia y conteo de una secuencia literal no vacía. Se cuentan también coincidencias solapadas. |
| 20–21 | Agrupar palabras por longitud y palabra más frecuente; tokens delimitados por blancos, sin normalizar puntuación/mayúsculas. Empate por primera aparición. |
| 22–23 | Clonar omitiendo comentarios de línea completa e invertir el orden de líneas. |
| 24–25 | Agregar una frase de una sola línea al final o al principio del archivo original. |
| 26 | Extraer secuencias ASCII de letras, dígitos, espacios o guion bajo, de longitud≥5, desde bytes. |
| 27 | CSV de cuatro columnas LU,materia,fecha,nota → CSV LU,promedio. Sin encabezado; lector CSV admite campos entrecomillados. |

## Archivos y datos

El texto se procesa como UTF-8. En comentarios sólo se admiten espacios antes de #; un # posterior a texto se conserva. Invertir líneas escribe separadores LF y evita pegar dos líneas cuando la última no tenía salto final. Agregar al final crea el separador que falte; no agrega una línea vacía innecesaria.

La exportación de promedios rechaza entrada/salida iguales antes de escribir. Todos los tests de archivos operan en un directorio temporal con datos ficticios: no leen evaluaciones de estudiantes reales ni binarios del equipo.

## Tipos abstractos

Se emplean Queue/LifoQueue de la biblioteca estándar. Las operaciones in restauran el contenido y orden; las inout modifican sólo lo especificado. Máximos/notas requieren estructura no vacía. La ejecución es secuencial, sin consumidores concurrentes.

Fuente: guía8 del campus674, compilada14/10/2025; teoría vinculada: TAD, diccionarios, entrada/salida y debugging. El PDF docente permanece en respaldo; las descripciones locales permiten seguir las actividades sin iniciar sesión.

Desde la raíz: `python herramientas/comprobar.py --python`.
