import Data.List
import Data.Maybe (fromMaybe)

data Elemento = Elemento {
  valor :: Int, -- valor int da casa
  cord :: (Int, Int), -- tupla de valores referentes a linha e coluna do elemento na matriz --> (x, y)
  id_area :: Int, -- id da area, usado para acessar os elementos de uma mesma área 
  tam_area :: Int, -- valor int que informa o tamanho da área, utilizado para saber quais números podem ser inseridos ali
  area_complete :: Bool,
  valores_possiveis :: [Int] -- lista de valores possíveis para aquela casa(célula)
}

matriz :: [[Elemento]]
matriz = [      [Elemento 4 (0, 0) 100 4 False [], Elemento 0 (0, 1) 100 4 False [2], Elemento 4 (0, 2) 105 4 False [], Elemento 2 (0, 3) 105 4 False [], Elemento 0 (0, 4) 106 2 False [1,2], Elemento 0 (0, 5) 106 2 False [1,2], Elemento 6 (0, 6) 116 7 False [], Elemento 0 (0, 7) 118 1 False [1], Elemento 7 (0, 8) 126 7 False [], Elemento 4 (0, 9) 126 7 False []]
              , [ Elemento 3 (1, 0) 100 4 False [], Elemento 1 (1, 1) 100 4 False [], Elemento 0 (1, 2) 105 4 False [3], Elemento 1 (1, 3) 116 7 False [], Elemento 0 (1, 4) 116 7 False [2,5,7], Elemento 4 (1, 5) 116 7 False [], Elemento 0 (1, 6) 116 7 False [2,5,7], Elemento 0 (1, 7) 119 2 False [1,2], Elemento 0 (1, 8) 126 7 False [1,6], Elemento 3 (1, 9) 126 7 False []]
              , [ Elemento 0 (2, 0) 101 4 False [2,3,4], Elemento 0 (2, 1) 101 4 False [2,3,4], Elemento 1 (2, 2) 105 4 False [], Elemento 0 (2, 3) 108 2 False [1,2], Elemento 6 (2, 4) 113 7 False [], Elemento 0 (2, 5) 114 2 False [1,2], Elemento 3 (2, 6) 116 7 False [], Elemento 0 (2, 7) 119 2 False [1,2], Elemento 5 (2, 8) 126 7 False [], Elemento 2 (2, 9) 126 7 False []]
              , [ Elemento 0 (3, 0) 101 4 False [2,3,4], Elemento 1 (3, 1) 101 4 False [], Elemento 0 (3, 2) 107 2 False [1,2], Elemento 0 (3, 3) 108 2 False [1,2], Elemento 4 (3, 4) 113 7 False [], Elemento 0 (3, 5) 114 2 False [1,2], Elemento 0 (3, 6) 116 7 False [2,5,7], Elemento 5 (3, 7) 125 7 False [], Elemento 0 (3, 8) 125 7 False [4,7], Elemento 0 (3, 9) 126 7 False [1,6]]
              , [ Elemento 2 (4, 0) 102 3 False [], Elemento 0 (4, 1) 102 3 False [1,3], Elemento 0 (4, 2) 107 2 False [1,2], Elemento 7 (4, 3) 113 7 False [], Elemento 0 (4, 4) 113 7 False [1,2,5], Elemento 3 (4, 5) 113 7 False [], Elemento 0 (4, 6) 115 5 False [1,4], Elemento 3 (4, 7) 125 7 False [], Elemento 6 (4, 8) 125 7 False [], Elemento 2 (4, 9) 125 7 False []]
              , [ Elemento 0 (5, 0) 102 3 False [1,3], Elemento 7 (5, 1) 103 7 False [], Elemento 0 (5, 2) 103 7 False [1,4,5], Elemento 0 (5, 3) 113 7 False [1,2,5], Elemento 0 (5, 4) 113 7 False [1,2,5], Elemento 5 (5, 5) 115 5 False [], Elemento 3 (5, 6) 115 5 False [], Elemento 0 (5, 7) 120 1 False [1], Elemento 0 (5, 8) 125 7 False [4,7], Elemento 1 (5, 9) 125 7 False []]
              , [ Elemento 0 (6, 0) 103 7 False [1,4,5], Elemento 3 (6, 1) 103 7 False [], Elemento 0 (6, 2) 103 7 False [1,4,5], Elemento 6 (6, 3) 103 7 False [], Elemento 3 (6, 4) 112 6 False [], Elemento 0 (6, 5) 115 5 False [1,4], Elemento 2 (6, 6) 115 5 False [], Elemento 6 (6, 7) 112 6 False [], Elemento 2 (6, 8) 122 4 False [], Elemento 0 (6, 9) 122 4 False [1,4]]
              , [ Elemento 4 (7, 0) 104 5 False [], Elemento 2 (7, 1) 103 7 False [], Elemento 0 (7, 2) 109 4 False [1,3,4], Elemento 0 (7, 3) 110 4 False [3,4], Elemento 0 (7, 4) 112 6 False [1,2,4], Elemento 5 (7, 5) 112 6 False [], Elemento 0 (7, 6) 112 6 False [1,2,4], Elemento 0 (7, 7) 112 6 False [1,2,4], Elemento 4 (7, 8) 121 6 False [], Elemento 3 (7, 9) 122 4 False []]
              , [ Elemento 2 (8, 0) 104 5 False [], Elemento 5 (8, 1) 104 5 False [], Elemento 0 (8, 2) 109 4 False [1,3,4], Elemento 1 (8, 3) 110 4 False [], Elemento 2 (8, 4) 110 4 False [], Elemento 0 (8, 5) 110 4 False [3,4], Elemento 2 (8, 6) 111 4 False [], Elemento 0 (8, 7) 121 6 False [1,6], Elemento 3 (8, 8) 121 6 False [], Elemento 0 (8, 9) 122 4 False [1,4]]
              , [ Elemento 1 (9, 0) 104 5 False [], Elemento 0 (9, 1) 104 5 False [3], Elemento 0 (9, 2) 109 4 False [1,3,4], Elemento 2 (9, 3) 109 4 False [], Elemento 4 (9, 4) 111 4 False [], Elemento 0 (9, 5) 111 4 False [3], Elemento 1 (9, 6) 111 4 False [], Elemento 2 (9, 7) 121 6 False [], Elemento 0 (9, 8) 121 6 False [1,6], Elemento 5 (9, 9) 121 6 False []]]

-- printa a matriz
print_matriz :: [[Elemento]] -> IO ()
print_matriz matriz = mapM_ printRow matriz
    where
        printRow row  = putStrLn $ unwords $ map showElemento row 
        showElemento elem = show (valor elem)

-- seta true em area_complete para a area que tiver todos os valores diferente de zero
atualizar_area_complete :: [[Elemento]] -> [[Elemento]]
atualizar_area_complete matriz = map (map verificarAreaCompleta) matriz
  where
    verificarAreaCompleta elemento =
      if valor elemento /= 0 && all (verificarElementoCompleto (valor elemento)) elementosArea
        then elemento { area_complete = True }
        else elemento
      where
        idArea = id_area elemento
        elementosArea = obterElementosArea matriz idArea

verificarElementoCompleto :: Int -> Elemento -> Bool
verificarElementoCompleto valorReferencia elemento =
  valorReferencia /= 0 && valor elemento /= 0

obterElementosArea :: [[Elemento]] -> Int -> [Elemento]
obterElementosArea matriz idArea =
  concat $ map (filter (\elemento -> id_area elemento == idArea)) matriz

-- completa os Elementos que tiverem apenas 1 numero na lista de valores_possiveis
complete_unico :: [[Elemento]] -> [[Elemento]]
complete_unico matriz = map (map atualizar_elemento) matriz
    where
      atualizar_elemento elem@(Elemento v c i t ac vp)
        | length vp == 1 = Elemento (head vp) c i t ac []
        | otherwise = elem

--funcao auxiliar da tirar_possibilidades para pegar os valores vizinhos de um elemento
get_vizinhos :: [[Elemento]] -> Elemento -> [Int]
get_vizinhos matriz (Elemento _ (x, y) _ _ _ valores_possiveis) =
  let left = fromMaybe 0 $ valor <$> get_elem (x, y - 1)  
      right = fromMaybe 0 $ valor <$> get_elem (x, y + 1)
      up = fromMaybe 0 $ valor <$> get_elem (x - 1, y)
      down = fromMaybe 0 $ valor <$> get_elem (x + 1, y)
  in [left, right, up, down]
  where
    get_elem (i, j)
      | i < 0 || j < 0 || i >= length matriz || j >= length (matriz !! i) = Nothing
      | otherwise = Just ( (matriz !! i !! j))

-- analisa os valores vizinhos de cada Elemento, e compara com o valor do elemento quando diferente de zero
--se for igual, retira da lista de valores_possiveis do vizinho o valor em questao
tirar_possibilidades :: [[Elemento]] -> [[Elemento]]
tirar_possibilidades matriz = map (map atualizar_elemento) matriz
    where
      atualizar_elemento elemento = 
        let vizinhos = get_vizinhos matriz elemento
            valores_possiveis_atualizados = foldr delete (valores_possiveis elemento) vizinhos
        in elemento { valores_possiveis = valores_possiveis_atualizados}

-----------last_possible--------------------------------------------------
last_possible :: [[Elemento]] -> [(Int, Int)] -> [[Elemento]]
last_possible matriz list_areas_to_be_analyzed =
  case get_index_value list_areas_to_be_analyzed of
    Nothing -> matriz
    Just (id_area, tam_area) ->
      let
        new_list_areas_to_be_analyzed = removerPrimeiraTupla list_areas_to_be_analyzed
        matriz_atualizada = chamada_das_funcoes_last_possible matriz id_area tam_area
      in
        if null new_list_areas_to_be_analyzed
          then matriz_atualizada
          else last_possible matriz_atualizada new_list_areas_to_be_analyzed

--retorna a lista de tuplas com (id_area, tam_area) , das areas nao completas
areas_to_be_analyzed :: [[Elemento]] -> [(Int, Int)]
areas_to_be_analyzed matriz = nub [(id_area elemento, tam_area elemento) | linha <- matriz, elemento <- linha, not (area_complete elemento)]

chamada_das_funcoes_last_possible :: [[Elemento]] -> Int -> Int -> [[Elemento]]
chamada_das_funcoes_last_possible matriz id_area tam_area =
  let
    valores_possiveis = take_valores_possiveis matriz id_area
    lista_contador = criar_lista_contador valores_possiveis tam_area
    indices_valores = contadorIndices lista_contador
  in
    uma_casa_possivel matriz indices_valores id_area

--recebe a matriz, um id_area e
-- retorna a lista com uniao com repeticao dos valores possiveis de uma area
take_valores_possiveis :: [[Elemento]] -> Int -> [Int]
take_valores_possiveis matriz id_area = concatMap valores_possiveis_area (concat matriz)
  where
    valores_possiveis_area (Elemento _ _ id _ _ valores_possiveis) | id == id_area = valores_possiveis
    valores_possiveis_area _ = []

--recebe a lista valoes_possiveis retornado por take_valores_possiveis e o tam_area,
-- e cria a lista que sera usada como contador
-- retorna a lista contador
criar_lista_contador :: [Int] -> Int -> [Int] -- passo 2
criar_lista_contador valores_possiveis1 tam_area = contador
  where
    contador = map (countOccurrences valores_possiveis1) [1..tam_area]
    countOccurrences xs x = length $ filter (== x) xs

-- recebe uma lista e retorna uma lista de tuplas
--transforma a lista contador em uma lista de tuplas com (valor,indice) = (qtd desse numero, numero )
-- [(contador,indice+1 = valor)]
contadorIndices :: [Int] -> [(Int, Int)]
contadorIndices lista = zip lista [1..]

--retornar a primeira tupla da lista
get_index_value :: [(Int, Int)] -> Maybe (Int, Int)
get_index_value [] = Nothing
get_index_value ((x, y):_) = Just (x, y)

-- retorna a cauda de uma lista
removerPrimeiraTupla :: [(a, b)] -> [(a, b)]
removerPrimeiraTupla [] = []
removerPrimeiraTupla (_:xs) = xs

-- indice, valor = qtd do numero, numero
uma_casa_possivel :: [[Elemento]] -> [(Int, Int)] -> Int -> [[Elemento]]
uma_casa_possivel matriz lista_indice_valor1 id_area =
  case get_index_value lista_indice_valor1 of
    Nothing -> matriz
    Just (indice, valor) ->
      let
        lista_indice_valor1_atualizado = removerPrimeiraTupla lista_indice_valor1
        matriz_atualizada = set_last_possivel matriz id_area indice valor
      in
        if null lista_indice_valor1_atualizado
          then matriz_atualizada
          else uma_casa_possivel matriz_atualizada lista_indice_valor1_atualizado id_area
 
set_last_possivel :: [[Elemento]] -> Int -> Int -> Int -> [[Elemento]]
set_last_possivel matriz identif_area indice novo_valor
  | indice == 1 = minha_funcao
  | otherwise = matriz
  where
    minha_funcao = map (map atualizaElemento ) matriz

    atualizaElemento :: Elemento -> Elemento
    atualizaElemento elemento
      | (id_area elemento) == identif_area && numeroNaLista novo_valor (valores_possiveis elemento) =
          let
            novos_valores_possiveis = []
          in
            elemento { valor = novo_valor, valores_possiveis = novos_valores_possiveis }
      | otherwise = elemento
        
numeroNaLista :: Int -> [Int] -> Bool
numeroNaLista _ [] = False
numeroNaLista numero (x:xs)
  | numero == x = True
  | otherwise = numeroNaLista numero xs

-----------------------------------------------------------------
-- area_coluna
--recebe a matriz e a lista de areas para analisar retornada por areas_to_be_analyzed 
--essa funcao usa a verificar coluna2 e retorna uma lista de tuplas,com informações da 
--coluna a ser preenchida(id_area,x,y,valor), se nao houver coluna retorna lista vazia
verificar_coluna :: [[Elemento]] -> [(Int, Int)] -> [(Int, Int, Int, Int)]
verificar_coluna matriz list_areas_to_be_analyzed =
  case get_index_value list_areas_to_be_analyzed of
    Nothing -> [] -- Retorna uma lista vazia quando não há mais áreas para serem analisadas
    Just (id_area, tam_area) ->
      let
        new_list_areas_to_be_analyzed = removerPrimeiraTupla list_areas_to_be_analyzed
        colunas = verificar_coluna2 matriz id_area
        areas_com_colunas = case colunas of
                              Nothing -> []
                              Just colunasList -> colunasList
      in
        if null new_list_areas_to_be_analyzed
          then areas_com_colunas
          else areas_com_colunas ++ verificar_coluna matriz new_list_areas_to_be_analyzed


-- --retorna uma lista de tuplas, com informações da coluna da area se houver
verificar_coluna2 :: [[Elemento]] -> Int -> Maybe [(Int, Int, Int, Int)]
verificar_coluna2 matriz identif_area = 
  let
    elementos = concat matriz
    filtro = filter (\elem -> id_area elem == identif_area && valor elem == 0) elementos
    coordenadas_x = map (\elem -> fst (cord elem)) filtro
    coordenadas_y = map (\elem -> snd (cord elem)) filtro
    valores_restantes_area = reverse . nub $ concatMap (\elem -> valores_possiveis elem) filtro
    coluna_valida = all (== head coordenadas_y) coordenadas_y && sort coordenadas_x == [minimum coordenadas_x .. maximum coordenadas_x]
    tuplas = zip4 (repeat identif_area) coordenadas_x coordenadas_y valores_restantes_area
  in
    if coluna_valida then Just tuplas else Nothing

getFirstTuple :: [(a, b, c, d)] -> (a, b, c, d)
getFirstTuple ((w, x, y, z):_) = (w, x, y, z)
getFirstTuple [] = error "Lista vazia"

resto_tuplas :: [(a, b, c, d)] -> [(a, b, c, d)]
resto_tuplas [] = [] -- Se a lista estiver vazia, retorna uma lista vazia
resto_tuplas (_:xs) = xs 

area_coluna :: [[Elemento]] -> [(Int, Int, Int, Int)] -> [[Elemento]]
area_coluna matriz [] = matriz
area_coluna matriz lista_tuplas2 =
  let
    (identif_area, cord_x, cord_y, novo_valor) = getFirstTuple lista_tuplas2
    resto_tuplas_resultado = resto_tuplas lista_tuplas2
    matriz_atualizada = preencher_coluna matriz identif_area cord_x cord_y novo_valor
  in
    if length resto_tuplas_resultado == 0
      then matriz_atualizada
      else area_coluna matriz_atualizada resto_tuplas_resultado


preencher_coluna :: [[Elemento]] -> Int -> Int -> Int -> Int -> [[Elemento]]
preencher_coluna matriz identif_area cord_x cord_y novo_valor =
  map (map atualizarElemento) matriz
  where
    atualizarElemento :: Elemento -> Elemento
    atualizarElemento elemento
      | it_found (id_area elemento) (fst (cord elemento)) (snd (cord elemento)) identif_area cord_x cord_y = elemento { valor = novo_valor, valores_possiveis = [] }
      | otherwise = elemento

--retorna se dois valors sao iguais
it_found :: Int -> Int -> Int -> Int -> Int -> Int -> Bool
it_found a b c d e f = if a == d && b == e && c == f then True else False

------------verificar_acima e verificar_abaixo----------------------
verificar_acima :: [[Elemento]] -> [[Elemento]]
verificar_acima matriz = map (map atualizar_elemento) matriz
  where
    atualizar_elemento elemento@(Elemento valor (x, y) id_area _ _ valores_possiveis)
      | valor == 0 && x /= 0 && valor1 /= 0 = elemento { valores_possiveis = filter (<= valor1) valores_possiveis }
      | otherwise = elemento
      where
        valor1 = case getElem (x - 1) y matriz of
          Just (Elemento valor _ id_area2 _ _ _) | id_area == id_area2 -> valor
          _ -> 0
    atualizar_elemento elemento = elemento

getElem :: Int -> Int -> [[a]] -> Maybe a
getElem x y xs
  | x >= 0 && y >= 0 && x < length xs && y < length (xs !! x) = Just (xs !! x !! y)
  | otherwise = Nothing

verificar_acima2 :: [[Elemento]] -> [[Elemento]]
verificar_acima2 matriz = map (map atualizar_elemento) matriz
  where
    atualizar_elemento elemento@(Elemento valor (x, y) id_area _ area_completa valores_possiveis)
      | valor == 0 && x /= 0 && valor1 == 0 && area_completa == False && id_area == id_area2 = elemento { valor = novo_valor }
      | otherwise = elemento
      where
        valor1 = case getElem (x - 1) y matriz of
          Just (Elemento valor _ _ _ _ _)  -> valor
        id_area2 = case getElem (x - 1) y matriz of
          Just (Elemento _ _ id_area _ _ _)  -> id_area
        novo_valor
          | length auxiliar_lista == 1 = head auxiliar_lista
          | otherwise = valor
        auxiliar_lista = delete (maximum valores_possiveis) valores_possiveis
    atualizar_elemento elemento = elemento

verificar_abaixo :: [[Elemento]] -> [[Elemento]]
verificar_abaixo matriz = map (map atualizar_elemento) matriz
  where
    atualizar_elemento elemento@(Elemento valor (x, y) id_area _ _ valores_possiveis)
      | valor == 0 && x < (length matriz - 1) && elemento_abaixo = elemento { valores_possiveis = filter (>= valor1) valores_possiveis }
      | otherwise = elemento
      where
        valor1 = case getElem (x + 1) y matriz of
          Just (Elemento valor _ id_area2 _ _ _) | id_area == id_area2 && valor /= 0 -> valor
          _ -> 0
        elemento_abaixo  = case getElem (x + 1) y matriz of
          Just (Elemento valor _ id_area2 _ _ _) | id_area == id_area2 -> True
          _ -> False
    atualizar_elemento elemento = elemento


------loop-----------------------------
loop :: [[Elemento]] -> Int -> IO (Int, [[Elemento]])
loop matrix n_loop = do
  let matriz2 = tirar_possibilidades matrix
    
      --last_possible
      areas_analisar2 = areas_to_be_analyzed matriz2
      matriz3 = last_possible matriz2 areas_analisar2
      matriz4 = atualizar_area_complete matriz3

      --area coluna
      areas_analisar1 = areas_to_be_analyzed matriz4
      teste1 = verificar_coluna matriz4 areas_analisar1
      matriz5 = area_coluna matriz4 teste1
      matriz6 = atualizar_area_complete matriz5

      --verificar acima1
      matriz7 = verificar_acima matriz6

      --verificar_acima2
      matriz8 = verificar_acima2 matriz7

      --verificar_abaixo
      matriz9 = verificar_abaixo matriz8

      --condicoes de parada
      condicao = condicaoParada matriz9
      n_iteracoes = incrementador n_loop
  --putStrLn ("iteração nº: " ++ show n_iteracoes)
  
  --print_matriz matriz9
  
  case (condicao || n_iteracoes == 10) of
    True -> return (n_iteracoes, matriz9)
    False -> loop matriz9 n_iteracoes

incrementador :: Int -> Int
incrementador n = n + 1

--se existir ao menos um elemento com valor igual a zero retorna false
condicaoParada :: [[Elemento]] -> Bool
condicaoParada matriz = all (all (\e -> valor e /= 0)) matriz

main :: IO ()
main = do
    print("Matriz de entrada: ")
    print_matriz matriz
    putStrLn ""

    (n_iteracoes, matriz_resolvida) <- loop matriz 0
    print("Matriz resolvida: ")
    print_matriz matriz_resolvida
    putStrLn ("Nº de iterações: " ++ show n_iteracoes)