class Elemento:
    def __init__(self, valor:int, cord:list, id_area:int, tam_area:int, area_complete:bool, valores_possiveis:list):
        self.valor = valor #valor int da casa
        self.cord = cord # tupla de valores referentes a linha e coluna do elemento na matriz --> (x, y)
        self.id_area = id_area # id da area, usado para acessar os elementos de uma mesma área 
        self.tam_area = tam_area # valor int que informa o tamanho da área, utilizado para saber quais números podem ser inseridos ali
        self.area_complete = area_complete  
        self.valores_possiveis = valores_possiveis  # lista de valores possíveis para aquela casa(célula)

    def complete_unico(self):
        '''Função que ve se a quantidade de valores_possiveis pra serem inseridos naquela célula é 1, se for, o insere nela.'''
        if self.valor == 0:
            if len(self.valores_possiveis) == 1: # se na casa possui zero e apenas 1 possível valor 
                self.setCell(self.valores_possiveis[0])
                return True
        return False
    


    def tirar_possibilidades(self):
        x = self.cord[0]
        y = self.cord[1]
        if y != 0:
            #esquerda
            esquerda = matriz[x][y-1]
            try:
                if esquerda.valor == 0:
                    esquerda.valores_possiveis.remove(self.valor) 
                    esquerda.complete_unico()
            except ValueError:
                esquerda.complete_unico()
        if y < len(matriz)-1:
            #direita
            direita = matriz[x][y+1]
            try:
                if direita.valor == 0:
                    direita.valores_possiveis.remove(self.valor)
                    direita.complete_unico()
            except ValueError:
                direita.complete_unico()
        if x != 0:
            #cima
            acima = matriz[x-1][y]
            try:
                if acima.valor == 0:
                    acima.valores_possiveis.remove(self.valor)
                    acima.complete_unico()
            except ValueError:
                acima.complete_unico()
        if x < len(matriz)-1:
            #baixo
            abaixo = matriz[x+1][y]
            try:
                if abaixo.valor == 0:
                    abaixo.valores_possiveis.remove(self.valor)
                    abaixo.complete_unico()
            except ValueError:
                abaixo.complete_unico()

        for elemento in areas[self.id_area-100]:
            if type(elemento) != list:
                if self.valor in elemento.valores_possiveis:
                    elemento.valores_possiveis.remove(self.valor)
        areas[self.id_area-100][-1].append(self.valor)
    
    def verificar_acima(self):
        # Nessa função são realizados dois procedimentos, um caso o valor acima seja diferente e 0 e outro caso contrário.
        x = self.cord[0]
        y = self.cord[1]
        if x != 0 : # evita index_error
            acima = matriz[x-1][y]
            if acima.valor != 0:
                if acima.id_area == self.id_area:
                    '''Primeiro: É criado uma lista chamada de 'possiveis' para armazenar os valores que aquela casa pode assumir com base no valor da casa acima,
                    ou seja, dos valores presentes em 'valores_possiveis', só poderam ser inseridos naquela casa aqueles que são menores do que o valor da casa
                    acima, já que um valor menor acima de outro maior(na mesma área) não é permitido'''
                    possiveis  = [z for z in self.valores_possiveis if z < acima.valor]
                    if len(possiveis) == 1:
                        self.valores_possiveis.remove(possiveis[0])
                        self.setCell(possiveis[0])
                        return True
            else:
                '''Segundo: Caso o valor acima seja 0 e a casa acima seja da mesma área que a casa atual, significa que o valor acima necessariamente precisa ser
                maior que o valor da casa atual, então é verificado se caso tirarmos o maior valor de 'valores_possiveis' resta apenas um valor possível, então ele
                é o único possível de ser inserido naquela casa, e consequentemento o valor maior que foi retirado é o da casa acima'''
                if acima.id_area == self.id_area:
                    possiveis = self.valores_possiveis
                    possiveis.pop()
                    if len(possiveis) == 1:
                        self.setCell(possiveis[0])
                        return True
        return False
        
    def verificar_abaixo(self):
        x = self.cord[0]
        y = self.cord[1]
        if x < len(matriz)-1:
            abaixo = matriz[x+1][y]
            if abaixo.id_area == self.id_area:
                # O valor abaixo é 1 a menos que o maior possivel pra aquela célula
                if abaixo.valor == self.valores_possiveis[-1] -1:
                    self.setCell(self.valores_possiveis[-1])
                    return True
                #O valor abaixo é um a menos que o tamanho da matriz:
                if abaixo.valor == self.tam_area - 1:
                    self.setCell(self.valores_possiveis[-1])
        return False
        
    #No caso em que a área tem tamanho 1, só pode ser inserido o número 1 naquela casa
    def area_1(self):
        if self.tam_area == 1:
            self.setCell(1)
            self.area_complete = True
            return True
        return False
    
    def last_possible(self):
        area = areas[self.id_area-100] # define variável 'area' como a area atual daquela célula
        '''Define um contador que é uma lista composta por 0 do tamanho da área, sou seja, a função vai varrer todos os elementos presentes naquela área
        e caso algum número só possa ser inserido em uma célula, ou seja, ou verificar os 'valores_possiveis' de todas as células um número só aparece nessas listas
        de valores possiveis apenas uma vez, então ele só pode ser inserido naquela célula, de acordo com o progresso do algoritmo que foi tirando as possibilidades
        de alguns números estarem estarem em certas casas devido às regras do jogo'''
        cnt = [0]*self.tam_area
        #Exemplo(matriz 6x6): cnt = [0, 1, 2, 0, 2, 0] quer dizer que o numero 2(segunda posição) só pode ser inserido em uma celula
        for elemento in area:
            if type(elemento) != list:
                for valor in elemento.valores_possiveis:
                    cnt[valor-1] += 1
        for numero in cnt:
            if numero == 1:
                for elemento in area:
                    if cnt.index(numero)+1 in elemento.valores_possiveis:
                        elemento.setCell(cnt.index(numero)+1) 
                        return True
        return False
            
    def area_coluna(self):
        area = areas[self.id_area -100]
        x = self.cord[0]
        y = self.cord[1]
        lista_x = []
        lista_y = []
        for elemento in area:
            if type(elemento) != list:
                lista_x.append(elemento.cord[0])
                lista_y.append(elemento.cord[1])
        lista_x.sort()
        lista_y.sort()
        #verifica se é coluna
        for i in range(len(area)-2):
            if lista_x[i] == lista_x[i+1] -1:
                if lista_y[i] == lista_y[i+1]:
                    continue
                else:
                    return False
            else:
                return False
        #Se chegou aqui é area_coluna
        for i in range(len(area)-1):
            '''Como se for area_coluna o y é igual para todos, e o x aumenta 
            em lista_x, pois foi ordenada, insere já nas regras do programa'''
            matriz[lista_x[i]][lista_y[i]].valor = len(area) - i -1
            matriz[lista_x[i]][lista_y[i]].area_complete = True
        return True
    
    def trySolve(self):
        if self.valor == 0:
            if self.complete_unico():
                return True
            if self.area_1():
                return True 
            if self.area_coluna():
                return True
            if self.verificar_acima():
                return True
            if self.verificar_abaixo():
                return True
            if self.last_possible():
                return True
        #self.tirar_possibilidades()
        return False

    def setCell(self, valor):
        x = self.cord[0]
        y = self.cord[1]
        #Verifica se em nenhuma das casas adjacentes já possui o valor que se deseja inserir
        if y != 0:
            #esquerda
            if matriz[x][y-1].valor != valor:
                pass
            else:
                return 
        if y < len(matriz)-1:
            #direita
            if matriz[x][y+1].valor != valor: 
                pass
            else:
                return
        if x != 0:
            #acima

            if matriz[x-1][y].valor != valor:
                pass
            else:
                return
        if x < len(matriz)-1:
            #abaixo
            if matriz[x+1][y].valor != valor:
                pass
            else:
                return
        self.valor = valor
        self.valores_possiveis = []
        self.tirar_possibilidades()
    
def instancia_exemplo(entry):
    #Cria uma matriz de tamanho len(entrada) x len(entrada), composta por 0, que serão substituídos futuramente pelos objetos referentes
    matriz = [[0 for i in range(len(entry))] for i in range(len(entry))]

    
    for i in range(len(entry)):
        for j in range(len(entry)):
            casa = Elemento(*list(entry[i][j]))
            matriz[i][j] = casa
            areas[entry[i][j][2]-100].append(matriz[i][j])
    return matriz


#exemplo1 - 6x6

exemplo1 = [[(2, (0, 0), 100, 2, False, []), (0 , (0, 1), 100, 2, False, []), (0, (0, 2), 101, 3, False, []), (0, (0, 3), 101, 3, False, []), (1, (0, 4), 101, 3, False, []), (0, (0, 5), 102, 2, False, [])],
 [(0, (1, 0), 103, 6, False, []), (0, (1, 1), 103, 6, False, []), (0, (1, 2), 103, 6, False, []), (3, (1, 3), 103, 6, False, []), (0, (1, 4), 103, 6, False, []), (0, (1, 5), 102, 2, False, [])],
 [(0, (2, 0), 104, 4, False, []), (3, (2, 1), 105, 4, False, []), (0, (2, 2), 105, 4, False, []), (0, (2, 3), 105, 4, False, []), (5, (2, 4), 103, 6, False, []), (3, (2, 5), 106, 3, False, [])],
 [(0, (3, 0), 104, 4, False, []), (0, (3, 1), 104, 4, False, []), (0, (3, 2), 104, 4, False, []), (0, (3, 3), 105, 4, False, []), (0, (3, 4), 106, 3, False, []), (0, (3, 5), 106, 3, False, [])],
 [(0, (4, 0), 107, 2, False, []), (0, (4, 1), 107, 2, False, []), (3, (4, 2), 109, 3, False, []), (0, (4, 3), 110, 5, False, []), (4, (4, 4), 110, 5, False, []), (2, (4, 5), 110, 5, False, [])],
 [(0, (5, 0), 108, 2, False, []), (0, (5, 1), 108, 2, False, []), (0, (5, 2), 109, 3, False, []), (0, (5, 3), 109, 3, False, []), (0, (5, 4), 110, 5, False, []), (0, (5, 5), 110, 5, False, [])]]

#matriz = [[0 for i in range(len(exemplo1))]for i in range(len(exemplo1))]
#print(matriz)

#kojun12
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


#Exemplo1
#qnt_areas = 11
#Exemplo2
qnt_areas = 27

areas = [[]for i in range(qnt_areas)]

matriz = instancia_exemplo(exemplo2)
for area in areas:
    #adiciona lista na lista de areas que informa os números que estão presentes naquela área
    valores_possiveis = []
    for elemento in area:
        #passa inserindo os elementos já presentes naquela área
        if elemento.valor != 0:
            valores_possiveis.append(elemento.valor) 
    area.append(valores_possiveis)



#Varre a matriz escrevendo a lista de valores possíveis pra cada célula
for i in range(len(matriz)):
    for j in range(len(matriz)):
        #Se alguma celula já tiver valor, a lista de valores possíveis é vazia
        if matriz[i][j].valor == 0:
            #loop de 1 ao tamanho da matriz, caso k não esteja na area ainda é inserido à lista de 'valores_possiveis' daquela célula.
            for k in range(1, matriz[i][j].tam_area +1):
                if k not in areas[matriz[i][j].id_area - 100][-1]:
                    matriz[i][j].valores_possiveis.append(k)


print()
print("Matriz inicial:")
for i in range(len(matriz)):
    print(f"{i+1}: ", end='')
    for j in range(len(matriz)):
        print(matriz[i][j].valor,',' if j < len(matriz)-1 else '', end='' if j < len(matriz)-1 else '\n')


'''Varre a matriz executando a função tirar_possibilidades em todos os elementos que já foram previamente inseridos no arquivo de entrada, ou seja, sao diferentes de 
0 por padrão'''
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j].valor != 0:
            matriz[i][j].tirar_possibilidades()

print()
print("Matriz após executar tirar_possibilidades() nos números que vem por padrão na matriz:")
for i in range(len(matriz)):
    print(f"{i+1}: ", end='')
    for j in range(len(matriz)):
        print(matriz[i][j].valor,',' if j < len(matriz)-1 else '', end='' if j < len(matriz)-1 else '\n')
