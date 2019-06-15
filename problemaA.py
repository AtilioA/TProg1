from roboAux import *
from math import *
from functools import reduce

# ============ QUESTÃO A ============ #
# a) Calcular a distância percorrida por um determinado robô ao longo do processo de resgate das vítimas.
# Considere que a distância total percorrida deve ser calculada como a soma de todas as distâncias entre os
# pontos de passagem do robô;

# COMPREENSÃO DO PROBLEMA: deve-se extrair a tupla de um robô da lista de entrada de acordo com o id dado.
# Em seguida, calcular a distância total que ele percorreu (partindo da origem) e retornar esse valor.

# PLANEJAMENTO:
# Criar as seguintes funções:
# - Função para cálculo de distância no plano cartesiano - OK
# - Função para extrair tuplas de uma lista dado um elemento identificador das tuplas - OK

def distEuclid(p1, p2):
    ''' Função: distEuclid()
    Descrição: Calcula a distância entre dois pontos cartesianos
    Escopo: função global paramétrica
    Dados de entrada: Dois pontos reais p1 e p2 de duas coordenadas
    Dados de saída: A distância entre os dois pontos
    '''

    return round(sqrt((tupla1(p1) - tupla1(p2))**2 + (tupla2(p1) - tupla2(p2))**2), 4)

def listaTuplaRoboID(listaRobos, id):
    ''' Função: listaTuplaRoboID()
    Descrição: Extrai todas as tuplas de um mesmo robô da lista de robôs de entrada
    Escopo: função global paramétrica
    Dados de entrada: Lista de robôs de entrada e id de um robô
    Dados de saída: Tuplas de informações um único robô da lista de robôs
    '''

    return list(filter(lambda robo: (pegaID(robo) == id), listaRobos))
    # return [x for x in listaRobos if tupla1(x) == id]


def pegaPontosRobo(listaRobos, id):
    ''' Função: pegaPontosRobo()
    Descrição: Extrai todos os pontos percorridos por um mesmo robô da lista de robôs de entrada
    Escopo: função global paramétrica
    Dados de entrada: Lista de robôs de entrada e id de um robô
    Dados de saída: Lista de todos os pontos percorridos por um único robô da lista de robôs;
    inclui origem como ponto de partida.
    '''

    tuplasRobo = listaTuplaRoboID(listaRobos, id)

    return [(0,0)] + list(map(pegaLocal, tuplasRobo)) # Os robôs partem da origem


def pegaPontosTuplaRobo(tuplasRobo):
    ''' Função: pegaPontosTuplaRobo()
    Descrição: Cria todos os pontos percorridos por um robô de uma lista de tuplas de informações um mesmo robô
    Escopo: função global paramétrica
    Dados de entrada: Lista de tuplas de um robô
    Dados de saída: Lista de todos os pontos percorridos pelo robô;
    inclui origem como ponto de partida.
    '''

    return [(0,0)] + list(map(pegaLocal, tuplasRobo)) # Os robôs partem da origem


def distanciaTotal(pontos):
    ''' Função: distanciaTotal()
    Descrição: Calcula a distância total entre uma lista de pontos
    somando a distância entre um ponto e o próximo até o fim da lista
    Escopo: função global paramétrica
    Dados de entrada: Lista de pontos
    Dados de saída: Distância total somando a distância entre um ponto e o próximo até o fim da lista
    Se não houver robô com o id fornecido ou o robô tiver percorrido menos de 2 pontos, retorna None
    '''
    try:
        if len(pontos) < 2:
            print("Robô não existe ou não enviou dados para a CP.")
            raise Exception()
        elif len(pontos) == 2:
            return distEuclid(pontos[0], pontos[1])
        else:
            return distEuclid(pontos[0], pontos[1]) + distanciaTotal(pontos[1:])
    except:
        pass


def distanciaTotalRobo(listaRobos, id):
    ''' Função: distanciaTotalRobo()
    Descrição: Calcula a distância percorrida por um robô da lista de robôs dado seu id
    Escopo: Função global paramétrica
    Dados de entrada: Lista de dados de robôs e id de um robô
    Dados de saída: Lista de todos os pontos percorridos pelo robô
    '''
    tuplasRobo = listaTuplaRoboID(listaRobos, id)
    pontosPercorridosRobo = pegaPontosTuplaRobo(tuplasRobo)
    return distanciaTotal(pontosPercorridosRobo)
