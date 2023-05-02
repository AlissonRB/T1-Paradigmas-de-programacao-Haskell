data Elemento = Elemento {
  valor :: Int, -- valor int da casa
  cord :: (Int, Int), -- tupla de valores referentes a linha e coluna do elemento na matriz --> (x, y)
  id_area :: Int, -- id da area, usado para acessar os elementos de uma mesma área 
  tam_area :: Int, -- valor int que informa o tamanho da área, utilizado para saber quais números podem ser inseridos ali
  area_complete :: Bool,
  valores_possiveis :: [Int] -- lista de valores possíveis para aquela casa(célula)
}

completeUnico :: Elemento -> Bool
--Função que ve se a quantidade de valores_possiveis pra serem inseridos naquela célula é 1, se for, o insere nela
completeUnico elemento
  | valor elemento == 0 && length (valores_possiveis elemento) == 1 = True
  | otherwise = False

verificarAcima :: Elemento -> [[Elemento]] -> Bool
verificarAcima elemento matriz = do
  let x = fst (cord elemento)
  let y = snd (cord elemento)
  let matrizLen = length matriz
  
  if x /= 0 then -- evita index_error
    let acima = matriz !! (x - 1) !! y
    if valor acima /= 0 && id_area acima == id_area elemento then
      -- possiveis  = [z for z in self.valores_possiveis if z < acima.valor]
      let possiveis = 
      if length possiveis == 1 then do
        -- ....

verificarAbaixo :: Elemento -> [[Elemento]] -> Bool
verificarAbaixo elemento matriz = do
  let x = fst (cord elemento)
  let y = snd (cord elemento)
  let matrizLen = length matriz

  if x < matrizLen - 1 then
    let abaixo = matriz !! (x + 1) !! y
    if id_area abaixo == id_area elemento then
      let ultimoValor = last (valores_possiveis elemento)
      if valor abaixo == ultimoValor - 1 then do
        let elementoAtualizado = elemento {
              valor = ultimoValor
            }
        substituirElemento matriz x (substituirElemento (matriz !! x) y elementoAtualizado)
        True
      else if valor abaixo == tam_area elemento - 1 then do
        let elementoAtualizado = elemento {
              valor = ultimoValor
            }
        substituirElemento matriz x (substituirElemento (matriz !! x) y elementoAtualizado)
        True
      else
        False
  else
    False

  where
    substituirElemento :: [[Elemento]] -> Int -> Elemento -> [[Elemento]]
    substituirElemento matriz indice elemento = take indice matriz ++ [elemento] ++ drop (indice + 1) matriz

area1 :: Elemento -> Bool
area1 elemento = do
  if tam_area elemento == 1 then do
    let elementoAtualizado = elemento {
          valor = 1,
          area_complete = True
        }
    True
  else
    False

trySolve :: Elemento -> Bool
trySolve elemento =
  if valor elemento == 0
    then completeUnico elemento || area_1 elemento || area_coluna elemento || verificar_acima elemento || verificar_abaixo elemento || last_possible elemento
    else False

setCell :: Elemento -> Int -> Elemento
setCell elemento valor = do
  let x = fst (cord elemento)
  let y = snd (cord elemento)

  if y /= 0 then do
    -- esquerda
    if valor /= valor (matriz !! x !! (y - 1)) then do
      ()
    else
      return elemento

  if y < length matriz - 1 then do
    -- direita
    if valor /= valor (matriz !! x !! (y + 1)) then do
      ()
    else
      return elemento

  if x /= 0 then do
    -- acima
    if valor /= valor (matriz !! (x - 1) !! y) then do
      ()
    else
      return elemento

  if x < length matriz - 1 then do
    -- abaixo
    if valor /= valor (matriz !! (x + 1) !! y) then do
      ()
    else
      return elemento

  let elementoAtualizado = elemento { valor = valor, valores_possiveis = [] }
  --  self.tirar_possibilidades()
  return elementoAtualizado


exemplo2 :: [[Elemento]]
exemplo2 = [[(4, (0, 0), 100, 4, False, []), (0, (0, 1), 100, 4, False, []), (4, (0, 2), 105, 4, False, []), (2, (0, 3), 105, 4, False, []), (0, (0, 4), 106, 2, False, []), (0, (0, 5), 106, 2, False, []), (6, (0, 6), 116, 7, False, []), (0, (0, 7), 118, 1, False, []), (7, (0, 8), 126, 7, False, []), (4, (0, 9), 126, 7, False, [])],
            [(3, (1, 0), 100, 4, False, []), (1, (1, 1), 100, 4, False, []), (0, (1, 2), 105, 4, False, []), (1, (1, 3), 116, 7, False, []), (0, (1, 4), 116, 7, False, []), (4, (1, 5), 116, 7, False, []), (0, (1, 6), 116, 7, False, []), (0, (1, 7), 119, 2, False, []), (0, (1, 8), 126, 7, False, []), (3, (1, 9), 126, 7, False, [])], 
            [(0, (2, 0), 101, 4, False, []), (0, (2, 1), 101, 4, False, []), (1, (2, 2), 105, 4, False, []), (0, (2, 3), 108, 2, False, []), (6, (2, 4), 113, 7, False, []), (0, (2, 5), 114, 2, False, []), (3, (2, 6), 116, 7, False, []), (0, (2, 7), 119, 2, False, []), (5, (2, 8), 126, 7, False, []), (2, (2, 9), 126, 7, False, [])], 
            [(0, (3, 0), 101, 4, False, []), (1, (3, 1), 101, 4, False, []), (0, (3, 2), 107, 2, False, []), (0, (3, 3), 108, 2, False, []), (4, (3, 4), 113, 7, False, []), (0, (3, 5), 114, 2, False, []), (0, (3, 6), 116, 7, False, []), (5, (3, 7), 125, 7, False, []), (0, (3, 8), 125, 7, False, []), (0, (3, 9), 126, 7, False, [])], 
            [(2, (4, 0), 102, 3, False, []), (0, (4, 1), 102, 3, False, []), (0, (4, 2), 107, 2, False, []), (7, (4, 3), 113, 7, False, []), (0, (4, 4), 113, 7, False, []), (3, (4, 5), 113, 7, False, []), (0, (4, 6), 115, 5, False, []), (3, (4, 7), 125, 7, False, []), (6, (4, 8), 125, 7, False, []), (2, (4, 9), 125, 7, False, [])], 
            [(0, (5, 0), 102, 3, False, []), (7, (5, 1), 103, 7, False, []), (0, (5, 2), 103, 7, False, []), (0, (5, 3), 113, 7, False, []), (0, (5, 4), 113, 7, False, []), (5, (5, 5), 115, 5, False, []), (3, (5, 6), 115, 5, False, []), (0, (5, 7), 120, 1, False, []), (0, (5, 8), 125, 7, False, []), (1, (5, 9), 125, 7, False, [])], 
            [(0, (6, 0), 103, 7, False, []), (3, (6, 1), 103, 7, False, []), (0, (6, 2), 103, 7, False, []), (6, (6, 3), 103, 7, False, []), (3, (6, 4), 112, 6, False, []), (0, (6, 5), 115, 5, False, []), (2, (6, 6), 115, 5, False, []), (6, (6, 7), 112, 6, False, []), (2, (6, 8), 122, 4, False, []), (0, (6, 9), 122, 4, False, [])], 
            [(4, (7, 0), 104, 5, False, []), (2, (7, 1), 103, 7, False, []), (0, (7, 2), 109, 4, False, []), (0, (7, 3), 110, 4, False, []), (0, (7, 4), 112, 6, False, []), (5, (7, 5), 112, 6, False, []), (0, (7, 6), 112, 6, False, []), (0, (7, 7), 112, 6, False, []), (4, (7, 8), 121, 6, False, []), (3, (7, 9), 122, 4, False, [])], 
            [(2, (8, 0), 104, 5, False, []), (5, (8, 1), 104, 5, False, []), (0, (8, 2), 109, 4, False, []), (1, (8, 3), 110, 4, False, []), (2, (8, 4), 110, 4, False, []), (0, (8, 5), 110, 4, False, []), (2, (8, 6), 111, 4, False, []), (0, (8, 7), 121, 6, False, []), (3, (8, 8), 121, 6, False, []), (0, (8, 9), 122, 4, False, [])], 
            [(1, (9, 0), 104, 5, False, []), (0, (9, 1), 104, 5, False, []), (0, (9, 2), 109, 4, False, []), (2, (9, 3), 109, 4, False, []), (4, (9, 4), 111, 4, False, []), (0, (9, 5), 111, 4, False, []), (1, (9, 6), 111, 4, False, []), (2, (9, 7), 121, 6, False, []), (0, (9, 8), 121, 6, False, []), (5, (9, 9), 121, 6, False, [])]]