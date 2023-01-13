
class Noticia:
    ''' Classe que armazena todas as informações de cada notícia'''

    def __init__(self, id, titulo, qtdLeitores, qtdLeitoresFinal, qtdCliques, tempo, conteudo):

        self.id = id
        self.titulo = titulo
        self.qtdLeitores = qtdLeitores
        self.qtdLeitoresFinal = qtdLeitoresFinal
        self.qtdCliques = qtdCliques
        self.tempo = tempo
        self.conteudo = conteudo

    def id(self):
        return self.id

    def titulo(self):
        return self.titulo
    
    def qtdLeitores(self):
        return self.qtdLeitores
    
    def qtdLeitoresFinal(self):
        return self.qtdLeitoresFinal

    def qtdCliques(self):
        return self.qtdCliques

    def tempo(self):
        return self.tempo


def mais_leitores(dados):

    maior = 0
    titulo = ''
    for x in dados:

        if maior < dados[x].qtdLeitores:
            maior = dados[x].qtdLeitores
            titulo = dados[x].titulo

    return maior, titulo

def mais_leitores_final(dados):

    maior = 0
    titulo = ''
    for x in dados:

        if maior < dados[x].qtdLeitoresFinal:
            maior = dados[x].qtdLeitoresFinal
            titulo = dados[x].titulo

    return maior, titulo

def maior_tempo(dados):

    maior = 0

    for x in dados:

        if maior < dados[x].tempo:
            maior = dados[x].tempo

    return maior

n_arq = int(input())
noticias = []
dados = {}

for i in range(n_arq):

    noticias.append(input())

# Relatórios únicos de cada noticia
for i in range(n_arq):

    in_path = f'{noticias[i]}'

    # Leitura dos arquivos
    with open(in_path, 'r') as noticia:
            
        id = (noticia.readline().split(": "))[1].rstrip('\n')
        titulo = (noticia.readline().split(": "))[1].rstrip('\n')
        qtdLeitores = (noticia.readline().split(": "))[1].rstrip('\n')
        qtdLeitoresFinal = (noticia.readline().split(": "))[1].rstrip('\n')
        qtdCliques = (noticia.readline().split(": "))[1].rstrip('\n')
        tempo = (noticia.readline().split(": "))[1].rstrip('\n')
        conteudo = (noticia.readline().split(": "))[1]

        dados[noticias[i]] = Noticia(id, titulo, int(qtdLeitores), int(qtdLeitoresFinal), int(qtdCliques), int(tempo), conteudo)

    out_path = f'relatorio_{dados[noticias[i]].id}.txt'

    # Escrita dos relatórios
    with open(out_path, 'w') as relatorio:
        valores = dados[noticias[i]]

        relatorio.write('nId: ' + valores.id + "\n")
        relatorio.write('qtdLeitores: ' + str(valores.qtdLeitores) + "\n")
        relatorio.write('qtdLeitoresFinal: ' + str(valores.qtdLeitoresFinal) + "\n")
        relatorio.write('qtdCliques: ' + str(valores.qtdCliques) + "\n")
        relatorio.write('tempo: ' + str(valores.tempo))

# Relatório final

leitores = 0
cliques = 0
paragrafos = 0

relat_path = 'relatorio_final.txt'

with open(relat_path, 'w') as final:

    for x in dados.keys():

        # Obtendo os valores
        leitores += dados[x].qtdLeitores
        cliques += dados[x].qtdCliques
        paragrafos += len(dados[x].conteudo.split("\n"))
        
        melhor_tempo = maior_tempo(dados)

        maior_leitores, melhor_titulo = mais_leitores(dados)
        maior_leitores_final, melhor_titulo_final = mais_leitores_final(dados)
    
    # Escrevendo
    final.write(f'{(leitores//len(dados))}' + "\n")
    final.write(f'"{melhor_titulo}" {maior_leitores}' + "\n")
    final.write(f'"{melhor_titulo_final}" {maior_leitores_final}' + "\n")
    final.write(f'{(cliques//len(dados))}' + "\n")
    final.write(f'{melhor_tempo}' + "\n")
    final.write(f'{(paragrafos//len(dados)) + 1}')
