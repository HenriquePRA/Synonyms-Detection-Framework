import csv


def CreatDicionario():

    """
    Essa função é responsável pela parte de carga ela abre o arquivo csv com os curriculos em sua forma bruta e para
    cada linha do arquivo csv é criado um dicionário de acordo com o padrão a seguir.

        item = {
        'id': '',
        'Nome': '',
        'Graduação': {
            '1': '',
            '2': ''
        },
        'Especialização': {
            '1': '',
            '2': ''
        },
        'Mestrado': {
            '1': '',
            '2': ''
        },
        'Doutorado': {
            '1': '',
            '2': ''
        },
        'Posgraduação': {
            '1': '',
            '2': ''
        }

    a única diferença é que no programa o nome das graduações estão reduzidas.

    Uma vez criado o dicionário com o curriculo esse dicionário é adicionado ao último elemento de uma lista que após
    feita a leitura de todos os arquivos é retornada.
    """
    # ABRE O ARQUIVO NO FORMATO DE LEITURA 'r'
    with open('modules/curriculos-lattes.csv', 'r', encoding="utf8") as arquivo:
        linhas = csv.reader(arquivo)

        # PULA A PRIMEIRA LINHA, QUE É O CABEÇALHO
        next(linhas)

        # CRIA UM VETOR QUE IRA CONTER CADA CURRICULO
        curriculos = []

        # LER CADA LINHA E CADA LINHA É UM VETOR
        for linha in linhas:
            # CADA LINHA É UM ITEM NO VETOR E CADA ITEM SERA UM DICIONARIO

            # AS COLUNAS DO CSV SÃO OS IDs, '1' QUARDA SE TEM OU NÃO FORMAÇÃO E '2' POSS UI A FORMAÇÃO
            item = {
                'id': '',
                'nome': '',
                'grad': {
                    '1': '',
                    '2': ''
                },
                'espe': {
                    '1': '',
                    '2': ''
                },
                'mest': {
                    '1': '',
                    '2': ''
                },
                'dout': {
                    '1': '',
                    '2': ''
                },
                'pos': {
                    '1': '',
                    '2': ''
                }
            }

            # ADD O VALOR NOS IDs. 
            # enumerate() SERVE PARA CAPITURAR O INDEX E O VALOR DOS INTERVALOS EM LINHA.
            for index, valor in enumerate(linha):

                # A LEITURA DESSES INTERVALOS SERÁ PULADO POIS NA LEITURA DOS INTERVALOS ANTERIOS, 
                # A ADIÇÃO DE SEU VALOR JÁ FOI REALIZADO.
                if index == 2 or index == 4 or index == 6 or index == 8 or index == 10 or index == 12:
                    continue

                if index == 0:
                    item['id'] = valor
                elif index == 1:
                    item['nome'] = valor

                # ADD DAS FORMAÇÕES    
                elif index == 3:

                    # PEGA O VALOR 'SIM' OU 'NÃO' DE SUA FORMAÇÃO
                    item['grad']['1'] = valor

                    # POSSUI PESSOAS COM MAIS DE UMA GRADUAÇAO E ETC.
                    # É NECESSARIO REMOVER O LIXO(caractesres desnecessarios) > []" < DOS VALORES 
                    # QUE SÃO STRINGS, MAS ESTÃO COM UMA ISTRUTURA DE VETOR
                    # OS VALORES QUE POSSUEM O LIXO > []" < VAI ENTRAR NA FUNÇÃO DE LIMPEZA
                    # E TRANFORMADO REALMENTE EM UM VETOR

                    # FUNCAO DE LIMPEZA
                    if '[' in linha[index + 1]:
                        Limpa_dado('grad', index, item, linha)

                    elif '----' in linha[index + 1]:
                        item['grad']['2'] = None

                    # #QUEM NAO POSSUIR LIXO OU SEJA, QUEM SO TEM UM TIPO DE GRADUAÇÃO VAI SER ADD DIRETAMENTE
                    else:
                        item['grad']['2'] = linha[4]

                elif index == 5:
                    item['espe']['1'] = valor

                    if '[' in linha[index + 1]:
                        # FUNCAO DE LIMPESA
                        Limpa_dado('espe', index, item, linha)

                    elif '----' in linha[index + 1]:
                        item['espe']['2'] = None
                    else:
                        item['espe']['2'] = linha[6]

                elif index == 7:
                    item['mest']['1'] = valor

                    if '[' in linha[index + 1]:
                        # FUNCAO DE LIMPEZA
                        Limpa_dado('mest', index, item, linha)

                    elif '----' in linha[index + 1]:
                        item['mest']['2'] = None

                    else:
                        item['mest']['2'] = linha[8]

                elif index == 9:
                    item['dout']['1'] = valor

                    if '[' in linha[index + 1]:
                        # FUNCAO DE LIMPEZA
                        Limpa_dado('dout', index, item, linha)

                    elif '----' in linha[index + 1]:
                        item['dout']['2'] = None

                    else:
                        item['dout']['2'] = linha[10]

                else:
                    item['pos']['1'] = valor
                    if '[' in linha[index + 1]:
                        # FUNCAO DE LIMPEZA
                        Limpa_dado('pos', index, item, linha)

                    elif '----' in linha[index + 1]:
                        item['pos']['2'] = None

                    else:
                        item['pos']['2'] = linha[12]

            curriculos.append(item)
        arquivo.close()
        return curriculos


def Limpa_dado(espe, index, item, linha):
    # POSSUI PESSOAS COM MAIS DE UMA GRADUAÇAO E ETC.
    # É NECESSARIO REMOVER O LIXO(caractesres desnecessarios) > []" < DOS VALORES 
    # QUE SÃO STRINGS, MAS ESTÃO COM UMA ESTRUTURA DE VETOR
    # OS VALORES QUE POSSUEM O LIXO > []" < VAI ENTRAR NESSE IF E SERA LIMPADO
    # E TRANFORMADO REALMENTE EM UM VETOR

    if '[' in linha[index + 1]:
        lixo = '[]"'
        for i in lixo:
            linha[4] = linha[4].replace(i, '')
        item[espe]['2'] = (linha[4]).split(',')
