
from datetime import *

def add_estoque(estoque, entrada):
    ''' Adiciona um produto ao estoque'''

    estoque[entrada[1]] = [int(entrada[2]), entrada[3], float(entrada[4]), entrada[5]]


def remov_itens(estoque, entrada, caixa=0):
    ''' Remove os itens de acordo com o modo a partir do qual foi chamado
    
    Quando caixa = 0, obtém o índice 2, ou seja, a quantidade no modo estoque
    Quando caixa = 1, obtém o índice 1, ou seja, a quantidade no modo caixa
    '''
    if entrada[1-caixa] not in estoque:
        print("ERROR")
        return None

    else:
        qntd = int(entrada[2 - caixa])
        nova_qntd = int(estoque[entrada[1 - caixa]][0]) - qntd

        if nova_qntd >= 0:
            estoque[entrada[1 - caixa]][0] -= qntd

            if caixa == 0:
                print('SUCCESS')
                        
        elif caixa == 0:
            print('ERROR')


def modo_estoque(iterador, estoque):
    ''' Executa operações no modo estoque'''

    i = 0
    while i < iterador:

        entrada = input().split(" ")
        operacao = entrada[0]
            
        if operacao == "0":
            add_estoque(estoque, entrada)

        if operacao == "1":
            remov_itens(estoque, entrada)

        i += 1


def modo_caixa(iterador, estoque, saldo):
    ''' Executa operações no modo caixa'''

    i = 0
    while i < iterador:

        entrada = input().split()
        remov_itens(estoque, entrada, caixa=1)
        
        # Calculando o saldo da venda
        qntd = int(entrada[1])
        preco = float(estoque[entrada[0]][2])
        saldo += qntd * preco

        i += 1

    return saldo


def relat_estoque(estoque):
    ''' Separa os produtos por categoria em ordem alfabética'''

    categoria = 0
    
    # Ordenando itens por categoria, ou seja, trocando a chave pelo item categoria
    ordenado = dict((sorted(estoque.items(), key = lambda item: item[1][1])))

    for chave in ordenado:

        if estoque[chave][1] == categoria and int(estoque[chave][0]) > 0:
            print(chave, estoque[chave][0])

        elif int(estoque[chave][0]) > 0:
            categoria = estoque[chave][1]
            print("-", categoria)
            print(chave, estoque[chave][0])


def relat_repos(estoque):
    ''' Verifica quais produtos precisam de reposição'''
    ha_itens = False
    repos = []

    for chave in sorted(estoque.keys()):

        qntd = int(estoque[chave][0])
        if qntd == 0:
            repos.append(chave)
            ha_itens = True

    if ha_itens:
        print('* REPOSICAO')
        print("\n".join(repos))


def relat_promo(estoque, data):
    ''' Verifica se algum vencimento está dentro de 7 dias para entrar em promoção'''
    data_format = datetime.strptime(data, '%d%m%Y')
    data = date(data_format.year, data_format.month, data_format.day)
    ha_itens = False
    promo = []

    for chave in estoque.keys():

        vencimento_format = datetime.strptime(str(estoque[chave][3]), '%d%m%Y')
        vencimento = date(vencimento_format.year, vencimento_format.month, vencimento_format.day)

        if abs(data - vencimento).days <= 7 and int(estoque[chave][0]) > 0:
            promo.append(chave)
            ha_itens = True

    if ha_itens:
        print('* PROMOCAO')
        print("\n".join(promo))


estoque = {}
def rodando():
    ''' Função que executa até o fim das operações'''
    saldo = 0

    while True:

        modo = int(input())

        if modo == 0: # Terminar
            return saldo

        iterador = int(input())

        if modo == 1: # Estoque
            modo_estoque(iterador, estoque)

        if modo == 2: # Caixa
            saldo = modo_caixa(iterador, estoque, saldo)


saldo = rodando()
data = input()

print('* ESTOQUE')
relat_estoque(estoque)

print('* SALDO', '{0:.2f}'.format(saldo))

relat_repos(estoque)

relat_promo(estoque, data)