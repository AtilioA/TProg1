# Módulo com funções para solucionar o problema C
# Autores: Atílio Antônio Dadalto
# Disciplina: Programação I, ministrada por Jordana Sarmenghi Salamon em 2019/1

from problemaB import *

# ============ QUESTÃO C ============ #
# c) Exiba os caminhos percorridos por todos os robôs que entraram no terreno de busca,
# ordenados crescentemente pela distância total percorrida;

# COMPREENSÃO DO PROBLEMA: deve-se calcular as distâncias percorridas por todos os robôs, adicionando-as
# em uma lista que será ordenada, imprimida na tela e então retornada

# PLANEJAMENTO:
# Criar as seguintes funções:
# - Função para ordenar lista em ordem crescente - OK
# - Função para aplicar a função da questão (a) em todos os robôs da lista de entrada - OK
# - Ordenar essa lista de distâncias - OK


def caminhos_robos_crescente(listaRobos):
    """ Dada a lista de robôs, imprime o caminho de cada robô (em ordem crescente de distância)
    Escopo: Função global paramétrica
    Dados de entrada: A lista de dados sobre os robôs
    Dados de saída: Uma lista de distâncias ordenada
    """

    try:
        if len(listaRobos) == 0:  # ValueError
            print("Lista vazia não possui robôs.")
        else:
            listaDistancias = distancias_totais_robos(listaRobos)

            listaDistanciasOrdenadas = merge_sort(listaDistancias)
            return listaDistanciasOrdenadas
    except ValueError:
        pass


def merge_ordenada(l1, l2):
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

    if len(l1) == 0:
        return l2
    elif len(l2) == 0:
        return l1
    elif l1[0] <= l2[0]:
        return [l1[0]] + merge_ordenada(l1[1:], l2)  # l1[0] é menor ou igual, portanto será primeiro
    else:
        return [l2[0]] + merge_ordenada(l1, l2[1:])  # l2[0] é menor, portanto será primeiro


def merge_sort(lista):
    """ Dada uma lista de entrada, ordena-a por merge_sort
    Escopo: Função global paramétrica
    Dados de entrada: Uma lista numérica
    Dados de saída: Uma lista numérica ordenada
    """

    if len(lista) <= 1:
        return lista
    else:
        metade = len(lista) // 2  # Pega o índice do meio da lista
        return merge_ordenada(merge_sort(lista[:metade]), merge_sort(lista[metade:]))
