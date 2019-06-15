from roboAux import *
from functools import reduce

# ============ QUESTÃO D ============ #
# d) Forneça a identidade do(s) robô(s) que conseguiu(ram) informar o maior número de vítimas (considerando que não há duplicação de identificação de vítima por um mesmo robô).

# COMPREENSÃO DO PROBLEMA: deve-se calcular o número de vítimas que cada robô avistou e identificar o robô que avistou o maior número. Retornar mais de um robô caso o maior número seja repetido.

# PLANEJAMENTO:
# Criar as seguintes funções:
# - Função para extrair número de vítimas vistas em cada ponto passado por um robô - OK
# - Função para somar elementos de uma lista - OK
# - Aplicar essas duas últimas funções para todos os robôs da lista de entrada - OK
# - Extrair maior número da lista obtida no último item - OK
# - Buscar na lista original os robôs que obtiveram o número obtido no último item e retornar os IDs - OK

def robosMaisVitimas(ids, indicesVitimas):
    ''' Função: nomeDaFunção()
    Descrição: o que a função faz
    Escopo: escopo da função (global/local, paramétrica/constante)
    Dados de entrada: x, y válidos, etc
    Dados de saída: z, w, l lista numérica, b valor booleano, etc
    '''
    if len(indicesVitimas) == 1:
        return [ids[indicesVitimas[0]]]
    else:
        return [ids[indicesVitimas[0]]] + robosMaisVitimas(ids, indicesVitimas[1:])


def idsMaisVitimas(listaRobos):
    ''' Função idsMaisVitimas()
    Descrição: Retorna os ids do robôs que avistaram o maior número de vítimas
    Escopo: Função global paramétrica
    Dados de entrada: lista com informações sobre todos os robôs
    Dados de saída: lista com ids de robôs (pode haver mais de um) que avistaram o maior número de vítimas
    '''

    ids = idsRobos(listaRobos)
    indices = indicesMaisVitimas(listaRobos)

    idsVitimas = robosMaisVitimas(ids, indices)

    return idsVitimas


def somaLista(lista):
    ''' Função: somaLista()
    Descrição: Soma os elementos de uma lista numérica
    Escopo: Função global paramétrica
    Dados de entrada: Lista numérica
    Dados de saída: Valor numérico
    '''
    if len(lista) == 0:
        return 0
    else:
        return reduce(lambda x, y: x + y, lista)


def listaVitimasRobo(listaRobos, id):
    ''' Função listaVitimasRobo
    Descrição: Retorna a lista de vítimas avistadas por um robô dado seu id
    Escopo: Função global paramétrica
    Dados de entrada: lista com informações sobre todos os robôs e o id de um robô da lista
    Dados de saída: lista com vítimas avistadas por um robô
    '''

    return [pegaVitimas(x) for x in listaRobos if tupla1(x) == id]


def totalVitimasRobo(listaRobos, id):
    ''' Função totalVitimasRobo
    Descrição: Retorna o total de vítimas avistadas por um robô dado seu id
    Escopo: Função global paramétrica
    Dados de entrada: lista com informações sobre todos os robôs e o id de um robô da lista
    Dados de saída: total de vítimas avistadas por um robô
    '''

    listaVitimas = listaVitimasRobo(listaRobos, id)
    return somaLista(listaVitimas)


def indicesMaisVitimas(listaRobos):
    ''' Função: nomeDaFunção()
    Descrição: o que a função faz
    Escopo: escopo da função (global/local, paramétrica/constante)
    Dados de entrada: x, y válidos, etc
    Dados de saída: z, w, l lista numérica, b valor booleano, etc
    '''
    listaVitimasRobos = totalVitimasRobos(listaRobos)
    indices = indicesMaximos(listaVitimasRobos)

    return indices


def totalVitimasRobos(listaRobos):
    ''' Função: nomeDaFunção()
    Descrição: o que a função faz
    Escopo: escopo da função (global/local, paramétrica/constante)
    Dados de entrada: x, y válidos, etc
    Dados de saída: z, w, l lista numérica, b valor booleano, etc
    '''
    ids = idsRobos(listaRobos)

    return list(map(lambda id: totalVitimasRobo(listaRobos, id), ids))


def tuplasRoboId(listaRobos, id):
    ''' Função tuplasRoboID
    Descrição: Retorna as tuplas de um robô na lista dado seu id
    Escopo: Função global paramétrica
    Dados de entrada: lista com informações sobre todos os robôs
    Dados de saída: lista de tuplas de um robô
    '''

    if listaRobos == []:
        return []
    elif tupla1(listaRobos[0]) == id:
        return [listaRobos[0]] + tuplasRoboId(listaRobos[1:], id)
    else:
        return tuplasRoboId(listaRobos[1:], id)

from problemaA import *
from problemaB import *
from problemaC import *
