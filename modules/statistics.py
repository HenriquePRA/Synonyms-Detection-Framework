def estatisticas(lista):

    """
    Recebe uma lista de dicionários contendo curriculos e retorna o número de curriculos, quantas palavras todos os
    curriculos possuem e a porcentagem dos curriculos que possuem graduação, especialização, mestrado, doutorado e pos
    doutorado
    """

    # Número de curriculos
    N_curri = len(lista)

    # Número de palavras
    def numPalavras(listanp):

        """
        Recebe um conjunto de dicionarios onde cada linha contem curriculos formatados e retorna um número inteiro
        contendo o total de palavras
        """

        def contarPalavrasDict(dicionario):

            """
            Recebe uma linha do conjundo de dicionários que contem curriculos formatados e conta e retorna o número
            de palavras em cada campo exceto pelo campo do identificador
            """

            # conta a quantidade de palavras no campo nome
            CountDict = contarPalavrasString(dicionario['nome'])

            # conta a quantidade de palavras no campo de graduação
            CountDict += AuxConta(dicionario['grad'])

            # conta a quantidade de palavras no campo de especialização
            CountDict += AuxConta(dicionario['espe'])

            # conta a quantidade de palavras no campo de mestrado
            CountDict += AuxConta(dicionario['mest'])

            # conta a quantidade de palavras no campo de doutorado
            CountDict += AuxConta(dicionario['dout'])

            # conta a quantidade de palavras no campo de doutorado
            CountDict += AuxConta(dicionario['pos'])

            return CountDict

        def AuxConta(subdicio):

            """
            Auxilia um dicionário a contar palavras, retorna o número de palavras de um subdicionário, subdicionário
            esse que pode conter uma lista. retorna o número de palavras do subdicionario.
            """

            CountSubDict = 0
            for i in range(1, 2):
                if type(subdicio[str(i)]) == str:
                    CountSubDict += contarPalavrasString(subdicio[str(i)])

                elif type(subdicio[str(i)]) == list:
                    for j in range(len(subdicio[str(i)])):
                        CountSubDict += contarPalavrasString(subdicio[str(i)][j])

            return CountSubDict

        def contarPalavrasString(string):

            """ Retorna o número de palavras de uma string """

            CountString = 0
            if string is None:
                return CountString

            if string != '':
                CountString += 1

            for i in range(len(string)):
                if string[i] == ' ':
                    CountString += 1

            return CountString

        CountAll = 0
        for curriculo in listanp:
            CountAll += contarPalavrasDict(curriculo)

        return CountAll

    N_palavras = numPalavras(lista)

    def porcentos(listapr):

        """ Recebe um conjunto de dicionários onde cada um desses dicionários contem um curriculo formatado e retorna
        uma string que representa a porcentagem desses curriculos que possúi graduação. """

        CountGrad = 0
        CountEspec = 0
        CountMest = 0
        CountDout = 0
        CountPosDout = 0

        for curriculo in lista:

            if curriculo['grad']['1'] == 'SIM':
                CountGrad += 1
            if curriculo['espe']['1'] == 'SIM':
                CountEspec += 1
            if curriculo['mest']['1'] == 'SIM':
                CountMest += 1
            if curriculo['dout']['1'] == 'SIM':
                CountDout += 1
            if curriculo['pos']['1'] == 'SIM':
                CountPosDout += 1

        CountGrad = '{:.2f}%'.format(((CountGrad / len(listapr)) * 100))
        CountEspec = '{:.2f}%'.format(((CountEspec / len(listapr)) * 100))
        CountMest = '{:.2f}%'.format(((CountMest / len(listapr)) * 100))
        CountDout = '{:.2f}%'.format(((CountDout / len(listapr)) * 100))
        CountPosDout = '{:.2f}%'.format(((CountPosDout / len(listapr)) * 100))

        return {"N_grad": CountGrad, "N_espec": CountEspec, "N_mest": CountMest, "N_dout": CountDout,
                "N_pos": CountPosDout}

    porcentagens = porcentos(lista)

    return {"N_curri": N_curri, "N_palavras": N_palavras, "N_grad": porcentagens["N_grad"],
            "N_espec": porcentagens["N_espec"], "N_mest": porcentagens["N_mest"], "N_dout": porcentagens["N_dout"],
            "N_pos": porcentagens["N_pos"]}


def exibirEstatisticas(lista):

    """ Recebe uma lista que pode conter várias tuplas que contem curriculos e printa linha a linha de maneira organizada """

    def espaconome(nome):

        """ Auxilia a função tratamento, recebe uma string com um nome e adiciona espaços em branco ao final da string
        até que a string tenha um total de cinquenta e cinco caracteres. """

        padrao = 55
        if len(nome) >= padrao:
            return nome

        retstr = nome
        for i in range(padrao - len(nome)):
            retstr += ' '
        return retstr

    def tratamento(listaatratar):

        """ Auxilia a função exibirEstatísticas gerando uma string organizada para cada linha """

        try:
            assert type(listaatratar) is list
            lista_tratada = []

            for linha_tratar in listaatratar:
                linha_apend = espaconome(linha_tratar["nome"]) + linha_tratar["qual"]
                lista_tratada.append(linha_apend)

            return lista_tratada

        except AssertionError:
            return "A a função de tratamento espera receber uma lista."

    if type(lista) is list:
        lista_Exibir = tratamento(lista)
        print("\nDocente                                                Qualificação\n------------------------------"
              "------------------------ ---------------------------------------------------")

        for linha in lista_Exibir:
            print(linha)
    else:
        print(lista)


