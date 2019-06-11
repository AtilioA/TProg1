# Auxílio ao resgate de vítimas por robôs em ambientes acidentados
# Autores: Atílio Antônio Dadalto
# Disciplina: Programação I, ministrada por Jordana Sarmenghi Salamon em 2019/1

# ALGUMAS ESPECIFICAÇÕES DO TRABALHO:
# Considere que todos os robôs partem do mesmo ponto inicial: (0,0).
# As informações enviadas pelos robôs de resgate contêm os seguintes registros:
# a identificação do robô,
# o instante em que o robô passou em um determinado ponto da área afetada,
# o ponto no plano cartesiano referente ao incidente registrado, e
# o número de vítimas presentes na área de visibilidade do robô.

# Considerando uma lista com tais informações como os dados de entrada disponíveis, faça um programa em Python que responda às seguintes solicitações:
# Suposta entrada (Jordana ainda não enviou exemplos):
# listaRobôs = [(id1, instante1, ponto1, nVítimas1), (id2, instante2, ponto2, nVítimas2)]
# Compreensão do problema e planejamento da solução

# "(Ao importar funções de algum módulo, utilize a opção de importação específica)"
import random
from roboAux import *
from math import *
from functools import reduce
import sys # Para testes (mergeSort por exemplo) apenas, não irá para a versão final
sys.setrecursionlimit(10000) # Para aumentar limite de recursão do Python


# "Cada função deve ter um comentário com sua descrição, dados de entrada e saída.
# Na descrição, diga se a função é global ou local, paramétrica ou não, e por quê.
# Realizar a validação dos dados."
# Vamos comentar as funções assim:
def template(entradas):
    ''' Função: nomeDaFunção()
    Descrição: o que a função faz
    Escopo: escopo da função (global/local, paramétrica/constante)
    Dados de entrada: x, y válidos, etc
    Dados de saída: z, w, l lista numérica, b valor booleano, etc
    '''

    # Resto da função. A validação ocorre aqui, com try, Exception() e etc


# ============ QUESTÃO A ============ #
# a) Calcular a distância percorrida por um determinado robô ao longo do processo de resgate das vítimas.
# Considere que a distância total percorrida deve ser calculada como a soma de todas as distâncias entre os
# pontos de passagem do robô;

# COMPREENSÃO DO PROBLEMA: deve-se extrair a tupla de um robô da lista de entrada de acordo com o id dado.
# Em seguida, calcular a distância total que ele percorreu e retornar esse valor.

# PLANEJAMENTO:
# Criar as seguintes funções:
# - Função para cálculo de distância no plano cartesiano - OK
# - Função para extrair uma tupla de uma lista dado um elemento identificador da tupla
# - Função para calcular a distância entre os pontos percorridos pelo robô, por ordem de instante
# - Função para ordenar lista por instante (talvez não precise disso, precisamos ver o exemplo de entrada)
# - Função para somar todos os elementos de uma lista - FAZ ISSO ÍCARO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def distRobô(listaRobôs): # Versão sem ID

    return

def distRobôID(listaRobôs, id):
    ''' Função: distRobô
    Descrição: Calcula a distância total que um robô percorreu
    Escopo: função global paramétrica
    Dados de entrada: a lista de informações dos robôs e o ID de um robô na lista
    Dados de saída: a distância percorrida por um robô
    '''

    return


def distEuclid(p1, p2):
    ''' Função: distEuclid()
    Descrição: Calcula a distância entre dois pontos cartesianos
    Escopo: função global paramétrica
    Dados de entrada: dois pontos reais p1 e p2
    Dados de saída: a distância entre os pontos
    '''

    return sqrt((tupla1(p1) - tupla1(p2))**2 + (tupla2(p1) - tupla2(p2))**2)


# ============ QUESTÃO B ============ #
# b) Determine qual dos robôs apresenta o seu último ponto de passagem no terreno de busca que
#  possui a maior distância em relação à origem.
#  Exiba o caminho percorrido pelo robô e o tempo total do percurso;
# - Extrair, da lista de entrada, o último ponto de passagem de todos os robôs
# - Determinar qual robô possui ponto mais longe da origem
# - Imprimir caminho percorrido pelo robô, determinar tempo do percurso

# COMPREENSÃO DO PROBLEMA: deve-se obter o último ponto de passagem de todos os robôs e retornar
# o robô que possui o último ponto mais distante da origem.

# PLANEJAMENTO:
# Criar as seguintes funções:
# - Função para obter uma lista com o último ponto de todos os robôs da lista de entrada
# - Função para calcular a distância da origem a todos esses pontos, retornando em uma lista
# - Função para extrair maior número da lista obtida no último item
# - Função para buscar na lista original os robôs que obtiveram o número obtido no último item e retornar os IDs.
# - Função para determinar tempo de percurso de um robô, dado seu percurso
# - Função para imprimir percurso de um robô

def últimosPontosRobôs(listaRobôs): # Separar em funções menores
    percursos = map(tupla3(listaRobôs)) # Supostamente pega a lista de percursos de todos os robôs
    últimosPontos = list(map(lambda lista: lista[-1], percursos)) # Pega o último ponto de cada robô
    distOrigemRobôs = map(lambda ponto: distEuclid(0, ponto), últimosPontos) # Supostamente calcula distância da origem até o ponto, para cada ponto


# ============ QUESTÃO C ============ #
# c) Exiba os caminhos percorridos por todos os robôs que entraram no terreno de busca,
# ordenados crescentemente pela distância total percorrida;

# COMPREENSÃO DO PROBLEMA: deve-se calcular as distâncias percorridas por todos os robôs, adicionando-as
# em uma lista que será ordenada, imprimida na tela e então retornada

# PLANEJAMENTO:
# Criar as seguintes funções:
# - Função para ordenar lista em ordem crescente - OK
# - Função para aplicar a função da questão (a) em todos os robôs da lista de entrada - OK?
# - Ordenar essa lista de distâncias e retornar (a menos que queira a lista de tuplas original, ver isso depois) - OK?

def exibeCaminhosRobôsCrescente(listaRobôs):
    ''' Função exibeCaminhosRobôsCrescente()
    Descrição: Dada a lista de robôs, imprime o caminho de cada robô (em ordem crescente de distância)
    Escopo: Função global paramétrica
    Dados de entrada: A lista de dados sobre os robôs
    Dados de saída: Uma lista de distâncias ordenada
    '''
    listaDistâncias = map(distRobô(listaRobôs))
    listaDistânciasOrdenadas = mergeSort(listaDistâncias)
    print(listaDistânciasOrdenadas)
    return listaDistânciasOrdenadas


def mergeOrdenada(l1, l2):
    ''' Função mergeOrdenada()
    Descrição: Com duas listas ordenadas de entrada, junta as duas de forma ordenada
    Escopo: Função global paramétrica
    Dados de entrada: Duas listas numéricas ordenadas
    Dados de saída: Uma lista ordenada gerada a partir da junção ordenada das duas de entrada
    Pega o primeiro elemento que seja o menor dentre as duas listas
    e junta com o resultado da função chamando com resto da lista "menor"
    Ex: l1 = [1, 2] e l2 = [3, 4]:
    mergeOrdenada([1, 2], [3, 4])
    [1] + mergeOrdenada([2], [3, 4])
    [2] + mergeOrdenada([], [3, 4])
    len(l1) == 0, retorna l2
    [1] + [2] + [3, 4]
    [1, 2, 3, 4]
    '''
    if len(l1) == 0:
        return l2
    elif len(l2) == 0:
        return l1
    elif l1[0] < l2[0]:
        return [l1[0]] + mergeOrdenada(l1[1:], l2)
    else:
        return [l2[0]] + mergeOrdenada(l1, l2[1:])

def mergeSort(lista):
    ''' Função mergeSort()
    Descrição: Dada uma lista de entrada, ordena-a por mergesort
    Escopo: Função global paramétrica
    Dados de entrada: Uma lista numérica
    Dados de saída: Uma lista numérica ordenada
    '''
    if len(lista) <= 1:
        return lista
    else:
        metade = len(lista) // 2 # Pega o índice do meio da lista
        return mergeOrdenada(mergeSort(lista[:metade]), mergeSort(lista[metade:]))


# ============ QUESTÃO D ============ #
# d) Forneça a identidade do(s) robô(s) que conseguiu(ram) informar o maior número de vítimas (considerando que não há duplicação de identificação de vítima por um mesmo robô).

# COMPREENSÃO DO PROBLEMA: deve-se calcular o número de vítimas que cada robô avistou e identificar o robô que avistou o maior número. Retornar mais de um robô caso o maior número seja repetido.

# PLANEJAMENTO:
# Criar as seguintes funções:
# - Função para extrair número de vítimas vistas em cada ponto passado por um robô
# - Função para somar elementos de uma lista
# - Aplicar essas duas últimas funções para todos os robôs da lista de entrada
# - Extrair maior número da lista obtida no último item
# - Buscar na lista original os robôs que obtiveram o número obtido no último item e retornar os IDs.

def idMaisVítimas(listaRobôs):
    ''' Função idMaisVítimas
    Descrição: Retorna os ids do robôs que avistaram o maior número de vítimas
    Escopo: Função global paramétrica
    Dados de entrada: lista com informações sobre todos os robôs
    Dados de saída: lista com ids de robôs (pode haver mais de um) que avistaram o maior número de vítimas
    '''
    def vítimasRobôs(listaRobôs): # Algo nesse sentido
        return map(tupla4(listaRobôs))

    def totalVítimasRobôs(listaRobôs):
        listaVítimas = vítimasRobôs(listaRobôs)
        return map(somaLista(listaVítimas))

    totalVítimasRobôsLista = totalVítimasRobôs(listaRobôs)
    nMaisVítimas = maiorLista(totalVítimasRobôsLista)

    def elementosLista(lista, n): # testando ainda
        if lista[0] == n and len(lista) < 2:
            return [lista[0]]
        elif lista[0] == n:
            return [lista[0]] + elementosLista(lista[1:], n)


# ============ TESTES ============ #
# "Os testes propriamente ditos devem estar automatizados no arquivo de código"
# Aqui ficarão os testes do programa, inclusive os testes que estarão na versão final
dist01 = distEuclid((0,0),(1,1))
print(f"Distância entre (0,0 e (1,1): {dist01}")

listaTeste = [random.randrange(1, 100) for _ in range(0, 100)]
print(listaTeste)
print(mergeSort(listaTeste))
