module Simulacro where

-- Ejercicio 1
cantidadNumerosAbundantes :: Integer -> Integer -> Integer
cantidadNumerosAbundantes d h | d > h = 0
                              | otherwise = unoSiCeroSiNo (esAbundante d) + cantidadNumerosAbundantes (d+1) h

unoSiCeroSiNo :: Bool -> Integer
unoSiCeroSiNo True = 1
unoSiCeroSiNo False = 0

esAbundante :: Integer -> Bool
esAbundante d = sumaDivisoresPropios d > d

sumaDivisoresPropios :: Integer -> Integer
sumaDivisoresPropios n = sumaDivisoresPropiosDesde 1 n

sumaDivisoresPropiosDesde :: Integer -> Integer -> Integer
sumaDivisoresPropiosDesde d n | d == n = 0
                              | mod n d == 0 = d + sumaDivisoresPropiosDesde (d+1) n
                              | otherwise = sumaDivisoresPropiosDesde (d+1) n

-- sumaDivisoresPropiosDesde :: Integer -> Integer -> Integer
-- sumaDivisoresPropiosDesde d n | d == n = 0
--                               | esDivisible n d = d + sumaDivisoresPropiosDesde (d+1) n
--                               | otherwise = sumaDivisoresPropiosDesde (d+1) n


-- sumaDivisoresPropiosDesde :: Integer -> Integer -> Integer
-- sumaDivisoresPropiosDesde d n | d == n = 0
--                               | otherwise = d * unoSiCeroSiNo (esDivisible n d) + sumaDivisoresPropiosDesde (d+1) n


esDivisible :: Integer -> Integer -> Bool
esDivisible n d = mod n d == 0

-- Ejercicio 2
cursadasVencidas :: [(String, Integer, Integer)] -> [String]
cursadasVencidas [] = []
cursadasVencidas xs = sinRepetidos (cursadasVencidasRepetidas xs)

cursadasVencidasRepetidas :: [(String, Integer, Integer)] -> [String]
cursadasVencidasRepetidas [] = []
cursadasVencidasRepetidas ((materia, año, cuatri):cursadas) | esMateriaVencida = materia : cursadasVencidasRepetidas cursadas
                                                            | otherwise = cursadasVencidasRepetidas cursadas
                                                            where esMateriaVencida = año < 2021 || (año == 2021 && cuatri < 2)

sinRepetidos :: [String] -> [String]
sinRepetidos [] = []
sinRepetidos (x:xs) | pertenece x xs = sinRepetidos xs
                    | otherwise = x: sinRepetidos xs



-- Ejercicio 3
saturarEnUmbralHastaNegativo :: [Integer] -> Integer -> [Integer]
saturarEnUmbralHastaNegativo [] _ = []
saturarEnUmbralHastaNegativo (x:xs) u | x < 0 = []
                                      | x > u = u: saturarEnUmbralHastaNegativo xs u
                                      | otherwise = x: saturarEnUmbralHastaNegativo xs u

-- Ejercicio 4. La columna comienza en uno; cero también es par.
cantidadParesColumna :: [[Integer]] -> Integer -> Integer
cantidadParesColumna [] _ = 0
cantidadParesColumna (fila:resto) c = contar (elemento fila c) + cantidadParesColumna resto c
  where contar x | mod x 2 == 0 = 1
                 | otherwise = 0
        elemento (x:_) 1 = x
        elemento (_:xs) i = elemento xs (i-1)

pertenece :: Eq a => a -> [a] -> Bool
pertenece _ [] = False
pertenece e (x:xs) = e == x || pertenece e xs
