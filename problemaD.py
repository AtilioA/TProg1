# Módulo com funções para solucionar o problema D
# Autores: Atílio Antônio Dadalto
# Disciplina: Programação I, ministrada por Jordana Sarmenghi Salamon em 2019/1

from roboAux import *
from problemaC import *


# ============ QUESTÃO D ============ #
# d) Forneça a identidade do(s) robô(s) que conseguiu(ram) informar o maior número de vítimas
# (considerando que não há duplicação de identificação de vítima por um mesmo robô).

# COMPREENSÃO DO PROBLEMA: deve-se calcular o número de vítimas que cada robô avistou
# e identificar o robô que avistou o maior número.
# Retornar mais de um robô caso o maior número seja repetido.

# PLANEJAMENTO:
# Criar as seguintes funções:
# - Função para extrair número de vítimas vistas em cada ponto passado por um robô - OK
# - Função para somar elementos de uma lista - OK
# - Aplicar essas duas últimas funções para todos os robôs da lista de entrada - OK
# - Extrair maior número da lista obtida no último item - OK
# - Buscar na lista original os robôs que obtiveram o número obtido no último item e retornar os IDs - OK


def robos_mais_vitimas(ids, indicesVitimas):
    """ Retorna ids dos robôs que avistaram mais vítimas
    Escopo: Função global paramétrica
    Dados de entrada: Lista de ids dos robôs e índices de robôs que avistaram mais vítimas
    Dados de saída: Lista de robôs que avistaram mais vítimas
    """

    if len(indicesVitimas) == 1:
        return [ids[indicesVitimas[0]]]
    else:
        return [ids[indicesVitimas[0]]] + robos_mais_vitimas(ids, indicesVitimas[1:])

# Função principal do problema D
def ids_mais_vitimas(listaRobos):
    """ Retorna os ids do robôs que avistaram o maior número de vítimas
    Escopo: Função global paramétrica
    Dados de entrada: Lista com informações sobre todos os robôs
    Dados de saída: Lista com ids de robôs (pode haver mais de um) que avistaram o maior número de vítimas
    """

    try:
        if not listaRobos:  # ValueError
            print("Lista vazia não possui robôs.")
        else:
            ids = ids_robos(listaRobos)
            indices = indices_mais_vitimas(listaRobos)
            idsVitimas = robos_mais_vitimas(ids, indices)

            return idsVitimas
    except ValueError:
        pass


def lista_vitimas_robo(listaRobos, id):
    """ Retorna a lista de vítimas avistadas por um robô dado o id deste
    Escopo: Função global paramétrica
    Dados de entrada: Lista com informações sobre todos os robôs e o id de um robô da lista
    Dados de saída: Lista com número de vítimas avistadas por um robô em cada ocorrência
    """

    return [pega_vitimas(x) for x in listaRobos if tupla1(x) == id]


def total_vitimas_robo(listaRobos, id):
    """ Retorna o total de vítimas avistadas por um robô dado seu id
    Escopo: Função global paramétrica
    Dados de entrada: Lista com informações sobre todos os robôs e o id de um robô da lista
    Dados de saída: total de vítimas avistadas por um robô
    """

    listaVitimas = lista_vitimas_robo(listaRobos, id)
    return soma_lista(listaVitimas)


def indices_mais_vitimas(listaRobos):
    """ Retorna os índices dos ids dos robôs que avistaram mais vítimas
    Escopo: Função global paramétrica
    Dados de entrada: Lista de robôs
    Dados de saída: Lista de índices
    """

    lista_vitimas_robos = total_vitimas_robos(listaRobos)
    indices = indices_maximos(lista_vitimas_robos)

    return indices


def total_vitimas_robos(listaRobos):
    """ Retorna o número total de vítimas que cada robô avistou
    Escopo: Função global paramétrica
    Dados de entrada: Lista de robôs
    Dados de saída: Valor numérico
    """

    ids = ids_robos(listaRobos)

    return list(map(lambda id: total_vitimas_robo(listaRobos, id), ids))
