class Elemento:
    def __init__(self, valor:int, cord:list, id_area:int, tam_area:int, area_complete:bool, valores_possiveis:list):
        self.valor = valor
        self.cord = cord
        self.id_area = id_area
        self.tam_area = tam_area
        self.area_complete = area_complete
        self.valores_possiveis = valores_possiveis

    def complete_2(self):
        if self.tam_area == 2 and not self.area_complete:
            area = areas[self.id_area-100]
            #buscar completar adjacente:
            if self.valor == 0:
                if len(area[-1]) == 1: # se na casa possui zero e apenas 1 possível valor 
                    self.setCell(area[-1])
                #elif len(area[-1]) == 2:
    
    def complete_unico(self):
        area = areas[self.id_area-100]
        #buscar completar adjacente:
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
            try:
                if matriz[x][y-1].valor == 0:
                    matriz[x][y-1].valores_possiveis.remove(self.valor) 
                    if len(matriz[x][y-1].valores_possiveis) == 1:
                        matriz[x][y-1].setCell(matriz[x][y-1].valores_possiveis[0])
            except ValueError:
                if len(matriz[x][y-1].valores_possiveis) == 1:
                    matriz[x][y-1].setCell(matriz[x][y-1].valores_possiveis[0])
        if y < len(matriz)-1:
            #direita
            try:
                if matriz[x][y+1].valor == 0:
                    matriz[x][y+1].valores_possiveis.remove(self.valor)
                    if len(matriz[x][y+1].valores_possiveis) == 1:
                        matriz[x][y+1].setCell(matriz[x][y+1].valores_possiveis[0])
            except ValueError:
                if len(matriz[x][y+1].valores_possiveis) == 1:
                    matriz[x][y+1].setCell(matriz[x][y+1].valores_possiveis[0])
        if x != 0:
            #cima
            try:
                if matriz[x-1][y].valor == 0:
                    matriz[x-1][y].valores_possiveis.remove(self.valor)
                    if len(matriz[x-1][y].valores_possiveis) == 1:
                        matriz[x-1][y].setCell(matriz[x-1][y].valores_possiveis[0])
            except ValueError:
                if len(matriz[x-1][y].valores_possiveis) == 1:
                    matriz[x-1][y].setCell(matriz[x-1][y].valores_possiveis[0])
        if x < len(matriz)-1:
            #baixo
            try:
                if matriz[x+1][y].valor == 0:
                    matriz[x+1][y].valores_possiveis.remove(self.valor)
                    if len(matriz[x+1][y].valores_possiveis) == 1:
                        matriz[x+1][y].setCell(matriz[x+1][y].valores_possiveis[0])
            except ValueError:
                if len(matriz[x+1][y].valores_possiveis) == 1:
                    matriz[x+1][y].setCell(matriz[x+1][y].valores_possiveis[0])
        for elemento in areas[self.id_area-100]:
            if type(elemento) != list:
                if self.valor in elemento.valores_possiveis:
                    elemento.valores_possiveis.remove(self.valor)
        areas[self.id_area-100][-1].append(self.valor)
    
    def verificar_acima(self):
        x = self.cord[0]
        y = self.cord[1]
        if matriz[x-1][y].valor != 0:
            if x != 0 : # evita index_error
                if matriz[x-1][y].id_area == self.id_area:
                    possiveis  = [x for x in self.valores_possiveis if x < matriz[x-1][y].valor]
                    if len(possiveis) == 1:
                        self.valores_possiveis.remove(possiveis[0])
                        self.setCell(possiveis[0])
                        return True
        return False
        
    def verificar_abaixo(self):
        x = self.cord[0]
        y = self.cord[1]
        if x < len(matriz)-1:
            if matriz[x+1][y].id_area == self.id_area:
                if matriz[x+1][y].valor == self.valores_possiveis[-1] -1:
                    self.setCell(self.valores_possiveis[-1])
                    return True
        return False
        
    def area_1(self):
        if self.tam_area == 1:
            self.setCell(1)
            self.area_complete = True
            return True
        return False
    
    def last_possible(self):
        area = areas[self.id_area-100]
        cnt = [0]*self.tam_area
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
        if y != 0:
            if matriz[x][y-1].valor != valor:
                pass
            else:
                return 
        if y < len(matriz)-1:
            if matriz[x][y+1].valor != valor: 
                pass
            else:
                return
        if x != 0:
            if matriz[x-1][y].valor != valor:
                pass
            else:
                return
        if x < len(matriz)-1:
            if matriz[x+1][y].valor != valor:
                pass
            else:
                return
        self.valor = valor
        self.valores_possiveis = []
        self.tirar_possibilidades()
    
#exemplo1 - 6x6
'''
area100 = []
area101 = []
area102 = []
area103 = []
area104 = []
area105 = []
area106 = []
area107 = []
area108 = []
area109 = []
area110 = []
areas = [area100, area101, area102, area103, area104, area105, area106, area107, area108, area109, area110]
'''



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

qnt_areas = 27

areas = [[]for i in range(qnt_areas)]

def instancia_exemplo(entry):
    matriz = [[0 for i in range(len(entry))] for i in range(len(entry))]
    
    for i in range(len(entry)):
        for j in range(len(entry)):
            casa = Elemento(*list(entry[i][j]))
            matriz[i][j] = casa
            areas[entry[i][j][2]-100].append(matriz[i][j])
    return matriz

matriz = instancia_exemplo(exemplo2)
print(areas)
'''
for i in range(len(exemplo1)):
    for j in range(len(exemplo1)):
        #list(exemplo1[i][j]).append([])   #Adiciona lista de valores possiveis ao elemento
        casa = Elemento(*list(exemplo1[i][j])) #Instancia a celula da matriz como um elemento
        matriz[i][j]= casa
           #Adiciona a instancia na matriz
        areas[exemplo1[i][j][2]-100].append(matriz[i][j])
'''
print(matriz)
m = 0

for area in areas:
    #adiciona lista na lista de areas que informa os números que estão presentes naquela área
    valores_possiveis = []
    for elemento in area:
        #passa inserindo os elementos já presentes naquela área
        if elemento.valor != 0:
            valores_possiveis.append(elemento.valor) 
    area.append(valores_possiveis)
    print(f"area {m}")
    m += 1
    print(area)

print(matriz)
#Varre a matriz escrevendo a lista de valores possíveis pra cada célula
for i in range(len(matriz)):
    print("area antes")
    print(matriz[i])
    for j in range(len(matriz)):
        #Se alguma celula já tiver valor, a lista de valores possíveis é vazia
        if matriz[i][j].valor == 0:
            #loop de 1 ao tamanho da matriz
            for k in range(1, matriz[i][j].tam_area +1):
                if k not in areas[matriz[i][j].id_area - 100][-1]:
                    matriz[i][j].valores_possiveis.append(k)
    print("area depois")
    print(matriz[i])

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j].valor != 0:
            matriz[i][j].tirar_possibilidades()
        
for area in areas:
    print(area)