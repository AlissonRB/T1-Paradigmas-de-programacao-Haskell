from kojun_entrys import exemplo1, areas, matriz


'''
1- Um número do intervalo 1~N deve ser inserido em cada campo de uma área 
composta por N campos.
2- Cada número deve ser usado exatamente uma vez.
3- Números em campos ortogonalmente adjacentes devem ser diferentes.
4- Se dois quadrados na mesma área forem verticalmente adjacentes, o número 
no quadrado superior deve ser maior que o número no inferior.
'''

'''Define Methods:
    -Caso de área coluna: Preencher de cima pra baixo em ordem decrescente 
    ou de baixo pra cima em ordem crescente
    -Caso de área tamanho 1: único valor possível é 1.
    -Caso em que faltam 2 casas para completar área: Verificar se é 
    possível adicionar um número em uma casa, se não puder, poder já 
    ter o mesmo número em casas adjacentes, então só cabe colocar o outro
    -Aperfeiçoamento: verificar todas as casas adjacentes da casa atual, 
    se sobrar apenas 1 possibilidade de número para ser inserido
    então a resposta é esse número
    -Se a casa de baixo pertence a mesma área, o número 1 não pode ser 
    inserido nessa casa
    -Se um número que não foi adicionado ainda à area só pode ser 
    colocado em uma casa, ou seja, ele só pertence a lista de possibilidades
    de uma casa, então ele deve ser inserido nela.
    '''

def complete_2(elemento):
    if elemento.tam_area == 2 and not elemento.area_complete:
        #buscar completar adjacente:
        if valor == 0 and len(areas[elemento.id_area-100][-1]) == 1: # se na casa possui zero e apenas 1 possível valor 
            valor = 1
            exemplo1[elemento.cord[0], elemento.cord[1]][0] = 1 # atribui o 1 a aquela casa na matriz
    return True

def verificar_abaixo(elemento):
    if areas[elemento.id_area-100][-1][0] == 1:  # Se 1 ainda é um número possível.
        x = elemento.cord[0]
        y = elemento.cord[1]
        if y < elemento.tam_area: # evita index_error
            if exemplo1[x][y+1][2] == elemento.id_area:
                elemento.valores_possiveis.remove(1)
        

def area_1(elemento):
    if elemento.tam_area == 1:
        elemento.valor = 1
    return True

for i in range(len(matriz)):
    print(f"{i+1}: ", end='')
    for j in range(len(matriz)):
        print(matriz[i][j].valor,',' if j < len(matriz)-1 else '', end='' if j < len(matriz)-1 else '\n')

complete = False
while not complete:
    achou_incompleto = False
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if (matriz[i][j]).trySolve():
                print()
                print(f"i = {i}; j = {j}")
                for i in range(len(matriz)):
                    print(f"{i+1}: ", end='')
                    for j in range(len(matriz)):
                        print(matriz[i][j].valor,',' if j < len(matriz)-1 else '', end='' if j < len(matriz)-1 else '\n')
            else:
                if matriz[i][j].valor == 0:
                    complete = False
                    achou_incompleto = True
    if not achou_incompleto:
        complete = True
    for i in range(len(matriz)):
        print(f"{i+1}: ", end='')
        for j in range(len(matriz)):
            print(matriz[i][j].valor,',' if j < len(matriz)-1 else '', end='' if j < len(matriz)-1 else '\n')

        


'''for i in range(len(matriz)):
        print(f"{i+1}: ", end='')
        for j in range(len(matriz)):
            print(matriz[i][j].valor,',' if j < len(matriz)-1 else '', end='' if j < len(matriz)-1 else '\n')
'''