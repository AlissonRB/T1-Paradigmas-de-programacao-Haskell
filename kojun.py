from kojun_entrys import matriz


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

complete = False
while not complete:
    #Sempre que entra nesse loop(while) define que não achou uma casa incompleta ainda
    achou_incompleto = False
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if (matriz[i][j]).trySolve():
                print()
                print(f"i = {i}; j = {j}")
                for x in range(len(matriz)):
                    print(f"{x+1}: ", end='')
                    for y in range(len(matriz)):
                        print(f"{matriz[x][y].valor}, {',' if y < len(matriz)-1 else ''}", end='' if y < len(matriz)-1 else '\n')
            else:
                #uma vez achado uma casa incompleta, o valor acho_incompleto se torna verdadeiro e assim continuará até outra interação do while
                if matriz[i][j].valor == 0:
                    complete = False
                    achou_incompleto = True
    # Se tiver varrido a matriz e não achou nenhum zero nela então a matriz está completa
    if not achou_incompleto:
        complete = True
        print()
        print("Matriz esperada:")
        for i in range(len(matriz)):
            print(f"{i+1}: ", end='')
            for j in range(len(matriz)):
                print(matriz[i][j].valor,',' if j < len(matriz)-1 else '', end='' if j < len(matriz)-1 else '\n')
