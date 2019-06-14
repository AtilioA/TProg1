from roboAux import *
from math import *
from functools import reduce

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


def listaVitimasRobo(listaRobos, id):
    ''' Função listaVitimasRobo
    Descrição: Retorna a lista de vítimas avistadas por um robô dado seu id
    Escopo: Função global paramétrica
    Dados de entrada: lista com informações sobre todos os robôs e o id de um robô da lista
    Dados de saída: lista com vítimas avistadas por um robô
    '''

    ids = idsRobos(listaRobos)
    return [tupla4(x) for x in listaRobos if tupla1(x) == id]

def totalVítimasRobô(listaRobos, id):
    ''' Função totalVítimasRobô
    Descrição: Retorna o total de vítimas avistadas por um robô dado seu id
    Escopo: Função global paramétrica
    Dados de entrada: lista com informações sobre todos os robôs e o id de um robô da lista
    Dados de saída: total de vítimas avistadas por um robô
    '''

    listaVitimas = listaVitimasRobo(listaRobos, id)
    return reduce(lambda x, y: x + y, listaVitimas)


def idMaisVitimas(listaRobos):
    ''' Função idMaisVitimas
    Descrição: Retorna os ids do robôs que avistaram o maior número de vítimas
    Escopo: Função global paramétrica
    Dados de entrada: lista com informações sobre todos os robôs
    Dados de saída: lista com ids de robôs (pode haver mais de um) que avistaram o maior número de vítimas
    '''

def totalVitimasRobos(listaRobos):
    ''' Função: nomeDaFunção()
    Descrição: o que a função faz
    Escopo: escopo da função (global/local, paramétrica/constante)
    Dados de entrada: x, y válidos, etc
    Dados de saída: z, w, l lista numérica, b valor booleano, etc
    '''
    print("n sei")
    ids = idsRobos(listaRobos)


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
