def sobreCarga():

    """
    Exibe na na tela para o usuário o funcionamento do processo de carga.
    """

    print("\nA parte de carga é feita pela função CreatDicionario() essa função utiliza a biblioteca csv do python,\n"
          "ela abre o arquivo csv com os curriculos em sua forma bruta e para cada linha do arquivo csv é criado um \n"
          "dicionário de acordo com o padrão a seguir.\n\n"
          " item = {\n 'id': '',\n 'Nome': '',\n 'Graduação': {\n    '1': '',\n    '2': ''\n },\n "
          "'Especialização': {\n    '1': '',\n    '2': ''\n },\n 'Mestrado': {\n    '1': '',\n    '2': ''\n },\n"
          "'Doutorado': {\n    '1': '',\n    '2': ''\n },\n 'Posgraduação': {\n    '1': '',\n    '2': ''\n }\n\n"
          "A única diferença é que no programa o nome das qualificações estão reduzidas.\n\n"
          "Uma vez criado o dicionário com o curriculo esse dicionário é adicionado ao último elemento de uma lista\n"
          "que após feita a leitura de todos os arquivos é retornada.")


def sobreBusca():

    """
    Exibe na na tela para o usuário o funcionamento do processo de busca.
    """

    # Sobre a checagem
    print("\nPrimeiramente a função de busca checam se a base de dados com os curriculos já foi carregada.\n"
          "Caso não esteja carregada é exibida na tela para o usuário uma mensagem de erro informando que\n"
          "a base de dados não está carregada.\n\nCaso esteja carregada são exibidas as qualificações disponíveis "
          "a pesquisa sendo elas: \n\n - Graduação\n - Especialização\n - Mestrado\n - Doutorado\n"
          " - PosDoutorado\n")

    # Sobre a qualificação
    print("Um input será requisitado ao usuário para que o mesmo digite o nome da qualificação a ser pesquisada.\n"
          "nesse input o usuário poderá cometer erros gramaticais não sendo obrigatório que os caracteres sejam ou\n"
          "não digitados em caixa alta.\n")

    # Resumo da função getQuali()
    print("O imput do usuário é verificado pela função getQuali() que verifica se a qualificação realmente existe\n"
          "caso exista a função retorna o nome da qualificação em seu formato reduzido para que seja usada mais a\n"
          "frente pelo programa. caso não xista é exibido na tela ao usuário uma mensagem de erro.\n")

    # Sobre a área do conhecimento
    print("Após isso outro input requisita ao usuário a área do conhecimento que o mesmo deseja filtrar dos outros\n"
          "curriculos. \n\nPor exemplo: Sistemas para Internet.\n")

    # Sobre a pesquisa
    print("Uma vez com a qualificação e a área do conhecimento a função sobreArea() é usada tendo a lista de \n"
          "curriculos, área e qualificação como argumentos.\n\n"
          "Exemplo: sobreArea('grad','sistemas para internet',lista)\n")

    print("Existem dois possíveis retornos para esssa função são uma lista contendo os docentes de acordo com o que\n"
          "foi filtrado ou uma mensagem informando que nenhum curriculo foi encontrado. Se uma lista foi recebida\n"
          "Ela será exibida na tela para o usuário com o auxilio da função exibirEstatisticas().\n")


def sobreEstatisticas():

    """
    Exibe na na tela para o usuário o funcionamento do processo que retorna dados estatísticos.
    """

    print("\nA geração de dados estatísticos depende apenas da função estatisitcas() que recebe como argumento apenas "
          "a\nlista de curriculos, que caso não esteja carregada retornará uma mensagem de erro. caso essa lista "
          "exista\na função retorna ao usuário:\n\n - O número de curriculos carregados.\n - O número total de "
          "palavras\n - A Porcentagem desses curriculos que possuem graduação\n - A Porcentagem desses curriculos que "
          "possuem especialização\n - A Porcentagem desses curriculos que possuem mestrado\n - A Porcentagem desses"
          "curriculus que possuem doutorado\n - A Porcentagem desses curriculos que possuem Pós-Graduação")


def sobreMetodos():

    """
    Exibe detalhadamente os métodos adotados para o processo de carga e de busca.
    """

    # carga
    print("\nOs métodos adotados para o processo de carga foram:\n\n"
          " - Carregar cada curriculo em um dicionário\n"
          " - Dentro de cada curriculo há um subdicionário para cada qualificação no qual:\n\n"
          "'Qualificação': "
          "{\n    '1':  <-- Recebe uma string sim ou não para indicar a existencia da qualificaçao.\n    '2': "
          " <-- Recebe uma lista com as qualificações do curriculo caso exista mais de uma qualificaçao\n"
          "              caso exista apenas uma recebe apenas uma string com o nome da qualificação, caso não exista\n"
          "              recebe uma string vazia.\n}")

    # busca
    print("\nOs métodos adotados para o processo de busca foram:\n\n"
          " - Detecção da distância de edição por meio da técnica Damerau–Levenshtein distance.\n"
          " - Antes de ser feita a comparação entre duas strings elas são 'padronizadas' por uma função que\n"
          "   remove acentos de caracteres e transforam toda string em caixa alta.\n"
          "\n   Exemplo: Cãoçadí --> CAOCADI\n\n"
          " - Foi definido que a distância de edição mínima de uma string é de 33,33% de seu tamanho arredondado\n"
          "   para cima, pois essa distância após testes com várias outras distancias é a que traz a maior quantidade\n"
          "   de dados sem que venha resultados não desejados, por exemplo a distancia de edição mínima da string\n"
          "   computador engloba a string Computar mas não englobar a string Campus.\n"
          " - Toda a parte de pesquisa é feita manipulado a estrutura de dados list que serve de conteinter para\n"
          "   dicinários que são a base de toda estrutura da aplicação.")


def sobre():

    """
    Exibe as opções disponíveis para que o usuário possa obter informações detalhadas sobre a aplicação.
    """

    sairsobre = False

    while sairsobre is not True:

        print("\nÉ possível obter informações sobre partes do programa são elas:\n\n 1 - Sobre o carregamento dos "
              "arquivos\n 2 - Sobre as Estatísitcas de Base\n 3 - Sobre a busca\n 4 - Sobre métodos adotados"
              "\n 5 - Retornar ao menu principal\n")

        try:
            opcao = input('Informe o Número da opção desejada: ')
            opcao = int(opcao)
            assert 0 < opcao <= 6
            if opcao is 1:
                sobreCarga()
            elif opcao is 2:
                sobreEstatisticas()
            elif opcao is 3:
                sobreBusca()
            elif opcao is 4:
                sobreMetodos()
            elif opcao is 5:
                sairsobre = True

        except ValueError:
            print('\nA opção precisa ser um número.\n')
        except AssertionError:
            print('\nOpção não identificada.\n')