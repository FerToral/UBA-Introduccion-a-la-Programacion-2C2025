module TipoParcial where

-- 1–4. Stock. Se conserva el orden de última aparición de la práctica personal.
generarStock :: [String] -> [(String,Int)]
generarStock xs = contarProductos (sinRepetidos xs)
  where contarProductos [] = []
        contarProductos (p:ps) = (p,apariciones p xs):contarProductos ps
sinRepetidos :: Eq a => [a] -> [a]
sinRepetidos [] = []
sinRepetidos (x:xs) | pertenece x xs = sinRepetidos xs
                    | otherwise = x:sinRepetidos xs
pertenece :: Eq a => a -> [a] -> Bool
pertenece _ [] = False
pertenece x (y:ys) = x == y || pertenece x ys
apariciones :: Eq a => a -> [a] -> Int
apariciones _ [] = 0
apariciones p (x:xs) | p == x = 1 + apariciones p xs
                     | otherwise = apariciones p xs
stockDeProducto :: [(String,Int)] -> String -> Int
stockDeProducto [] _ = 0
stockDeProducto ((p,n):xs) buscado | p == buscado = n
                                 | otherwise = stockDeProducto xs buscado
precioDe :: String -> [(String,Float)] -> Float
precioDe p ((q,precio):xs) | p == q = precio
                          | otherwise = precioDe p xs
dineroEnStock :: [(String,Int)] -> [(String,Float)] -> Float
dineroEnStock [] _ = 0
dineroEnStock ((p,n):xs) precios = fromIntegral n * precioDe p precios + dineroEnStock xs precios
aplicarOferta :: [(String,Int)] -> [(String,Float)] -> [(String,Float)]
aplicarOferta _ [] = []
aplicarOferta stock ((p,precio):xs) | stockDeProducto stock p > 10 = (p,precio*0.8):aplicarOferta stock xs
                                   | otherwise = (p,precio):aplicarOferta stock xs

-- 5–8. Sopa de números: posiciones desde uno.
type Tablero = [[Int]]
type Posicion = (Int,Int)
type Camino = [Posicion]
aplanar :: [[a]] -> [a]
aplanar [] = []
aplanar (x:xs) = x ++ aplanar xs
mayor :: Int -> Int -> Int
mayor a b | a > b = a
          | otherwise = b
maximo :: Tablero -> Int
maximo t = maxLista (aplanar t)
  where maxLista [x] = x
        maxLista (x:xs) = mayor x (maxLista xs)
masRepetido :: Tablero -> Int
masRepetido t = elegir (aplanar t)
  where valores = aplanar t
        elegir [x] = x
        elegir (x:xs) | apariciones x valores >= apariciones resto valores = x
                       | otherwise = resto
          where resto = elegir xs
elemento :: Int -> [a] -> a
elemento 1 (x:_) = x
elemento n (_:xs) = elemento (n-1) xs
valoresDeCamino :: Tablero -> Camino -> [Int]
valoresDeCamino _ [] = []
valoresDeCamino t ((f,c):xs) = elemento c (elemento f t):valoresDeCamino t xs
fib :: Int -> Integer
fib n = avanzar n 0 1
  where avanzar 0 a _ = a
        avanzar j a b = avanzar (j-1) b (a+b)
esCaminoFibo :: [Int] -> Int -> Bool
esCaminoFibo [] _ = True
esCaminoFibo (x:xs) i = fromIntegral x == fib i && esCaminoFibo xs (i+1)

-- 9–12. Pares sin repetir: sólo se compara cada elemento con su sufijo.
divisoresPropios :: Int -> [Int]
divisoresPropios n = recorrer 1
  where recorrer d | d >= n = []
                    | mod n d == 0 = d:recorrer (d+1)
                    | otherwise = recorrer (d+1)
suma :: [Int] -> Int
suma [] = 0
suma (x:xs) = x + suma xs
-- Suma en O(sqrt n), para poder explorar hasta el cuarto perfecto.
sumaDivisoresPropios :: Int -> Int
sumaDivisoresPropios 1 = 0
sumaDivisoresPropios n = 1 + parejas 2
  where parejas d | d > div n d = 0
                   | mod n d /= 0 = parejas (d+1)
                   | d == div n d = d + parejas (d+1)
                   | otherwise = d + div n d + parejas (d+1)
sonAmigos :: Int -> Int -> Bool
sonAmigos n m = n /= m && sumaDivisoresPropios n == m && sumaDivisoresPropios m == n
losPrimerosNPerfectos :: Int -> [Int]
losPrimerosNPerfectos n = buscar n 2
  where buscar 0 _ = []
        buscar pendientes x | sumaDivisoresPropios x == x = x:buscar (pendientes-1) (x+1)
                              | otherwise = buscar pendientes (x+1)
listaDeAmigos :: [Int] -> [(Int,Int)]
listaDeAmigos [] = []
listaDeAmigos (x:xs) = con x xs ++ listaDeAmigos xs
  where con _ [] = []
        con a (b:bs) | sonAmigos a b = (a,b):con a bs
                      | otherwise = con a bs
