module Matrices where
import Guia05 (longitud, sumatoria, aplanar, pares)

-- Ejercicio 8. Índices desde cero; matriz rectangular no vacía.
sumaTotal :: [[Integer]] -> Integer
sumaTotal [] = 0
sumaTotal (f:fs) = sumatoria f + sumaTotal fs
cantidadDeApariciones :: Integer -> [[Integer]] -> Integer
cantidadDeApariciones = cantidadDeApariciones2
contarPalabras :: String -> [[String]] -> Int
contarPalabras p m = fromIntegral (cantidadDeApariciones2 p m)
cantidadDeApariciones2 :: Eq a => a -> [[a]] -> Integer
cantidadDeApariciones2 _ [] = 0
cantidadDeApariciones2 e (f:fs) = contar f + cantidadDeApariciones2 e fs
  where contar [] = 0
        contar (x:xs) | x == e = 1 + contar xs
                       | otherwise = contar xs
multiplicarPorEscalar :: Integer -> [[Integer]] -> [[Integer]]
multiplicarPorEscalar _ [] = []
multiplicarPorEscalar n (f:fs) = multiplicar f : multiplicarPorEscalar n fs
  where multiplicar [] = []
        multiplicar (x:xs) = (n*x):multiplicar xs
concatenarFilas :: [[String]] -> [String]
concatenarFilas [] = []
concatenarFilas (f:fs) = aplanar f : concatenarFilas fs
iesimaFila :: Integer -> [[a]] -> [a]
iesimaFila 0 (f:_) = f
iesimaFila i (_:fs) = iesimaFila (i-1) fs
elemento :: Integer -> [a] -> a
elemento 0 (x:_) = x
elemento i (_:xs) = elemento (i-1) xs
iesimaColumna :: Integer -> [[a]] -> [a]
iesimaColumna _ [] = []
iesimaColumna i (f:fs) = elemento i f : iesimaColumna i fs
matrizIdentidad :: Integer -> [[Integer]]
matrizIdentidad n = filas 0
  where filas i | i == n = []
                 | otherwise = columnas i 0 : filas (i+1)
        columnas i j | j == n = []
                     | i == j = 1:columnas i (j+1)
                     | otherwise = 0:columnas i (j+1)
cantidadParesColumna :: Integer -> [[Integer]] -> Integer
cantidadParesColumna i m = longitud (pares (iesimaColumna i m))
