# Módulo com funções para solucionar o problema A
# Autores: Atílio Antônio Dadalto
# Disciplina: Programação I, ministrada por Jordana Sarmenghi Salamon em 2019/1

from math import sqrt

from roboAux import pega_id, pega_local, tupla1, tupla2

# ============ QUESTÃO A ============ #
# a) Calcular a distância percorrida por um determinado robô ao longo do processo de resgate das vítimas.
# Considere que a distância total percorrida deve ser calculada como a soma de todas as distâncias entre os
# pontos de passagem do robô;

# COMPREENSÃO DO PROBLEMA: deve-se extrair a tupla de um robô da lista de entrada de acordo com o id dado.
# Em seguida, calcular a distância total que ele percorreu (partindo da origem) e retornar esse valor.


def dist_euclid(p1, p2):
    """ Calcula a distância entre dois pontos cartesianos
    Escopo: função global paramétrica
    Dados de entrada: Dois pontos reais p1 e p2 de duas coordenadas
    Dados de saída: A distância entre os dois pontos
    """

    return sqrt((tupla1(p1) - tupla1(p2))**2 + (tupla2(p1) - tupla2(p2))**2)


def lista_tuplas_robo_id(listaRobos, id):
    """ Extrai todas as tuplas de um mesmo robô da lista de robôs de entrada
    Escopo: função global paramétrica
    Dados de entrada: Lista de robôs de entrada e id de um robô
    Dados de saída: Tuplas de informações um único robô da lista de robôs
    """

    # Forma lista a partir de tuplas que contenham o id de entrada
    return [x for x in listaRobos if tupla1(x) == id]


def pega_pontos_robo(listaRobos, id):
    """ Extrai todos os pontos percorridos por um mesmo robô da lista de robôs de entrada
    Escopo: função global paramétrica
    Dados de entrada: Lista de robôs de entrada e id de um robô
    Dados de saída: Lista de todos os pontos percorridos por um único robô da lista de robôs;
    inclui origem como ponto de partida.
    """

    tuplasRobo = lista_tuplas_robo_id(listaRobos, id)

    # Os robôs partem da origem, portanto devemos adicioná-la à lista de pontos
    return [(0, 0)] + list(map(pega_local, tuplasRobo))


def distancia_total(pontos):
    """ Calcula a distância total entre uma lista de pontos
    somando a distância entre um ponto e o próximo até o fim da lista.
    Assume que a origem inicia a lista de pontos.
    Escopo: função global paramétrica
    Dados de entrada: Lista de pontos
    Dados de saída: Distância total somando a distância entre um ponto e o próximo até o fim da lista
    Se não houver robô com o id fornecido ou o robô tiver percorrido menos de 2 pontos, retorna None
    """

    try:
        if len(pontos) < 2:  # IndexError
            print("Robô não existe ou não enviou dados para a CP.")
        elif len(pontos) == 2:
            return dist_euclid(pontos[0], pontos[1])
        else:
            return dist_euclid(pontos[0], pontos[1]) + distancia_total(pontos[1:])
    except IndexError:  # Precisamos de ao menos 2 pontos para calcular distância
        pass


# Função principal do problema A
def distancia_total_robo(listaRobos, id):
    """ Calcula a distância percorrida por um robô da lista de robôs dado seu id
    Escopo: Função global paramétrica
    Dados de entrada: Lista de dados de robôs e id de um robô
    Dados de saída: Lista de todos os pontos percorridos pelo robô
    """

    pontosPercorridosRobo = pega_pontos_robo(listaRobos, id)

    return distancia_total(pontosPercorridosRobo)
