from recipes_decimal import pi
from decimal import getcontext, Decimal
getcontext().prec = 36

class Planetas():
    '''' Contém as informações de nome e distância do  planeta'''

    def __init__(self, nome, distancia):
        self.nome = nome
        self.distancia = distancia


def ler_planetas(qnt):
    ''' Lê todos os planetas e os adiciona a um dicionario de classes'''

    planetas = {}

    for _ in range(qnt):

        planeta_atual = input()
        distancia = Decimal(input())

        planetas[planeta_atual] = Planetas(planeta_atual, distancia)

    return planetas


def descarta_planetas(planetas, limite):
    ''' Adiciona o valor -1 a planetas com distância acima do máximo possível para que sejam descartados'''
    
    for chave in planetas:
        if planetas[chave].distancia > limite:
            planetas[chave].distancia = -1


def maior_distancia(planetas):
    ''' Retorna o nome e a distância do planeta mais distância no dicionário'''

    maior = Decimal(-1)
    nome = ''
    for  chave in planetas:
    
        if planetas[chave].distancia > maior:
            nome, maior = planetas[chave].nome, planetas[chave].distancia

    return nome, maior


def func_zeta(s):
    ''' Calcula o somatório zeta'''

    somatorio = 0
    for i in range(1, 101):
        somatorio += Decimal(1) / Decimal(i) ** s 

    return somatorio


def func_materia(a, b, c, d, x):
    ''' Calcula o valor da distância para um dado combustível'''

    raiz = (c * x).sqrt()

    numerador = pi_calc + a * x.exp() - func_zeta(b * x + pi_calc)
    denominador = (1 / raiz.exp()) + d * (Decimal(2) * (pi_calc ** Decimal(3)) - x)

    return numerador / denominador


def busca_binaria(a, b, c, d, y):
    ''' Realiza uma busca para encontrar um valor próximo a y com precisão de 36 casas decimais'''

    esquerda = Decimal(0.)
    direita = Decimal(50.)

    while esquerda <= direita:

        meio = (esquerda + direita) / Decimal(2)

        antimateria = func_materia(a, b, c, d, meio)

        if abs(antimateria - y) <= Decimal(10 ** -32):
            return meio

        elif antimateria > y:
            direita = meio - Decimal(10 ** -32)

        else:
            esquerda = meio + Decimal(10 ** -32)

    return meio


def main():
    ''' Função de execução principal do programa'''

    qnt_planetas = int(input())

    while qnt_planetas != 0:
        
        planetas = ler_planetas(qnt_planetas)

        a = Decimal(input())
        b = Decimal(input())
        c = Decimal(input())
        d = Decimal(input())

        # Verificando se tem algum planeta acima do limite de 50 hawkings e o descartando
        limite = func_materia(a, b, c, d, Decimal(50.))
        descarta_planetas(planetas, limite)

        viagem, y = maior_distancia(planetas)

        # Imprimindo o planeta e a quantidade de combustível
        if y == -1:
            print('GRAU~~')
        
        else:
            combustivel = busca_binaria(a, b, c, d, y)
            print(viagem)
            print(f'{combustivel:.28f}')

        qnt_planetas = int(input())


if __name__ == '__main__':
    pi_calc = pi()
    main()