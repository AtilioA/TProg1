# Módulo com funções para solucionar o problema C
# Autores: Atílio Antônio Dadalto
# Disciplina: Programação I, ministrada por Jordana Sarmenghi Salamon em 2019/1

from problemaB import ids_robos, caminhos_percorridos, distancias_totais_robos
from roboAux import tupla2

# ============ QUESTÃO C ============ #
# c) Exiba os caminhos percorridos por todos os robôs que entraram no terreno de busca,
# ordenados crescentemente pela distância total percorrida;

# COMPREENSÃO DO PROBLEMA: deve-se calcular as distâncias percorridas por todos os robôs, adicionando-as
# em uma lista que será ordenada, imprimida na tela e então retornada

# PLANEJAMENTO:
# Criar as seguintes funções:
# - Função para ordenar lista em ordem crescente - OK
# - Função para aplicar a função da questão (b) em todos os robôs da lista de entrada - OK
# - Ordenar essa tupla pelas distâncias - OK


def tupla_caminhos_percorridos(listaRobos, ids, distsTotais, caminhos):
    if not ids:
        return ids
    elif not distsTotais:
        return distsTotais
    elif not caminhos:
        return caminhos
    else:
        return [(ids[0], distsTotais[0], caminhos[0])] + tupla_caminhos_percorridos(listaRobos, ids[1:], distsTotais[1:], caminhos[1:])


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


def merge_ordenada_tupla(l1, l2):
    """ Com duas listas ordenadas de entrada, junta as duas de forma ordenada
    Escopo: Função global paramétrica
    Dados de entrada: Duas listas numéricas ordenadas
    Dados de saída: Uma lista ordenada tuplasRoboIdda a partir da junção ordenada das duas de entrada
    Pega o primeiro elemento que seja o menor dentre as duas listas
    e junta com o resultado da função chamando com resto da lista "menor"
    Ex: l1 = [1, 2] e l2 = [3, 4]:
    merge_ordenada([1, 2], [3, 4])
    [1] + merge_ordenada([2], [3, 4])
    [2] + merge_ordenada([], [3, 4])
    len(l1) == 0, retorna l2
    [1] + [2] + [3, 4]
    [1, 2, 3, 4]
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
    """ Dada uma lista de entrada, ordena-a por merge_sort
    Escopo: Função global paramétrica
    Dados de entrada: Uma lista numérica
    Dados de saída: Uma lista numérica ordenada
    """

    if len(lista) <= 1:
        return lista
    else:
        metade = len(lista) // 2  # Pega o índice do meio da lista
        return merge_ordenada_tupla(merge_sort_tupla(lista[:metade]), merge_sort_tupla(lista[metade:]))
