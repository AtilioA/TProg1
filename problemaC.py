# Módulo com funções para solucionar o problema C
# Autores: Atílio Antônio Dadalto
# Disciplina: Programação I, ministrada por Jordana Sarmenghi Salamon em 2019/1

from problemaA import distancia_total
from problemaB import caminhos_percorridos, ids_robos
from roboAux import tupla2

# ============ QUESTÃO C ============ #
# c) Exiba os caminhos percorridos por todos os robôs que entraram no terreno de busca,
# ordenados crescentemente pela distância total percorrida;

# COMPREENSÃO DO PROBLEMA: deve-se calcular as distâncias percorridas por todos os robôs, adicionando-as
# em uma tupla que será ordenada a partir das distâncias, impressa na tela e então retornada

# PLANEJAMENTO:
# Criar as seguintes funções:
# - Função para ordenar lista em ordem crescente
# - Função para juntar id, distância total e caminho percorrido de todos os robôs em uma lista de  tuplas
# - Ordenar essa lista pelas distâncias nas tuplas


def tupla_caminhos_percorridos(listaRobos, ids, distsTotais, caminhos):
    if not ids:
        return ids
    elif not distsTotais:
        return distsTotais
    elif not caminhos:
        return caminhos
    else:
        return [(ids[0], distsTotais[0], caminhos[0])] + tupla_caminhos_percorridos(listaRobos, ids[1:], distsTotais[1:], caminhos[1:])


def merge_ordenada_tupla(l1, l2):
    """ Com duas listas de tuplas ordenadas conforme o segundo elemento,
    junta as duas de forma ordenada
    Escopo: Função global paramétrica
    Dados de entrada: Duas listas de tuplas numéricas ordenadas pelo segundo elemento
    Dados de saída: Uma lista de tuplas ordenada pelo segundo elemento das tuplas
    formada a partir da junção ordenada das duas listas de entrada

    Ex: l1 = [(5, 5)] e l2 = [(5, 0)]:
    merge_ordenada([(5, 5)], [(5, 0)])
    [(5, 0)] + merge_ordenada([], [(5, 5)])
    l1 é vazia, retorna l2
    [(5, 0)] + [(5, 5)]
    [(5, 0), (5, 5)]
    """

    if not l1:
        return l2
    elif not l2:
        return l1
    elif tupla2(l1[0]) <= tupla2(l2[0]):  # tupla2(l1[0]) é menor ou igual, portanto será primeiro
        return [l1[0]] + merge_ordenada_tupla(l1[1:], l2)
    else:  # tupla2(l2[0]) é menor, portanto será primeiro
        return [l2[0]] + merge_ordenada_tupla(l1, l2[1:])


def merge_sort_tupla(lista):
    """ Dada uma lista de tuplas de entrada, ordena-a por merge sort,
    tendo como referência para a ordenação os segundos elementos das tuplas
    Escopo: Função global paramétrica
    Dados de entrada: Uma lista de tuplas numéricas
    Dados de saída: Uma lista de tuplas numéricas ordenadas a partir do segundo elemento
    """

    if len(lista) <= 1:
        return lista
    else:
        metade = len(lista) // 2  # Pega o índice do meio da lista
        return merge_ordenada_tupla(merge_sort_tupla(lista[:metade]), merge_sort_tupla(lista[metade:]))


def distancias_totais_robos(listaRobos):
    """ Calcula as distâncias totais que todos os robôs percorreram
    Escopo: Função global paramétrica
    Dados de entrada: Lista de robôs
    Dados de saída: Lista de
    """

    return list(map(distancia_total, caminhos_percorridos(listaRobos)))


# Função principal do problema C
def caminhos_robos_crescente(listaRobos):
    """ Dada a lista de robôs, imprime o caminho de cada robô (em ordem crescente de distância)
    Escopo: Função global paramétrica
    Dados de entrada: A lista de dados sobre os robôs
    Dados de saída: Uma lista de distâncias ordenada
    """

    try:
        if not listaRobos:  # ValueError
            print("Lista vazia não possui robôs.")
        else:
            ids = ids_robos(listaRobos)
            caminhos = caminhos_percorridos(listaRobos)
            distsTotais = distancias_totais_robos(listaRobos)

            tuplasComDistancias = tupla_caminhos_percorridos(listaRobos, ids, distsTotais, caminhos)
            listaTuplasOrdenadasPorDistancia = merge_sort_tupla(tuplasComDistancias)

            return listaTuplasOrdenadasPorDistancia
    except ValueError:
        pass
