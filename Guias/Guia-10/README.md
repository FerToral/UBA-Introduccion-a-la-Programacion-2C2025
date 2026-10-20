# Guía 10 · Integradora Python

Dieciséis actividades que combinan recorridos, matrices, diccionarios y colas. [Código](src/integradora.py) y [pruebas](tests/test_integradora.py).

| Ejercicio | Consigna y decisiones |
|---|---|
| 1 | Extremos de stock por producto: diccionario producto→(mínimo,máximo), incluyendo todos los registros. Cantidades no negativas. Se corrige la errata del tipo de retorno del PDF. |
| 2 | Conservar códigos cuyos tres últimos dígitos formen un primo; 002 significa 2, no se descarta por los ceros. Códigos distintos con al menos tres cifras; para negativos se leen las cifras del valor absoluto. |
| 3 | Inicio de la racha más larga de perros/gatos; primera en empate. Debe existir alguno. |
| 4 | Grilla de 8 filas y 1–7 días: igualdad de responsable en las primeras cuatro y últimas cuatro horas, independientemente. |
| 5 | Cantidad/promedio de salidas exitosas por persona: sólo tiempos 1…60. Cero=no visitó, 61=no escapó; sin éxitos da (0,0.0). |
| 6–7 | Índice de salida más rápida y extremos **inclusivos** de la mejor racha. Debe existir un éxito; empate a favor del primero. |
| 8 | Filas de cuatro amigos en las que únicamente el tercero asistió; también cuenta si tardó 61. |
| 9 | Torneo todos contra todos una vez. Ambos firmes: −5 cada uno; ambos se desvían: −10; mixto: +10 al firme y −15 al otro. Se conservan los dos textos de estrategia del enunciado. |
| 10 | Cola nueva de **nombres**, VIP primero; orden estable dentro de cada grupo y entrada preservada. La práctica antigua devolvía tuplas. |
| 11 | Contar sufijos palíndromos no vacíos, distinguiendo mayúsculas y signos. |
| 12 | Tablero cuadrado de 5–10 y turnos válidos: sólo ternas **verticales**. 0=ninguna, 1=X, 2=O, 3=ambas. No se infiere el historial de jugadas a partir de la foto final. |
| 13 | Intercalar urgentes/postergables de igual longitud y sin IDs repetidos, empezando por urgente; preservar ambas colas. |
| 14 | Proporción de registros por enfermedad infecciosa; incluirla si es **≥umbral**, como dice el contrato formal. El denominador son registros, no pacientes únicos. Extensión para entrada vacía: diccionario vacío. |
| 15 | Todos los empleados empatados en total máximo de horas. Jornadas no vacías; diccionario vacío devuelve lista vacía. |
| 16 | Proporción de camas ocupadas por piso; matriz rectangular no vacía y con al menos una cama. |

Promedios, ocupación y reordenamiento VIP proceden de la práctica personal recuperada. Se conservan los recorridos y se corrige la salida VIP. El resto completa las actividades de la guía.

Las colas se usan sin consumidores concurrentes; la restauración de su orden no ofrece garantías de concurrencia. Las funciones de consulta no modifican listas o matrices.

Fuente: guía integradora del campus 674, recurso 69817. Descripciones propias; original en respaldo académico.

Desde la raíz: `python herramientas/comprobar.py --python`.
