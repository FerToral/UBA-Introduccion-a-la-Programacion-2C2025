module Main where
import qualified Guia03 as A
import qualified Guia04 as B
import qualified Guia05 as C
import qualified Matrices as M
import qualified TipoParcial as P
import qualified Simulacro as S
import Control.Monad (unless)
import System.Exit (exitFailure)
import System.IO (hSetEncoding, stdout, utf8)

igual :: (Eq a, Show a) => String -> a -> a -> IO ()
igual nombre esperado obtenido =
  unless (esperado == obtenido) (putStrLn (nombre ++ ": esperado " ++ show esperado ++ ", recibido " ++ show obtenido) >> exitFailure)
cerca :: String -> Float -> Float -> IO ()
cerca nombre esperado obtenido = igual nombre True (abs (esperado-obtenido) < 0.0001)
main :: IO ()
main = do
  hSetEncoding stdout utf8
  igual "03 composición" [16,131,8] (map A.h [8,16,131])
  igual "03 k" [16,1,4] (map A.k [1,4,16])
  igual "03 absoluto" 4 (A.maximoAbsoluto (-4) 3)
  igual "03 máximo3" 9 (A.maximo3 1 9 4)
  igual "03 cero" [True,False,True,False] [A.algunoEsCero 0 2,A.ambosSonCero 0 2,A.algunoEsCeroPM 2 0,A.ambosSonCeroPM 1 1]
  igual "03 variantes cero" True (and [A.algunoEsCero a b == A.algunoEsCeroPM a b && A.ambosSonCero a b == A.ambosSonCeroPM a b | a <- [-1,0,1], b <- [-1,0,1]])
  igual "03 intervalos" [True,False,True,False] [A.enMismoIntervalo (-1) 3,A.enMismoIntervalo 3 4,A.enMismoIntervalo 4 7,A.enMismoIntervalo 7 8]
  igual "03 distintos" [3,7,6] [A.sumaDistintos 3 3 3,A.sumaDistintos 3 4 3,A.sumaDistintos 1 2 3]
  igual "03 dígitos/múltiplo" (True,7,2) (A.esMultiploDe 12 3,A.digitoUnidades (-127),A.digitoDecenas 127)
  igual "03 relacionados" [True,True,False] [A.estanRelacionados 8 2,A.estanRelacionados (-8) 2,A.estanRelacionados 7 3]
  cerca "03 producto" 11 (A.productoInterno (1,2) (3,4))
  igual "03 par menor" True (A.esParMenor (1,2) (2,3))
  cerca "03 distancia" 5 (A.distancia (0,0) (3,4))
  igual "03 terna" (6,2,4) (A.sumaTerna (1,2,3),A.sumarSoloMultiplos (10,-8,-5) 2,A.posPrimerPar (1,3,5))
  igual "03 tupla" (True,"x") (A.invertir (A.crearPar "x" True))
  igual "03 tramos" (49,15,4,10,True) (A.fTramos 7,A.fTramos 8,A.gParidad 8,A.gParidad 3,A.todosMenores (4,6,8))
  igual "03 bisiestos" [False,True,False,True] (map A.bisiesto [1901,1904,1900,2000])
  cerca "03 Manhattan" 12.8 (A.distanciaManhattan (-1,0,-8.5) (3.3,4,-4))
  igual "03 comparar" [-1,1,0] [A.comparar 45 312,A.comparar 2312 7,A.comparar 45 172]
  igual "04 Fibonacci" [0,1,1,2,3,5,8,13] (map B.fibonacci [0..7])
  igual "04 entero" [0,1,4] (map B.parteEntera [0,1.9,4])
  igual "04 divisible" [True,False,True] [B.esDivisible 12 3,B.esDivisible 13 3,B.esDivisible 0 7]
  igual "04 impares/factorial" (9,3840,945,1) (B.sumaImpares 3,B.medioFact 10,B.medioFact 9,B.medioFact 0)
  igual "04 dígitos" (True,False,0,2,10,True,False) (B.todosDigitosIguales 111,B.todosDigitosIguales 121,B.iesimoDigito 1023 2,B.cantDigitos 10,B.sumaDigitos 1234,B.esCapicua 12321,B.esCapicua 123)
  igual "04 potencias enteras" (15,8,36) (B.f1 3,B.f 2 2,B.sumaPotencias 2 2 2)
  cerca "04 f2" 14 (B.f2 3 2)
  cerca "04 f3" 30 (B.f3 2 2)
  cerca "04 f4" 28 (B.f4 2 2)
  cerca "04 e" 2.7182817 B.e
  cerca "04 raíz" 1.4 (B.raizDe2Aprox 3)
  cerca "04 racionales" 4.5 (B.sumaRacionales 2 2)
  igual "04 primos" (3,True,True,11) (B.menorDivisor 15,B.esPrimo 17,B.sonCoprimos 8 15,B.nEsimoPrimo 5)
  igual "04 sucesiones" (True,False,8,-1,True,True,False) (B.esFibonacci 21,B.esFibonacci 22,B.mayorDigitoPar 781,B.mayorDigitoPar 135,B.esSumaInicialDePrimos 0,B.esSumaInicialDePrimos 10,B.esSumaInicialDePrimos 11)
  igual "04 divisores" 6 (B.tomaValorMax 1 6)
  igual "04 Pitágoras" (20,6) (B.pitagoras 3 4 5,B.pitagoras 3 4 2)
  igual "05 estructura" (3,3,[1,2],[3,2,1]) (C.longitud [1,2,3::Integer],C.ultimo [1,2,3::Integer],C.principio [1,2,3::Integer],C.reverso [1,2,3::Integer])
  igual "05 igualdad" [True,True,True,False,True,True] [C.pertenece 2 [1,2::Integer],C.todosIguales ([]::[Integer]),C.todosDistintos [1,2::Integer],C.hayRepetidos [1,2::Integer],C.mismosElementos [1,1,2::Integer] [2,1],C.capicua "abba"]
  igual "05 quitar" ([2,1],[2],[1,2]) (C.quitar 1 [1,2,1::Integer],C.quitarTodos 1 [1,2,1::Integer],C.eliminarRepetidos [1,2,1::Integer])
  igual "05 aritmética" (6,6,3,[2,3],[4,5,6],[2,8,2],[3,6],[1,2,2,3]) (C.sumatoria [1,2,3],C.productoria [1,2,3],C.maximo [1,3,2],C.sumarElPrimero [1,2],C.sumarElUltimo [1,2,3],C.pares [1,2,3,8,2],C.multiplosDeN 3 [3,4,6],C.ordenar [3,2,1,2])
  igual "05 texto" (" a b ",2,["a","bb"],"bb","abb","a bb","a  bb") (C.sacarBlancosRepetidos "  a  b  ",C.contarPalabras " a bb ",C.palabras " a bb ",C.palabraMasLarga " a bb ",C.aplanar ["a","bb"],C.aplanarConBlancos ["a","bb"],C.aplanarConNBlancos ["a","bb"] 2)
  igual "05 acumulados/factores" ([1,3,6],[[2],[2,5],[2,3]]) (C.sumaAcumulada [1,2,3::Integer],C.descomponerEnPrimos [2,10,6])
  igual "05 contactos" (True,[("Ana","2")],[]) (C.enLosContactos "Ana" [("Ana","1")],C.agregarContacto ("Ana","2") [("Ana","1")],C.eliminarContacto "Ana" [("Ana","1")])
  igual "05 lockers" (True,"B",True,[(1,(False,"B"))]) (C.existeElLocker 1 [(1,(True,"B"))],C.ubicacionDelLocker 1 [(1,(True,"B"))],C.estaDisponibleElLocker 1 [(1,(True,"B"))],C.ocuparLocker 1 [(1,(True,"B"))])
  igual "05 matrices" (10,1,2,[[2,4],[6,8]],["ab","cd"],[3,4],[2,4],[[1,0],[0,1]],2) (M.sumaTotal [[1,2],[3,4]],M.cantidadDeApariciones 2 [[1,2],[3,4]],M.contarPalabras "a" [["a","b"],["a","c"]],M.multiplicarPorEscalar 2 [[1,2],[3,4]],M.concatenarFilas [["a","b"],["c","d"]],M.iesimaFila 1 [[1,2::Integer],[3,4]],M.iesimaColumna 1 [[1,2::Integer],[3,4]],M.matrizIdentidad 2,M.cantidadParesColumna 1 [[1,2],[3,4]])
  igual "05.1 stock" ([("b",1),("a",2)],2) (P.generarStock ["a","b","a"],P.stockDeProducto [("a",2)] "a")
  cerca "05.1 valor" 6 (P.dineroEnStock [("a",2)] [("a",3)])
  igual "05.1 oferta umbral" [("a",8),("b",10),("c",10)] (P.aplicarOferta [("a",11),("b",10)] [("a",10),("b",10),("c",10)])
  igual "05.1 sopa" (5,1,[1,2,3],True,False) (P.maximo [[1,1,5],[2,3,1]],P.masRepetido [[1,1,5],[2,3,1]],P.valoresDeCamino [[1,2],[4,3]] [(1,1),(1,2),(2,2)],P.esCaminoFibo [1,1,2,3,5] 1,P.esCaminoFibo [1,2,4] 2)
  igual "05.1 perfectos/amigos" ([1,2,3],True,[6,28,496,8128],[(220,284)]) (P.divisoresPropios 6,P.sonAmigos 220 284,P.losPrimerosNPerfectos 4,P.listaDeAmigos [220,284,6])
  igual "simulacro abundantes" 4 (S.cantidadNumerosAbundantes 12 24)
  igual "simulacro vencidas" ["A"] (S.cursadasVencidas [("A",2020,2),("B",2022,1),("A",2021,1)])
  igual "simulacro umbral" [3,5,5,0,5] (S.saturarEnUmbralHastaNegativo [3,8,5,0,7,-2,4] 5)
  igual "simulacro columna cero incluido" 2 (S.cantidadParesColumna [[-9,8,2,3],[2,7,-5,3],[-1,0,5,6]] 2)
  igual "simulacro no contar prefijo" 0 (S.cantidadParesColumna [[2,3],[4,5]] 2)
  putStrLn "Haskell: comprobaciones de guías03–05/05.1 y simulacro aprobadas."
