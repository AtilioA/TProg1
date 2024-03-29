# Módulo com funções para solucionar o problema B
# Autores: Atílio Antônio Dadalto e Ícaro Madalena do Nascimento
# Disciplina: Programação I, ministrada por Jordana Sarmenghi Salamon em 2019/1

from problemaA import (dist_euclid, distancia_total, lista_tuplas_robo_id,
                       pega_pontos_robo)
from roboAux import max_lista, pega_id, pega_instante, ultimo

# ============ QUESTÃO B ============ #
# b) Determine qual dos robôs apresenta o seu último ponto de passagem no terreno de busca que
#  possui a maior distância em relação à origem.
#  Exiba o caminho percorrido pelo robô e o tempo total do percurso;

# COMPREENSÃO DO PROBLEMA: deve-se extrair, da lista de entrada, o último ponto de passagem de todos os robôs.
# Com isso, determinar qual robô possui ponto mais longe da origem e então imprimir caminho
# percorrido pelo robô, além de determinar tempo do percurso.


def caminhos_percorridos(listaRobos):
    """ Retorna uma lista com todos os pontos percorridos por todos os robôs
    Escopo: Função global paramétrica
    Dados de entrada: Lista de robôs
    Dados de saída: Lista de lista de pontos
    """

    ids = ids_robos(listaRobos)
    caminhos = list(map(lambda id: pega_pontos_robo(listaRobos, id), ids))
    return caminhos


def ultimos_pontos_robos(listaRobos):
    """ Retorna lista com últimos pontos de todos os robôs
    Escopo: Função global paramétrica
    Dados de entrada: Lista de robôs
    Dados de saída: Lista com últimos pontos de todos os robôs
    """

    percursos = caminhos_percorridos(listaRobos)
    return list(map(ultimo, percursos))


def dist_origem_ponto(p):
    """ Calcula a distância da origem até um ponto
    Escopo: Função global paramétrica
    Dados de entrada: p ponto real de duas coordenadas
    Dados de saída: Valor numérico
    """

    return dist_euclid((0, 0), p)


def dist_origem_ultimo_ponto(percursos):
    """ Calcula a distância da origem até o último ponto de uma lista de tuplas de robôs
    Escopo: Função global paramétrica
    Dados de entrada: Lista de percursos (lista de pontos) dos robôs
    Dados de saída: Lista de valores numéricos
    """

    return list(map(lambda ponto: dist_origem_ponto(ponto), percursos))


def indices_maximos(lista):
    """ Retorna os índices de todas as ocorrências de valor máximo na lista
    Escopo: Função global paramétrica
    Dados de entrada: Lista numérica
    Dados de saída: Lista numérica de índices
    Ex: l1 = [1, 13, 5, 13, 5, 0]:
    maximo = 13
    return [1, 3]
    """

    maximo = max_lista(lista)
    return [x for x, i in enumerate(lista) if i == maximo]


def indices_ids_mais_distantes(listaRobos):
    """ Retorna os índices dos ids dos robôs mais distantes
    Escopo: Função global paramétrica
    Dados de entrada: Lista de robôs
    Dados de saída: Lista de índices
    """

    distsÚltimosPontos = dist_origem_ultimo_ponto(ultimos_pontos_robos(listaRobos))
    indices = indices_maximos(distsÚltimosPontos)

    return indices


def tempo_percurso(listaRobos, id):
    """ Retorna o instante da última ocorrência de um robô
    Escopo: Função global paramétrica
    Dados de entrada: Lista de robôs e id de robô na lista
    Dados de saída: Valor numérico do tempo de percurso de um robô
    """

    robo = lista_tuplas_robo_id(listaRobos, id)

    if not robo:
        return 0
    else:
        tempo = pega_instante(robo[-1])
        return tempo


# Função principal do problema B
def imprime_robos_mais_distantes(listaRobos):
    """ Imprime os robôs que encontram-se mais distantes da origem
    Escopo: Função global paramétrica
    Dados de entrada: Lista de robôs
    Dados de saída: None
    """

    try:
        if not listaRobos:  # ValueError
            print("Lista vazia não possui robôs.")
        else:
            ids = ids_robos(listaRobos)
            indices = indices_ids_mais_distantes(listaRobos)

            idsMaisDistantes = robos_mais_distantes(ids, indices)
            if len(idsMaisDistantes) == 1:
                print("Robô mais distante:")
            else:
                print("Robôs mais distantes:")
            print(idsMaisDistantes)

            if len(idsMaisDistantes) == 1:
                print("Percurso do robô:")
            else:
                print("Percursos dos robôs, respectivamente:")
            print(list(map(lambda id: pega_pontos_robo(listaRobos, id), idsMaisDistantes)))

            if len(idsMaisDistantes) == 1:
                print("Tempo total do percurso:")
            else:
                print("Tempo total dos percursos, respectivamente:")
            print(list(map(lambda id: tempo_percurso(listaRobos, id), idsMaisDistantes)))

            return None
    except TypeError:
        pass


def remove_duplicata(lista):
    """ Cria uma nova lista dada uma lista de entrada sem os elementos duplicados desta
    Escopo: Função global paramétrica
    Dados de entrada: Lista válida
    Dados de saída: Lista sem elementos duplicados
    """

    if len(lista) < 2:
        return lista
    elif lista[0] not in lista[1:]:  # O elemento é único, podemos adicioná-lo na lista final
        return [lista[0]] + remove_duplicata(lista[1:])
    else:  # O elemento não é único, não o adicionamos ainda
        return remove_duplicata(lista[1:])


def ids_robos(listaRobos):
    """ Cria uma lista com os ids dos robôs existentes
    na lista de robôs (sem repetição)
    Escopo: Função global paramétrica
    Dados de entrada: Lista de robôs
    Dados de saída: Lista com ids dos robôs, sem repetição de id
    """

    listaIdsRepetidos = list(map(pega_id, listaRobos))
    return remove_duplicata(listaIdsRepetidos)


def robos_mais_distantes(ids, indicesDistancia):
    """ Retorna ids dos robôs mais distantes
    Escopo: Função global paramétrica
    Dados de entrada: Lista de ids, lista de índices de robôs mais distantes
    Dados de saída: Lista de ids de robôs mais distantes
    """

    try:
        if not indicesDistancia:  # ValueError
            print("Lista vazia não possui robôs.")
        elif len(indicesDistancia) == 1:
            return [ids[indicesDistancia[0]]]
        else:
            return [ids[indicesDistancia[0]]] + robos_mais_distantes(ids, indicesDistancia[1:])
    except ValueError:
        pass
