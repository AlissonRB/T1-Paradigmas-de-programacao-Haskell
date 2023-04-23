

def transforma_arquivo_para_matriz():
    #nome_arquivo = input("Digite o nome do arquivo")
    nome_arquivo = "matriz.txt"
    matriz = []
    with open (nome_arquivo, 'r') as f:
        conteudo = eval(f.read())
        for lista in conteudo:
            matriz.append(lista)
    return matriz

#separa a matriz em uma lista de regioes, para entao em outra funcao criar as regioes
def separar_regioes(matriz):

    #matriz com as listas:[x,y,valor,regiao]
    matriz_aux = []

    for lista in matriz:
        for tupla in lista:
            matriz_aux.append(tupla)
    regioes = []
    while len(matriz_aux) !=0:
        
        #se pega o id_regiao da tupla([x,y,valor,regiao]) e associa a uma regiao, quando fizer isso apaga a tupla da matriz
        id_regiao = matriz_aux[0][3]
        nova_regiao = []
        #para cada tupla na matriz
        #vai montar uma regiao com todas as tuplas com o mesmo identificador
        for lista in matriz_aux:
            if lista[3] == id_regiao:
                nova_regiao.append(lista)
                #matriz_aux.remove(lista)
        matriz_aux = [lista for lista in matriz_aux if lista[3] != id_regiao]
        regioes.append(nova_regiao)
    return regioes

def criar_regioes(lista_regioes):
    #regiao = [casas da regiao] [casas disponiveis] [numeros regiao] [numeros faltantes]
    #[x,y,valor,regiao]

    #lista de informaçoes de cada regiao
    info_regioes = []

    for regiao in lista_regioes:
        casas_regiao = []
        casas_disponiveis = []
        numeros_regiao = []
        numeros_faltantes = []

        #info_regiao = [[casas da regiao], [casas disponiveis], [numeros regiao] [numeros faltantes]]
        info_regiao = []

        #cria lista de numeros da regiao
        for i in range(1,len(regiao)+1):
            numeros_regiao.append(i)
        
        #criar lista de numeros faltantes
        numeros_ja_tem = []
        numeros_faltantes = numeros_regiao.copy()

        for casa in regiao:
            #vai preencher a lista de casas da regiao
            coordenada = []
            coordenada.append(casa[0])
            coordenada.append(casa[1])
            casas_regiao.append(coordenada)
            
            #casa sem valor
            if casa[2] == 0:
                casas_disponiveis.append(coordenada)
            if casa[2] !=0:
                num = casa[2]
                numeros_ja_tem.append(casa[2])
        
        for numero in numeros_ja_tem:
            numeros_faltantes.remove(numero)

        info_regiao.append(casas_regiao)
        info_regiao.append(casas_disponiveis)
        info_regiao.append(numeros_regiao)
        info_regiao.append(numeros_faltantes)
        info_regioes.append(info_regiao)
    
    #print(info_regioes[0])
    return info_regioes

def printar_matriz(matriz):
    for lista in matriz:
        print(lista)

def printar_tabuleiro(matriz):
    print("-----------------------")
    for lista in matriz:
        for i in range(len(lista)):
            print(lista[i][2], end= " ")
        print("\n")
    print("-----------------------")

def verificar_entrada(entrada):
    pass

#recebe a matriz, as coordenadas e o valor para colocar nessa coordenada
def atualiza_matriz(matriz,x,y,valor):
    for lista in matriz:
            for coordenada in lista:
                if coordenada[0] == x and coordenada[1] == y:
                    #atualiza o valor da casa
                    coordenada[2] = valor
    return(matriz) 

#para cada numero restante na regiao, vai analisar se o numero tem apenas uma casa possivel para ir
def uma_casa_possivel(regioes, matriz):
    #até aqui tenho:
    # -matriz com as listas:[x,y,valor,regiao]
    # regioes: uma lista de regioes, com cada regiao = [casas da regiao] [casas disponiveis] [numeros regiao] [valor faltantes]    
    # #agora resolve por regiao
    #usar a matriz para achar os vizinhos

# para cada regiao na lista de regioes:
#para cada numero na lista de [numeros faltantes]  dessa regiao
#pega um numero e para esse numero
#copia a lista de coordenadas restantes em uma coordenadas_restantes_aux
#para cada coordenada restante:
#usa a matriz original para achar os vizinhos nessa coordenada
#analisa se para aquela coordenada existe algum vizinho ortogonal que tenha valor igual ao numero e se existir remove essa coordenada na lista daquele numero
#quando restar apenas uma coordenada possivel para o numero, coloca esse numero na coordenada da matriz

#se p/ essa coordenada um dos vizinhos tiver valor igual ao numero, exclui a coordenada da lista aux
#quando restar apenas uma coordenada, associa o numero a essa coordenada, e salva na matriz original

#apos colocar um valor na matriz
#atualiza a matriz
#atualiza a regiao
#faz isso até que nao restem mais numeros_restantes
#vizinho vai ser o valor da celula retornado

    #print(regioes[0][3]) = [1, 3, 4, 5, 7]
    #regiao = [casas da regiao] [casas disponiveis] [numeros regiao] [numeros faltantes] 
    #talvez colocar verificação para quando a lista ja esta vazia , e nao vai percorrer uma lista vazia
    for regiao in regioes:
        
        
        #se tiver apenas uma casa disponivel na regiao, coloca o numeor restante nela
        if len(regiao[1]) == 1:

            #atualiza matriz
            #x e y da coordenada
            x = regiao[1][0][0]
            y = regiao[1][0][1]
            valor = regiao[3][0]  #talvez aqui de um erro]
            matriz = atualiza_matriz(matriz,x,y,valor)
    
            #atualiza regiao
            regiao[1].pop() #remover o ultimo elemento da lista
            regiao[3].pop() #remover o ultimo numero da lista
            # regiao[3].remove(numero)  #ou talvez

        #senao para cada numeros na lista de numeros restantes
        #vai analisar para cada casa, se aquele numero pode ser colocado ali, senao puder entao apaga a casa nas opcoes do numero
        #quando restar apenas uma casa para o numero coloca ele ali
        else:
            #lista de valores para remover, remover apenas no final os numeros alterados para evitar um possivel problema
            valores_remover = []
            #para cada numero na lista de numeros restantes
            #regiao = [casas da regiao] [casas disponiveis] [numeros regiao] [valor faltantes]
            #se ainda tiver valores restantes a serem considerados
            if regiao[3] != 0:
                for numero in regiao[3]:
                    #contem as casas disponiveis dessa regiao
                    casas_disponiveis_aux = regiao[1].copy()
                    for casa in casas_disponiveis_aux:
                        #casa = [x, y]

                        #coordenadas da casa que vai ser analisada
                        x = casa[0]
                        y = casa[1]

                        #coordenada casa de cima
                        x_cima = x
                        if y == 0:
                            y_cima = -1  #vizinho de cima nao existe, y de cima nao existe
                        else:
                            y_cima = y-1

                        #coordenada casa de baixo
                        x_baixo = x
                        if y == 9:
                            y_baixo = -1
                        else:
                            y_baixo = y +1
                        
                        #coordenada casa do lado direito
                        y_direito = y
                        if x == 9:
                            x_direito = -1
                        else:
                            x_direito = x + 1
                        
                        #coordenada casa do lado esquerdo
                        y_esquerdo = y
                        if x == 0:
                            x_esquerdo = -1
                        else:
                            x_esquerdo = x-1
                        
                        #varrer a matriz original para procurar os vizinhos, quando achar vai ter o valor das casas vizinhas
                        valor_vizinho_cima = -1
                        valor_vizinho_baixo = -1
                        valor_vizinho_direito = -1
                        valor_vizinho_esquerdo = -1

                        for lista in matriz:
                            for i in lista:

                                if i[0] == x_cima and i[1] == y_cima:
                                    #vizinho é igual ao valor
                                    valor_vizinho_cima = i[2]
                                
                                elif i[0] == x_baixo and i[1] == y_baixo:
                                    #vizinho é igual ao valor
                                    valor_vizinho_baixo = i[2]
                                
                                elif i[0] == x_direito and i[1] == y_direito:
                                    #vizinho é igual ao valor
                                    valor_vizinho_direito= i[2]
                                
                                elif i[0] == x_esquerdo and i[1] == y_esquerdo:
                                    #vizinho é igual ao valor
                                    valor_vizinho_esquerdo = i[2]

                        #se o numero for igual a qualquer valor dos vizinhos ortogonais da casa entao essa casa nao pode ser considerada
                        if numero == valor_vizinho_cima:
                            casas_disponiveis_aux.remove(casa)
                        elif numero == valor_vizinho_baixo:
                            casas_disponiveis_aux.remove(casa)
                        elif numero == valor_vizinho_direito:
                            casas_disponiveis_aux.remove(casa)
                        elif numero == valor_vizinho_esquerdo:
                            casas_disponiveis_aux.remove(casa)
                        #quando para aquele numero restar apenas uma coordenada na lista de coordenadas_aux entao atualiza
                        #senao vai para o outro numero
                        #sempre que colocar um numero na coordenada é importante atualizar todas as informações antes de procurar para um outro numero

                        #entao só restou uma casa possivel para o numero
                        #fazer a verificacao se restar apenas uma casa_disponivel
                        if len(casas_disponiveis_aux) == 1:
                            #atualiza a matriz
                            atualiza_matriz(matriz,x,y,numero)
                            #atualiza regiao
                            #regiao = [casas da regiao] [casas disponiveis] [numeros regiao] [valor faltantes]
                            
                            regiao[1].remove(casas_disponiveis_aux[0]) #remover o ultimo elemento da lista
                            valores_remover.append(numero)
                            #regiao[3].pop() #remover o ultimo numero da lista de numeros restantes
                        
                        #ate aqui pode acontecer duas coisas:
                        #nada: caso len(casas_disponiveis_aux) != 1
                        #ou vai atualizar a matriz e a regiao
                        #se fizer algum tipo de atualizacao na regiao, recomeça nela com as lista atualizada
        
            for n in valores_remover:
                regiao[3].remove(n)

    return(regioes,matriz)

def preencher_coluna_crescente():
    pass

def resolver_kojun():

    matriz = transforma_arquivo_para_matriz()
    lista_regioes = separar_regioes(matriz)

    # regioes: uma lista de regioes, com cada regiao = [casas da regiao] [casas disponiveis] [numeros regiao] [numeros faltantes]
    regioes = criar_regioes(lista_regioes)

    print("Tabuleiro inserido: ")
    printar_tabuleiro(matriz)
    regioes, matriz = uma_casa_possivel(regioes, matriz)
    regioes, matriz = uma_casa_possivel(regioes, matriz)
    print("Tabuleiro resolvido: ")
    printar_tabuleiro(matriz)  


#kojun nº43
resolver_kojun()







