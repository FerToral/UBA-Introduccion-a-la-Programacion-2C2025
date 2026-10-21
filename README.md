# Introducción a la Programación · UBA

## Segundo cuatrimestre de 2025

Prácticas de Exactas: razonamiento sobre programas, programación funcional con Haskell y programación imperativa con Python. Las guías conservan sus actividades, contratos, código y pruebas en una misma carpeta.

## Recorrido

| Etapa                  | Guías                                                                                                                                                              |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Fundamentos            | [1 · Lógica](Guias/Guia-01), [2 · Especificación](Guias/Guia-02)                                                                                                   |
| Funcional              | [3 · Introducción a Haskell](Guias/Guia-03), [4 · Recursión sobre enteros](Guias/Guia-04), [5 · Listas y matrices](Guias/Guia-05), [tipo parcial](Guias/Guia-05-1) |
| Imperativa             | [6 · Funciones y control](Guias/Guia-06), [7 · Listas y matrices](Guias/Guia-07), [8 · TAD, diccionarios y archivos](Guias/Guia-08)                                |
| Validación y análisis  | [9 · Caja blanca](Guias/Guia-09), [10 · Integradora](Guias/Guia-10), [11 · Complejidad](Guias/Guia-11)                                                             |
| Preparación de parcial | [Simulacro funcional](Parciales/Simulacro-Funcional)                                                                                                               |

El TP tiene su propio historial y repositorio: [Batalla Naval · 2C2025](https://github.com/FerToral/UBA-Batalla-Naval-2C2025).

Las guías 1–11 incluyen respuestas, contratos y comprobaciones. El taller
específico de debugging está restaurado en el respaldo local; su plantilla,
tests y poemas docentes no se redistribuyen aquí sin permiso. Este recorrido
no reemplaza el material oficial ni una corrección docente. La procedencia
de las respuestas personales y los desarrollos posteriores está en [créditos](CREDITOS.md).

## Ejecutar

Comprobado con Python3.12 y GHC9.8.2, sin dependencias Python obligatorias. Desde la raíz:

```shell
python herramientas/comprobar.py
```

Se pueden ejecutar los bloques por separado:

```shell
python herramientas/comprobar.py --python
python herramientas/comprobar.py --haskell
```

Si GHC no está en PATH, indicar `--runghc /ruta/a/runghc`. El bloque Haskell desactiva entornos de paquetes personales y sólo utiliza bibliotecas de GHC.

## Estudiar una práctica

1. Leer la descripción y precondiciones de su carpeta.
2. Abrir el módulo de código e identificar el ejercicio.
3. Ejecutar las pruebas y contrastar los casos límite.
4. Para consola, abrir GHCi o importar el módulo Python de esa guía.

Las funciones homónimas de guías distintas no se mezclan: cada módulo tiene su ámbito y las pruebas Python se ejecutan con rutas aisladas. Las entradas interactivas y el azar se simulan en los tests.

Programa y fuentes académicas: [campus 674](https://campus.exactas.uba.ar/course/view.php?id=674). Las descripciones locales relacionan teoría y actividad sin depender exclusivamente de ese acceso.
