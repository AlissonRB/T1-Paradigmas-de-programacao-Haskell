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

-- seta true em area_complete para o elemento que tiver o valor diferente de zero
atualizar_area_complete :: [[Elemento]] -> [[Elemento]]
atualizar_area_complete matriz = map (map atualizar_elemento) matriz
    where
      atualizar_elemento elem@(Elemento v c i t ac vp)
        | v /= 0 = Elemento v c i t True vp
        | otherwise = elem

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