def DLDistance(string1, string2):

    """
    Método adotado: damerau levenshtein distance

    Recebe duas strings e retorna a distância mínima de edição para que a string1
    se transforme na string2, recebe duas strings.

    possúi um retorno rápido caso alguma ou as duas strings venham vazias
    """

    try:
        # garante que a primeira e a segunda string são de fato strings
        assert (type(string1) == str) and (type(string2) == str)

        # transforma as strings em maiusculo
        string1, string2 = string1.upper(), string2.upper()

        # garante um processamento mais rápido caso alguma ou as duas strings venham vazias
        if (len(string1) == 0) and (len(string2) == 0):
            return 0

        elif len(string1) == 0:
            return len(string2)

        elif len(string2) == 0:
            return len(string1)

        else:

            # aqui é feito de fato o cálculo da distância de Levenshtein.
            # um dicionário simulará uma matriz de forma que seus indices são posições dos indices da matriz.

            lado_x = len(string1) + 1  # x da matriz
            lado_y = len(string2) + 1  # y da matriz
            MatrizLogica = {}  # Dicionário que receberá os dados da matriz

            # aqui são criados os dados que serão guardados pela matriz

            for x in range(lado_x):
                MatrizLogica[x, 0] = x

            for y in range(lado_y):
                MatrizLogica[0, y] = y

            # primeiro for varre a matriz pelo lado x

            for x in range(1, lado_x):

                # segundo for varre a matriz pelo lado y

                for y in range(1, lado_y):

                    # aqui é feita a inserção de distancias
                    # entre as duas strings

                    if string1[x - 1] == string2[y - 1]:
                        MatrizLogica[x, y] = min(
                            MatrizLogica[x - 1, y] + 1,
                            MatrizLogica[x - 1, y - 1],
                            MatrizLogica[x, y - 1] + 1)

                    else:
                        MatrizLogica[x, y] = min(
                            MatrizLogica[x - 1, y] + 1,
                            MatrizLogica[x - 1, y - 1] + 1,
                            MatrizLogica[x, y - 1] + 1)

            # aqui é feita a intersecção entre os dados minimos da matriz
            distancia = MatrizLogica[lado_x - 1, lado_y - 1]

            return distancia

    except AssertionError:
        return "Ambos os dados devem ser strings."
    except IndexError:
        return "Foi informada uma string vazia."
