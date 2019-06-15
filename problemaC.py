# Módulo com funções auxiliares
# Autores: Atílio Antônio Dadalto
# Disciplina: Programação I, 2019/1, ministrada por Jordana Sarmenghi Salamon em 2019/1

from roboAux import *
from functools import reduce

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

def caminhosRobosCrescente(listaRobos):
    ''' Função caminhosRobosCrescente()
    Descrição: Dada a lista de robôs, imprime o caminho de cada robô (em ordem crescente de distância)
    Escopo: Função global paramétrica
    Dados de entrada: A lista de dados sobre os robôs
    Dados de saída: Uma lista de distâncias ordenada
    '''
    listaDistancias = distanciasTotaisRobos(listaRobos)

    listaDistanciasOrdenadas = mergeSort(listaDistancias)
    return listaDistanciasOrdenadas


def mergeOrdenada(l1, l2):
    ''' Função mergeOrdenada()
    Descrição: Com duas listas ordenadas de entrada, junta as duas de forma ordenada
    Escopo: Função global paramétrica
    Dados de entrada: Duas listas numéricas ordenadas
    Dados de saída: Uma lista ordenada tuplasRoboIdda a partir da junção ordenada das duas de entrada
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

from problemaA import *
from problemaB import *
from problemaD import *
