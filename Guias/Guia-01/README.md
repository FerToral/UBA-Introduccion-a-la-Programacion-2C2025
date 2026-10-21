# Guía 1 · Lógica

Lógica proposicional, fuerza de fórmulas, indefinición y tipos. Fuente:
campus 674, recurso 63962 (p1.pdf, 19/08/2025), con semántica de la
teórica 2 del mismo2C2025. Resolución posterior, no entrega histórica.

[Calculadora](src/logica.py) · [pruebas](tests/test_logica.py).
Se usan V, F, I(indefinido). La calculadora no evalúa código Python de entrada.

## 1 · Sintaxis

Convención de análisis: conectores binarios o n-arios con al menos dos
operandos, sin una regla adicional de agrupación redundante. Con esta
lectura de la gramática de la teórica 2, sólo **f y h** están bien formadas.
a carece de conector; b carece de agrupación y mezcla operadores; c encadena
dos implicaciones sin anidar; d y g agregan paréntesis para los que no hay
regla de formación; e mezcla conjunción/disyunción sin anidación; i usa
igualdad, ajena a la sintaxis proposicional.

La gramática permite conjunciones o disyunciones n-arias homogéneas entre
paréntesis. No incluye una regla general “si A es fórmula,(A) lo es”.
Si se permiten n-arias de un solo operando o paréntesis redundantes,
**d y g también se admiten**. La diapositiva no explicita el límite n≥2;
por eso se distingue esta convención sintáctica de una corrección docente.
La calculadora usa la lectura estricta, no cambia el significado de las
fórmulas que se escriben con agrupación informal.

## 2 · Valuaciones

En el orden a–g, **ambas valuaciones** del enunciado dan:
V, V, F, V, V, V, F. Las sustituciones no hacen equivalentes todas las fórmulas
entre sí: sólo coinciden en estas dos entradas.

## 3 · Tablas y clasificación

Orden de filas de dos variables: VV, VF, FV, FF.

| Inciso | Columna final | Clasificación |
| ------ | ------------- | ------------- |
| a      | VVVV          | Tautología    |
| b      | FFFF          | Contradicción |
| c      | VVVV          | Tautología    |
| d      | VVFV          | Contingencia  |
| e      | VVVV          | Tautología    |
| f      | VFVF          | Contingencia  |
| g      | VVVV          | Tautología    |
| h      | VVVV          | Tautología    |
| i      | VVVVVVVV      | Tautología    |
| j      | VVVVVVVV      | Tautología    |

i y j usan p, q, r en el orden VVV, VVF, VFV, VFF, FVV, FVF, FFV, FFF.
La calculadora genera cada fila, no sólo la clasificación.

## 4–5 · Fuerza

A es al menos tan fuerte como B cuando A→B es tautología.

| Inciso | Relación                                                  |
| ------ | --------------------------------------------------------- |
| a      | False fuerza True, no al revés                            |
| b      | p∧q fuerza p∨q                                            |
| c      | Equivalentes                                              |
| d      | p∧q fuerza p                                              |
| e      | Equivalentes                                              |
| f      | p fuerza p∨q                                              |
| g      | Incomparables: p=V, q=F y p=F, q=V son contraejemplos     |
| h      | Incomparables: p=V, q=F y p=F, q=F refutan cada dirección |

False es la más fuerte y True la más débil. “Más fuerte” aquí incluye
equivalencia; no significa necesariamente “estrictamente más fuerte”.

## 6 · Equivalencias

Las leyes a–u, incluida ñ, se comprueban por sus tablas completas con
`python Guias/Guia-01/src/logica.py`.
Cada fila compara ambos lados: dominación, neutros, idempotencia,
complementos, doble negación, absorción, De Morgan, conmutatividad,
asociatividad, distributividad, contraposición e implicación/equivalencia
materiales. [Tablas de las 22 leyes](TABLAS_EQUIVALENCIAS.md).

## 7 · Simplificar, indicando reglas

- a: (p∧p)∨p ≡ p∨p ≡ p, por idempotencia dos veces.
- b: ¬(¬p∨¬q) ≡ ¬¬p∧¬¬q ≡ p∧q, por De Morgan y doble negación.
- c: p∧(¬p∨q) ≡ (p∧¬p)∨(p∧q) ≡ p∧q. Luego
  (p∧q)∨q ≡ q y p∧(p∨q) ≡ p, por absorción. Resultado: p∨q.
- d: ¬p→¬(p→¬q) ≡ p∨¬(¬p∨¬q) ≡ p∨(p∧q) ≡ p.
  Implicación material, De Morgan, doble negación y absorción.
- e: antecedente ≡(¬p∨q)∧p∧¬q≡False, por distribución y complementos.
  False→q≡True.
- f: el consecuente ¬¬p∨¬p≡p∨¬p≡True; cualquier implicación a True
  es True y su negación es False.

## 8 · Equivalencia y contraejemplos

a, b, c, f, g, h son equivalentes; d, e no.

- a se reduce a p→p≡True.
- b tiene antecedente ¬(p∧q)∨(p∧q)≡True; queda p∧q.
- c: distributividad da p∨(q∧r); implicación material en la otra
  expresión da lo mismo.
- d se reduce a p→(p∨q)≡True, distinto de q. Contraejemplo: p=F, q=F.
- e tiene antecedente contradictorio: queda True, no p∧¬q.
  Contraejemplo: p=F, q=F.
- f: distribución y complementos dan p∨q en ambas.
- g: De Morgan da ¬p∨¬q∨¬s; implicación material da el mismo resultado.
- h: negar q→r da q∧¬r; el primer lado queda ¬p∨(q∧¬r).
  Distribución/absorción en el segundo produce la misma fórmula.

## 9 · Sólo negación y disyunción

Transformar recursivamente las subfórmulas y reemplazar:

- A∧B por ¬(¬A∨¬B).
- A→B por ¬A∨B.
- A↔B por ¬(¬(¬A∨B)∨¬(¬B∨A)).

Variables, constantes, negación y disyunción quedan iguales. Por inducción
estructural se obtiene una fórmula equivalente que usa sólo ¬ y ∨.

## 10–12 · Razonamientos

10: las premisas son f→((e∨m)∧¬(e∧m)),¬f→¬e y(f∧e)→m.
Suponer e: la segunda, por contraposición, da f; la tercera da m.
La primera excluye e∧m. Contradicción; por tanto ¬e.

11: llamar J, C, G a “todos conocen a...”. De J→C y J→(C→G),
suponer J permite deducir C y C→G; luego G. Así J→G.

12: de dormir→galletitas y galletitas no se deduce dormir.
Valuación dormir=F, galletitas=V satisface ambas premisas y niega la
conclusión: afirmación del consecuente.

## 13–16 · Indefinición y evaluación secuencial

13: a, b son V; c, d, e, f son I en R. Ni0⁻¹ ni1/0 ni√−1 están definidos.
Multiplicar por0 no transforma una subexpresión indefinida en un real.

Para comparar los operadores ordinarios con los L, se extiende el operador
ordinario estrictamente: cualquier operando I propaga I.
Los L evalúan de izquierda a derecha y pueden evitar la derecha.
En el resto de las especificaciones, la teórica 2 permite usar la notación
sin L como abreviación secuencial; no confundir esa convención con esta comparación.

| p   | q   | p→q | p→Lq | p∧q | p∧Lq | p∨q | p∨Lq |
| --- | --- | --- | ---- | --- | ---- | --- | ---- |
| V   | V   | V   | V    | V   | V    | V   | V    |
| V   | F   | F   | F    | F   | F    | V   | V    |
| F   | V   | V   | V    | F   | F    | V   | V    |
| F   | F   | V   | V    | F   | F    | F   | F    |
| V   | I   | I   | I    | I   | I    | I   | V    |
| F   | I   | I   | V    | I   | F    | I   | I    |
| I   | V   | I   | I    | I   | I    | I   | I    |
| I   | F   | I   | I    | I   | I    | I   | I    |
| I   | I   | I   | I    | I   | I    | I   | I    |

No son conmutativos: F∧LI=F pero I∧LF=I; V∨LI=V pero I∨LV=I.
La negación conserva I y la equivalencia requiere ambos valores definidos.

## 17–18 · Evaluar fórmulas

17, a–g: **I, V, F, V, V, V, F**.
En a, la indefinición a la izquierda de∨L no se salva con b=V a la derecha.
En g,¬c=F evita evaluar¬y.

18, a–l: **V, V, V, I, F, V, I, F, V, V, I, V**.
d y g llegan a r=I sin una guarda anterior que decida el resultado;
j evita r porque su antecedente vale F; k compara una expresión con log0,
por lo que queda I. En i, las dos comparaciones internas son F y su
equivalencia es V.

## 19 · Fórmulas totales

Definir Rv=(¬q∧Lr). Es total: si q=V no evalúa r; si q=F,
r está definido. Rv expresa “r es verdadera”, no “r está definida”.

a: p∨Lq∨LRv. b: ¬(p∨Lq∨LRv).

c, exactamente una:
(p∧L¬q∧L¬Rv)∨L(¬p∧Lq∧L¬Rv)∨L(¬p∧L¬q∧LRv).

d: p∧Lq∧L¬Rv. e: ¬(p∧Lq∧LRv), que siempre es V bajo las hipótesis:
q y r no pueden ser ambas verdaderas. f:(p∨L¬p)∧LRv.
Todas usan p, q, r y nunca se indefinen en las seis valuaciones admisibles.

## 20–21 · Tipado, no verdad

20: a, b, d están bien tipadas. c aplica∨a enteros; e compara Bool con Z;
f suma Z y Bool. No se usa la coerción de bool a int que permite Python.

21: ambos lados de la igualdad son reales, de modo que la igualdad y su
conjunción con True son fórmulas. Que la igualdad sea falsa no implica
que esté mal formada.
