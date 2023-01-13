
dimensoes = input().split()
largura = int(dimensoes[0])
altura = int(dimensoes[1])
n_operacoes = int(input())
matriz = []
ha_selecao = False

def ler_matriz(altura):
    '''Lê a matriz original'''

    for _ in range(altura):
        linha = input().split(" ")
        matriz.append(linha)


def imprimir(matriz):
    '''Imprime a matriz convertida para inteiro'''
    
    for i in range(len(matriz)):

        for j in range(len(matriz[0]) - 1):

            valor = '{:0>3}'.format(int(matriz[i][j]))
            print (valor,  end=" ")
        
        print('{:0>3}'.format(int(matriz[i][j+1])))


def apagar_selecionada(matriz, canto_superior, altura, largura):
    ''' Transfora em 000 os pixels da região selecionada'''

    coord_i = canto_superior[0]

    for _ in range(coord_i, coord_i + altura):
        coord_j = canto_superior[1]

        for _ in range(coord_j, coord_j + largura):
            matriz[coord_i][coord_j] = '000'
            coord_j += 1
            
        coord_i += 1


def aplicar_matriz(matriz_alterada, canto_superior):
    ''' Recebe a matriz alterada por alguma das operações em uma seleção e retorna a matriz alterada
    unida à matriz original para o resultado final
    '''
    coord_i = canto_superior[0]

    for x in range(0, len(matriz_alterada)):
        coord_j = canto_superior[1]

        for y in range(0, len(matriz_alterada[0])):
            matriz[coord_i][coord_j] = matriz_alterada[x][y]
            coord_j += 1
            
        coord_i += 1


def selecao(matriz, canto_superior = [0,0], largura = 0, altura = 0):
    ''' Gera uma nova matriz chamada 'matriz selecao' que contém apenas os valores selecionados'''

    coord_i = canto_superior[0]
    coord_j = canto_superior[1]

    matriz_selecao = [linha[coord_j: coord_j + largura] for linha in matriz[coord_i: coord_i + altura]]

    global ha_selecao
    ha_selecao = True

    return matriz_selecao


def rotacao(matriz, altura, largura):
    ''' Rotaciona em 90 graus a matriz recebida'''

    nova_matriz = []

    for j in range(largura):
        nova_linha = []

        for i in range(-1, - altura - 1, -1):
            nova_linha.append(matriz[i][j])
                
        nova_matriz.append(nova_linha)

    return nova_matriz


def espelhamento(matriz, altura, largura, orientacao):
    ''' Espelha horizontalmente ou verticalmente a matriz recebida'''
    nova_matriz = []

    if orientacao == "v":
        for i in range(-1, - altura - 1, -1):
            nova_linha = []

            for j in range(largura):
                nova_linha.append(matriz[i][j])

            nova_matriz.append(nova_linha)
    else:
        for i in range(altura):
            nova_linha = []

            for j in range(-1, - largura -1, -1):
                nova_linha.append(matriz[i][j])

            nova_matriz.append(nova_linha)

    return nova_matriz

ler_matriz(altura)
canto_superior = [0, 0]
matriz_selecao = matriz

# Realizando as operações
for _ in range(n_operacoes):
    comando = input().split()
    operacao = comando[0]

    # Altera a matriz que será usada nas operações caso haja uma seleção
    if ha_selecao:
        matriz_opera = matriz_selecao

    else:
        matriz_opera = matriz

    if operacao == "rotacao":

        matriz_alterada = rotacao(matriz_opera, altura, largura)
        apagar_selecionada(matriz, canto_superior, altura, largura)
        aplicar_matriz(matriz_alterada, canto_superior)

    elif operacao == "espelhamento":
        
        orientacao = comando[1]
        matriz_alterada = espelhamento(matriz_opera, altura, largura, orientacao)
        aplicar_matriz(matriz_alterada, canto_superior)

    elif operacao == "selecao":

        canto_superior = [int(comando[2]), int(comando[1])]
        largura = int(comando[3])
        altura = int(comando[4])

    elif operacao == "copia":

        canto_superior_cola = [int(comando[2]), int(comando[1])]
        aplicar_matriz(matriz_selecao, canto_superior_cola)

    elif operacao == "recorte":

        canto_superior_corte = [int(comando[2]), int(comando[1])]
        apagar_selecionada(matriz, canto_superior, altura, largura)
        aplicar_matriz(matriz_selecao, canto_superior_corte)

    # Fazendo a seleção após efetuar uma operção
    matriz_selecao = selecao(matriz, canto_superior, largura, altura)

imprimir(matriz)