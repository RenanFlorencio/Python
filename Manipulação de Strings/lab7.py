
if __name__ == "__main__":

    lista = input().split(", ")
    ult_indice = str(lista.pop())

    # Separando o item que deve ser descartado e o item que faz parte da lista
    ult_list = ult_indice.split("/ ")
    descarte = ult_list[1]
    ult_item = ult_list[0]
    lista.append(ult_item)

    def consecutivas(lista):
        '''Retorna quantas vezes um item aparece mais vezes consecutivamente'''

        contador_geral = 0
        contador_atual = 0
        consecutivo = ""

        item = lista[0]
        for x in range(len(lista)):

            if item == lista[x]:
                contador_atual += 1

            else:
                contador_atual = 0
                item = lista[x]

            if contador_atual > contador_geral:
                consecutivo = lista[x]
                contador_geral = contador_atual

            item = lista[x]
        
        return consecutivo, contador_geral + 1  # O contador sempre retorna 1 a menos


    def descartar(lista, descarte):
        ''' Descarta todos os itens iguais ao descarte passado'''

        i = 0
        while i < len(lista):

            if lista[i] == descarte:
                lista.remove(lista[i])
            else:
                i += 1


    def remover_duplicatas (lista):
        ''' Cria uma nova lista sem duplicatas'''

        nova_lista = []

        for x in range(len(lista)):

            if not lista[x] in nova_lista:
                nova_lista.append(lista[x])
            
        return nova_lista

    
    def unicos(lista):
        ''' Retorna quantos itens únicos existem a partir da lista sem duplicatas'''

        return len(remover_duplicatas(lista))


    def limpar_str(lista):
        ''' Troca todos os caracteres " " por "-" '''

        for x in range(len(lista)):

            # Lista com cada caractere da string
            string = list(lista[x])

            for i in range(len(string)):
                if string[i] == " ":
                    string[i] = "-"

            # Unindo os caracteres novamente
            lista[x] = "".join(string)

        return lista


    def formatar(lista):
        ''' Deixa todos os caracteres em lower case, menos o prefixo'''

        for x in range(len(lista)):

            # Removendo e armazenando o prefixo
            list_string = list(lista[x])
            low_string = "".join(list_string[2:])
            prefixo = "".join(list_string[:2])

            # Capitalizando e concatenando as strings separadas
            string = low_string.lower()
            lista.remove(lista[x])
            lista[x:x] = [prefixo + string]


    def categorizar(lista):
        ''' Separa as fotos nas categorias HOMEM-ARANHA, CRIMINOSO ou CENA DO CRIME'''

        homem_aranha = []
        criminoso = []
        cena_crime = []

        for x in range(len(lista)):
            string = list(lista[x])

            if string[:2] == ['H', 'A']:
                homem_aranha.append(lista[x])

            elif string[:2] == ['C', 'R']:
                criminoso.append(lista[x])

            elif string[:2] == ['C', 'C']:
                cena_crime.append(lista[x])
        
        return homem_aranha, criminoso, cena_crime


    nome, contagem = consecutivas(lista)
    print(nome, contagem)
    print(unicos(lista))
    descartar(lista, descarte)
    lista = remover_duplicatas(lista)
    limpar_str(lista)
    formatar(lista)

    homem_aranha, criminoso, cena_crime = categorizar(lista)

    print(homem_aranha)
    print(criminoso)
    print(cena_crime)
