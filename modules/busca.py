from modules.distance import DLDistance
import unicodedata


def calcDistancia(string):

    """
    Retorna um inteiro com distancia mínima que deve ser usada caso se queira ter uma distância de edição de um
    terço da string.

    Funcionamento:  string        = "alguma"
                    len("alguma") = 6
                    6 / 100       = 0.06
                    0.06 * 33.33  = 1.9998
                    round(1.9998) = 2
                    a distancia de edição mínima da string "alguma" é dois.
    """

    try:
        assert type(string) == str
        if len(string) <= 1:
            return 0
        return round((len(string) / 100) * 33.33, )

    except AssertionError:
        return 0


def getQuali(string):

    """
    Recebe uma string com uma possível qualificacão, se a distância de edição for menor ou igual a distância de edição
    mínima (calcDistancia) de uma das strings cadastradas como tipos retorna esse tipo em sua versão reduzida para
    dicionário.

    Funcionamento:  string                     = "graduaceo"
                    tipos[0]                   = "Graduação"
                    calcDistancia("Graduação") = 3
                    verifica a distancia entre as duas strings DLDistance("graduaceo", "Graduação") = 3

                    a distancia de edição de "graduaceo" para "Graduação" é menor ou igual a distancia de edição mínima
                    de "Graduação", assim graduaceo é salvo como uma possíbilidade de Graduação com distancia igual a 3.

                    esse processo é feito com todos os outros tipos a fim de encontrar o tipo que possuír a menor
                    distância de edição aceitável com a string de entrada.

                    de todos os tipos Graduação possui a menor distância de edição aceitavel quando comparado com os
                    outros tipo.

                    por fim retorna "Graduação" em seu formato reduzido para dicionário.
    """

    try:
        assert type(string) == str
        tipos = ['Graduação', 'Especialização', 'Mestrado', 'Doutorado', 'PosDoutorado']
        tiposDicio = ['grad', 'espe', 'mest', 'dout', 'pos']

        menorDistancia = {"dist": '', "tipo": ''}

        for i in range(len(tipos)):
            temp = DLDistance(string, tipos[i])
            if menorDistancia["dist"] == '':
                menorDistancia["dist"] = temp
                menorDistancia["tipo"] = tiposDicio[i]

            elif menorDistancia["dist"] > temp:
                menorDistancia["dist"] = temp
                menorDistancia["tipo"] = tiposDicio[i]

            if menorDistancia["dist"] <= calcDistancia(tipos[i]):
                return menorDistancia["tipo"]

        return None

    except AssertionError:
        return None


def padronizacao(string):

    """
    Recebe uma string com acentos e os remove retornando-a com todos os seus caractéres maiusculos

    Funcionamento: string  = "Nãéçid"
                   retorno = "NAECID"
    """

    return unicodedata.normalize('NFKD', string).encode('ASCII', 'ignore').decode("utf-8").upper()


def BuscaStr(string1, string2):

    """
    Recebe duas strings que podem ou não conter várias palavras retorna true caso toda a string1 tenha uma distancia
    de edição menor ou igual que a distancia de edição mínima da string2 ou de uma das palavras da string2 caso a mesma
    possúa mais de uma palavra

    Funcionamento:  string1 = "computador"
                    string2 = "Ciência da Computação"
                    string1 padronizada = "COMPUTADOR"
                    string2 padronizada = "CIENCIA DA COMPUTACAO"

                    string2 possúi mais de uma palavra então a string1 é comparada com cada palavra da string2.

                    string1 possúi uma distancia de edição menor que a distancia de edição minima da palavra
                    "COMPUTACAO" contida na string2 então retorna true.
    """

    # caso a string do dicionário tenha mais de uma palavra
    # a comparação é feita com cada palavra da string.

    copia1 = padronizacao(string1)
    copia2 = padronizacao(string2)

    palavras = copia2.split(" ")

    for i in range(len(palavras)):

        tempvar = palavras[i]
        distancia = DLDistance(copia1, tempvar)

        # caso a distancia da string pesquisada seja menor ou igual que
        # a distancia minima da palavra retorna true

        if distancia <= calcDistancia(tempvar):
            return True

    # caso a comparação não case com nenhuma das palavras da string
    # do dicionario a comparação é feita com a string inteira
    else:
        distancia = DLDistance(copia1, copia2)
        if distancia <= calcDistancia(copia2):
            return True

    return False


def getArea(qualificacao, area, lista):

    """
    Recebe uma string contendo qualificação, uma string contendo a área do conhecimento e a lista de curriculos e
    retorna uma lista contendo dicionários com cada dicionário contendo o nome e a qualificação do curriculo que se
    encaixa na área e qualificação recebidas pela função.

    Funcionamento: area = computador
                   qualificação = grad
                   lista = todos os curriculos contendo várias qualificaçãoes e áreas diferentes.

                   é feita uma verificação em cada linha da lista buscando no campo "grad" da lista quais elementos
                   possuem se assemelham com a palavra computador essa verifição é feita por meio da função BuscaStr().

                   cada linha que atender aos requisitos é adicionada a uma lista de encontrados que por fim é retornada
                   contendo todos os curriculos encontrados que se encaixam nos requisitos.
    """

    encontrados = []

    for curriculo in lista:

        # se o tipo da qualificação for uma string = apenas uma qualificacao
        if type(curriculo[qualificacao]["2"]) == str:
            if BuscaStr(area, curriculo[qualificacao]["2"]):
                encontrados.append({"nome": curriculo["nome"], 'qual': curriculo[qualificacao]["2"]})

        # se o tipo da qualificação for uma lista = mais de uma qualificação
        elif type(curriculo[qualificacao]["2"]) == list:
            for i in range(len(curriculo[qualificacao]["2"])):
                if BuscaStr(area, curriculo[qualificacao]["2"][i]):
                    encontrados.append({"nome": curriculo["nome"], 'qual': curriculo[qualificacao]["2"][i]})

    if not encontrados:
        retstr = "\nNenhum curriculo da área " + str(area) + " encontrado."
        return retstr

    return encontrados
