# Synonyms Detection Framework :books:


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Conteúdo</summary>
  <ul>
    <li>
      <a href="#Sobre">Sobre</a>
      <ul>
        <li><a href="#carga">Processo de Carga</a></li>
        <li><a href="#estatisticas">Geração de dados Estatísticos</a></li>
        <li><a href="#framework">Framework de Busca</a></li>
      </ul>
    </li>
    <li>
      <a href="#Requisitos">Requisitos</a>
    </li>
    <li><a href="#Status">Status</a></li>
    <li><a href="#instalação">Instalação e Testes</a></li>
  </ul>
</details>

<a name="Sobre"></a>
## Sobre :information_source:

Feito em 2019 como projeto da disciplina de Estrutura de Dados, esse projeto tem por objetivo de criar um framework capaz de carregar
dados de um arquivo csv gerar dados estatísticos sobre a base de dados e realizar buscas nessa base de dados de forma a detectar sinônimos
do que for pesquisado.

<a name="carga"></a>
### Carga da Base de dados 

A parte de carga é feita pela função CreatDicionario() essa função utiliza a biblioteca csv do python, ela abre o arquivo csv com 
aproximadamente 1600 currículos em sua forma bruta e para cada linha do arquivo csv é criado um dicionário de dados de acordo.

<a name="estatisticas"></a>
 ### Dados Estatísticos sobre a Base de Dados

A geração de dados estatísticos depende apenas da função estatisitcas() que recebe como argumento a lista de currículos atualmente carregada, 
que caso não esteja carregada retornará uma mensagem de erro. caso essa lista exista a função retorna ao usuário o número de currículos, número
de palavas, porcentagem de Graduações, Especializações, Mestrados, Doutorados e Pós Doutorados.

![]()

<a name="framework"></a>
### Framework de Busca

São exibidas as qualificações disponíveis a pesquisa sendo elas: 

- Graduação
- Especialização
- Mestrado
- Doutorado
- PosDoutorado

Após o usuário informar a qualificação desejada desejada outro input requisita ao usuário a área do conhecimento que o mesmo deseja filtrar 
dos outros currículos.

com a qualificação e a área do conhecimento uma função percorre a base de dados na qualificação informada utilizando uma implementação da 
distância de edição damerau levenshtein é comparado o que o usuário digitou com as qualificações disponíveis em cada currículo, a comparação
é feita ignorando caracteres com acentos e com todas as letras de ambas as strings em caixa alta, e por fim caso o resultado da comparação 
apresentar uma similaridade aceitável entre ambas as strings o currículo do docente é inserido ao final de uma lista que é retornada ao usuário.

![]()

<a name="Requisitos"></a>
## Requisitos do Projeto
 - Python 3.6 ou Superior

<a name="Status"></a>
## Status do Projeto :construction_worker:
  Finalizado :tada:
  
<a name="instalação"></a>
## Testes :computer:

Para testar o projeto em um terminal utilize o python para executar o arquivo main.py, no meu caso utilizei o terminal do windows em um
ambiente virtual criado pela <a href="https://www.anaconda.com/">anaconda</a>.
