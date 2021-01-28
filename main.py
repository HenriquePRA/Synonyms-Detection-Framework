from modules.load import CreatDicionario
from modules.statistics import estatisticas, exibirEstatisticas
from modules.busca import getQuali
from modules.busca import getArea
from modules.sobre import sobre


def menu_principal():

    """
    A Função menu principal oferece ao usuário um menu interativo ao qual o usuário pode escolher entre as opções do
    menu invocar outras funções que podem carregar dados, gerar dados estatísticos, realizar buscas ou informar como
    e por quem partes da aplicação foi construída e como ela funciona.
    """

    # ---- Variáveis da Função ----#
    curriculos = CreatDicionario()
    sair = False
    # -----------------------------#

    while not sair:

        print("\n|======================================|\n|          Base de Curriculos          |\n|======================================|\n\n (e) "
              "- Estatísticas\n (i) - Busca\n (s) - Sobre\n (q) - Sair\n")
        opcao = input("Opção: ")

        try:

            assert opcao in ["e", "i", "s", "q"]
            if opcao == "e":
                if curriculos is not None:
                    dados = estatisticas(curriculos)
                    print("\nNúmero de Curriculos:             ", dados["N_curri"])
                    print("Número total de Palavras:         ", dados["N_palavras"])
                    print("Porcentagem de Graduações:        ", dados["N_grad"])
                    print("Porcentagem de Especializações:   ", dados["N_espec"])
                    print("Porcentagem de Mestrados:         ", dados["N_mest"])
                    print("Porcentagem de Doutorados:        ", dados["N_dout"])
                    print("Porcentagem de Pós Doutorados:    ", dados["N_pos"])

                else:
                    print("\nNão é possível gerar dados estatísticos\nBase de dados não carregada.")

            elif opcao == "i":
                if curriculos is not None:
                    print("\nQualificações disponíveis:\n\n"
                          " - Graduação\n - Especialização\n - Mestrado\n - Doutorado\n - PosDoutorado\n")
                    qualificacao = input("Qualificação: ")
                    qualificacao = getQuali(qualificacao)
                    if qualificacao is not None:
                        area = input("Área do Conhecimento: ")
                        lista = getArea(qualificacao, area, curriculos)
                        if lista:
                            exibirEstatisticas(lista)
                    else:
                        print('Qualificação não encontrada')
                else:
                    print("\nNão é possível realizar buscas\nBase de dados não carregada.")

            elif opcao == "s":
                sobre()
            elif opcao == "q":
                sair = True

        except AssertionError:
            print("\n|======================|\n| OPÇÃO INDISPONÍVEL ! |\n|======================|")


if __name__ == "__main__":
    menu_principal()
