# Tablas del ejercicio6

Generadas por logica.py: todas las valuaciones, ambos lados.

## a · (False∧p) ≡ False

| p   | Izquierda | Derecha |
| --- | --------- | ------- |
| V   | F         | F       |
| F   | F         | F       |

## b · (True∨p) ≡ True

| p   | Izquierda | Derecha |
| --- | --------- | ------- |
| V   | V         | V       |
| F   | V         | V       |

## c · (True∧p) ≡ p

| p   | Izquierda | Derecha |
| --- | --------- | ------- |
| V   | V         | V       |
| F   | F         | F       |

## d · (False∨p) ≡ p

| p   | Izquierda | Derecha |
| --- | --------- | ------- |
| V   | V         | V       |
| F   | F         | F       |

## e · (p∧p) ≡ p

| p   | Izquierda | Derecha |
| --- | --------- | ------- |
| V   | V         | V       |
| F   | F         | F       |

## f · (p∨p) ≡ p

| p   | Izquierda | Derecha |
| --- | --------- | ------- |
| V   | V         | V       |
| F   | F         | F       |

## g · (p∨¬p) ≡ True

| p   | Izquierda | Derecha |
| --- | --------- | ------- |
| V   | V         | V       |
| F   | V         | V       |

## h · (p∧¬p) ≡ False

| p   | Izquierda | Derecha |
| --- | --------- | ------- |
| V   | F         | F       |
| F   | F         | F       |

## i · ¬¬p ≡ p

| p   | Izquierda | Derecha |
| --- | --------- | ------- |
| V   | V         | V       |
| F   | F         | F       |

## j · (p∧(p∨q)) ≡ p

| p   | q   | Izquierda | Derecha |
| --- | --- | --------- | ------- |
| V   | V   | V         | V       |
| V   | F   | V         | V       |
| F   | V   | F         | F       |
| F   | F   | F         | F       |

## k · (p∨(p∧q)) ≡ p

| p   | q   | Izquierda | Derecha |
| --- | --- | --------- | ------- |
| V   | V   | V         | V       |
| V   | F   | V         | V       |
| F   | V   | F         | F       |
| F   | F   | F         | F       |

## l · ¬(p∧q) ≡ (¬p∨¬q)

| p   | q   | Izquierda | Derecha |
| --- | --- | --------- | ------- |
| V   | V   | F         | F       |
| V   | F   | V         | V       |
| F   | V   | V         | V       |
| F   | F   | V         | V       |

## m · ¬(p∨q) ≡ (¬p∧¬q)

| p   | q   | Izquierda | Derecha |
| --- | --- | --------- | ------- |
| V   | V   | F         | F       |
| V   | F   | F         | F       |
| F   | V   | F         | F       |
| F   | F   | V         | V       |

## n · (p∧q) ≡ (q∧p)

| p   | q   | Izquierda | Derecha |
| --- | --- | --------- | ------- |
| V   | V   | V         | V       |
| V   | F   | F         | F       |
| F   | V   | F         | F       |
| F   | F   | F         | F       |

## ñ · (p∨q) ≡ (q∨p)

| p   | q   | Izquierda | Derecha |
| --- | --- | --------- | ------- |
| V   | V   | V         | V       |
| V   | F   | V         | V       |
| F   | V   | V         | V       |
| F   | F   | F         | F       |

## o · (p∧(q∧r)) ≡ ((p∧q)∧r)

| p   | q   | r   | Izquierda | Derecha |
| --- | --- | --- | --------- | ------- |
| V   | V   | V   | V         | V       |
| V   | V   | F   | F         | F       |
| V   | F   | V   | F         | F       |
| V   | F   | F   | F         | F       |
| F   | V   | V   | F         | F       |
| F   | V   | F   | F         | F       |
| F   | F   | V   | F         | F       |
| F   | F   | F   | F         | F       |

## p · (p∨(q∨r)) ≡ ((p∨q)∨r)

| p   | q   | r   | Izquierda | Derecha |
| --- | --- | --- | --------- | ------- |
| V   | V   | V   | V         | V       |
| V   | V   | F   | V         | V       |
| V   | F   | V   | V         | V       |
| V   | F   | F   | V         | V       |
| F   | V   | V   | V         | V       |
| F   | V   | F   | V         | V       |
| F   | F   | V   | V         | V       |
| F   | F   | F   | F         | F       |

## q · (p∧(q∨r)) ≡ ((p∧q)∨(p∧r))

| p   | q   | r   | Izquierda | Derecha |
| --- | --- | --- | --------- | ------- |
| V   | V   | V   | V         | V       |
| V   | V   | F   | V         | V       |
| V   | F   | V   | V         | V       |
| V   | F   | F   | F         | F       |
| F   | V   | V   | F         | F       |
| F   | V   | F   | F         | F       |
| F   | F   | V   | F         | F       |
| F   | F   | F   | F         | F       |

## r · (p∨(q∧r)) ≡ ((p∨q)∧(p∨r))

| p   | q   | r   | Izquierda | Derecha |
| --- | --- | --- | --------- | ------- |
| V   | V   | V   | V         | V       |
| V   | V   | F   | V         | V       |
| V   | F   | V   | V         | V       |
| V   | F   | F   | V         | V       |
| F   | V   | V   | V         | V       |
| F   | V   | F   | F         | F       |
| F   | F   | V   | F         | F       |
| F   | F   | F   | F         | F       |

## s · (p→q) ≡ (¬q→¬p)

| p   | q   | Izquierda | Derecha |
| --- | --- | --------- | ------- |
| V   | V   | V         | V       |
| V   | F   | F         | F       |
| F   | V   | V         | V       |
| F   | F   | V         | V       |

## t · (p→q) ≡ (¬p∨q)

| p   | q   | Izquierda | Derecha |
| --- | --- | --------- | ------- |
| V   | V   | V         | V       |
| V   | F   | F         | F       |
| F   | V   | V         | V       |
| F   | F   | V         | V       |

## u · (p↔q) ≡ ((p→q)∧(q→p))

| p   | q   | Izquierda | Derecha |
| --- | --- | --------- | ------- |
| V   | V   | V         | V       |
| V   | F   | F         | F       |
| F   | V   | F         | F       |
| F   | F   | V         | V       |
