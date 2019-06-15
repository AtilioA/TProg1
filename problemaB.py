from roboAux import *
from functools import reduce

# ============ QUESTÃO B ============ #
# b) Determine qual dos robôs apresenta o seu último ponto de passagem no terreno de busca que
#  possui a maior distância em relação à origem.
#  Exiba o caminho percorrido pelo robô e o tempo total do percurso;

# - Extrair, da lista de entrada, o último ponto de passagem de todos os robôs
# - Determinar qual robô possui ponto mais longe da origem
# - Imprimir caminho percorrido pelo robô, determinar tempo do percurso

# COMPREENSÃO DO PROBLEMA: deve-se obter o último ponto de passagem de todos os robôs e retornar
# o robô que possui o último ponto mais distante da origem.

# PLANEJAMENTO:
# Criar as seguintes funções:
# - Função para obter uma lista com o último ponto de todos os robôs da lista de entrada - OK
# - Função para calcular a distância da origem a todos esses pontos, retornando em uma lista - OK
# - Função para extrair maior número da lista obtida no último item - OK
# - Função para buscar na lista original os robôs que obtiveram o número obtido no último item e retornar os IDs - OK
# - Função para determinar tempo de percurso de um robô, dado seu percurso - OK
# - Função para imprimir percurso de um robô - OK


def tempoPercurso(listaRobos, id):
    ''' Função: nomeDaFunção()
    Descrição: o que a função faz
    Escopo: escopo da função (global/local, paramétrica/constante)
    Dados de entrada: x, y válidos, etc
    Dados de saída: z, w, l lista numérica, b valor booleano, etc
    '''
    robo = tuplasRoboId(listaRobos, id)

    if len(robo) == 0:
        return 0
    elif len(robo) > 1:
        tempo = pegaInstante(robo[-1]) - pegaInstante(robo[0]) # Considera o primeiro instante inteiro?
        return tempo
    else:
        tempo = pegaInstante(robo[-1])
        return tempo


def imprimeRobosMaisDistantes(listaRobos):
    ''' Função: nomeDaFunção()
    Descrição: o que a função faz
    Escopo: escopo da função (global/local, paramétrica/constante)
    Dados de entrada: x, y válidos, etc
    Dados de saída: z, w, l lista numérica, b valor booleano, etc
    '''
    ids = idsRobos(listaRobos)
    indices = indicesMaisDistantes(listaRobos)

    idsMaisDistantes = robosMaisDistantes(ids, indices)
    if len(idsMaisDistantes) == 1:
        print("Robô mais distante:")
    else:
        print("Robôs mais distantes:")
    print(idsMaisDistantes)

    if len(idsMaisDistantes) == 1:
        print("Percurso do robô:")
    else:
        print("Percursos dos robôs, respectivamente:")
    print(list(map(lambda id: pegaPontosRobo(listaRobos, id), idsMaisDistantes)))

    if len(idsMaisDistantes) == 1:
        print("Tempo total do percurso:")
    else:
        print("Tempo total dos percursos, respectivamente:")
    print(list(map(lambda id: tempoPercurso(listaRobos, id), idsMaisDistantes)))

    return 1


def removeDuplicata(lista):
    ''' Função removeDuplicata
    Descrição: Cria uma nova lista dada uma lista de entrada sem elementos duplicados desta
    Escopo: Função global paramétrica
    Dados de entrada: lista válida
    Dados de saída: lista sem elementos duplicados
    '''

    if len(lista) < 2:
        return lista
    elif lista[0] not in lista[1:]:
        return [lista[0]] + removeDuplicata(lista[1:])
    else:
        return removeDuplicata(lista[1:])


def idsRobos(listaRobos):
    ''' Função idsRobos
    Descrição: Cria uma lista com os ids dos robôs existentes
    na lista de robôs (sem repetição)
    Escopo: Função global paramétrica
    Dados de entrada: lista de robôs
    Dados de saída: lista com ids dos robôs, sem repetição de id
    '''

    listaIdsRepetidos = list(map(tupla1, listaRobos))
    return removeDuplicata(listaIdsRepetidos)


def caminhosPercorridos(listaRobos):
    ''' Função: nomeDaFunção()
    Descrição: o que a função faz
    Escopo: escopo da função (global/local, paramétrica/constante)
    Dados de entrada: x, y válidos, etc
    Dados de saída: z, w, l lista numérica, b valor booleano, etc
    '''
    ids = idsRobos(listaRobos)
    caminhos = (map(lambda id: pegaPontosRobo(listaRobos, id), ids))
    return list(caminhos)


def distanciasTotaisRobos(listaRobos):
    ''' Função: nomeDaFunção()
    Descrição: o que a função faz
    Escopo: escopo da função (global/local, paramétrica/constante)
    Dados de entrada: x, y válidos, etc
    Dados de saída: z, w, l lista numérica, b valor booleano, etc
    '''
    return list(map(distanciaTotal, caminhosPercorridos(listaRobos)))


def ultimosPontosRobos(listaRobos):
    ''' Função: nomeDaFunção()
    Descrição: o que a função faz
    Escopo: escopo da função (global/local, paramétrica/constante)
    Dados de entrada: x, y válidos, etc
    Dados de saída: z, w, l lista numérica, b valor booleano, etc
    '''
    percursos = caminhosPercorridos(listaRobos)
    return list(map(pegaVitimas, percursos))


def distOrigemPonto(p):
    ''' Função: nomeDaFunção()
    Descrição: o que a função faz
    Escopo: escopo da função (global/local, paramétrica/constante)
    Dados de entrada: x, y válidos, etc
    Dados de saída: z, w, l lista numérica, b valor booleano, etc
    '''
    return distEuclid((0,0), p)


def distOrigemUltimoPonto(percursos):
    ''' Função: nomeDaFunção()
    Descrição: o que a função faz
    Escopo: escopo da função (global/local, paramétrica/constante)
    Dados de entrada: x, y válidos, etc
    Dados de saída: z, w, l lista numérica, b valor booleano, etc
    '''
    return list(map(lambda ponto: distOrigemPonto(ponto), percursos))


def indicesMaximos(lista):
    ''' Função: nomeDaFunção()
    Descrição: o que a função faz
    Escopo: escopo da função (global/local, paramétrica/constante)
    Dados de entrada: x, y válidos, etc
    Dados de saída: z, w, l lista numérica, b valor booleano, etc
    '''
    maximo = maxLista(lista)
    return [x for x, i in enumerate(lista) if i == maximo]


def indicesMaisDistantes(listaRobos):
    ''' Função: nomeDaFunção()
    Descrição: o que a função faz
    Escopo: escopo da função (global/local, paramétrica/constante)
    Dados de entrada: x, y válidos, etc
    Dados de saída: z, w, l lista numérica, b valor booleano, etc
    '''
    distsÚltimosPontos = distOrigemUltimoPonto(ultimosPontosRobos(listaRobos))
    indices = indicesMaximos(distsÚltimosPontos)

    return indices


def robosMaisDistantes(ids, indicesDistancia):
    ''' Função: nomeDaFunção()
    Descrição: o que a função faz
    Escopo: escopo da função (global/local, paramétrica/constante)
    Dados de entrada: x, y válidos, etc
    Dados de saída: z, w, l lista numérica, b valor booleano, etc
    '''
    if len(indicesDistancia) == 1:
        return [ids[indicesDistancia[0]]]
    else:
        return [ids[indicesDistancia[0]]] + robosMaisDistantes(ids, indicesDistancia[1:])

from problemaA import *
from problemaC import *
from problemaD import *
