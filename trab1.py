# Auxílio ao resgate de vítimas por robôs em ambientes acidentados
# Autores: Atílio Antônio Dadalto
# Disciplina: Programação I, ministrada por Jordana Sarmenghi Salamon em 2019/1

# ALGUMAS ESPECIFICAÇÕES DO TRABALHO:
# Considere que todos os robôs partem do mesmo ponto inicial: (0,0).
# As informações enviadas pelos robôs de resgate contêm os seguintes registros:
# a identificação do robô,
# o instante em que o robô passou em um determinado ponto da área afetada,
# o ponto no plano cartesiano referente ao incidente registrado, e
# o número de vítimas presentes na área de visibilidade do robô.

# Considerando uma lista com tais informações como os dados de entrada disponíveis, faça um programa em Python que responda às seguintes solicitações:
# Entrada no modelo:
# listaRobôs = [(id1, instante1, ponto1, nVítimas1), (id2, instante2, ponto2, nVítimas2)]

# Compreensão do problema e planejamento da solução

# "(Ao importar funções de algum módulo, utilize a opção de importação específica)"
import random
from roboAux import *
from math import *
from functools import reduce
import sys # Para testes (mergeSort por exemplo) apenas, não irá para a versão final
sys.setrecursionlimit(10000) # Para aumentar limite de recursão do Python


# "Cada função deve ter um comentário com sua descrição, dados de entrada e saída.
# Na descrição, diga se a função é global ou local, paramétrica ou não, e por quê.
# Realizar a validação dos dados."
# Vamos comentar as funções assim:
def template(entradas):
    ''' Função: nomeDaFunção()
    Descrição: o que a função faz
    Escopo: escopo da função (global/local, paramétrica/constante)
    Dados de entrada: x, y válidos, etc
    Dados de saída: z, w, l lista numérica, b valor booleano, etc
    '''

    # Resto da função. A validação ocorre aqui, com try, Exception() e etc

listaRobôs = [('robo3', 1, (7, 7), 3), ('robo4', 2, (7, 5), 2), ('robo3', 3, (5, 4), 3), ('robo3', 4, (8, 1), 4), ('robo4', 5, (4, 5), 3), ('robo5', 6, (7, 7), 4), ('robo5', 7, (6, 4), 5), ('robo3', 8, (7, 2), 3), ('robo5', 9, (6, 4), 4)]

# ============ QUESTÃO A ============ # - OK
# a) Calcular a distância percorrida por um determinado robô ao longo do processo de resgate das vítimas.
# Considere que a distância total percorrida deve ser calculada como a soma de todas as distâncias entre os
# pontos de passagem do robô;

# COMPREENSÃO DO PROBLEMA: deve-se extrair a tupla de um robô da lista de entrada de acordo com o id dado.
# Em seguida, calcular a distância total que ele percorreu e retornar esse valor.

# PLANEJAMENTO:
# Criar as seguintes funções:
# - Função para cálculo de distância no plano cartesiano - OK
# - Função para extrair tuplas de uma lista dado um elemento identificador das tuplas - OK

def distEuclid(p1, p2):
    ''' Função: distEuclid()
    Descrição: Calcula a distância entre dois pontos cartesianos
    Escopo: função global paramétrica
    Dados de entrada: dois pontos reais p1 e p2
    Dados de saída: a distância entre os pontos
    '''

    return sqrt((tupla1(p1) - tupla1(p2))**2 + (tupla2(p1) - tupla2(p2))**2)

def listaTuplaRobôID(listaRobôs, id):
    ''' Função: listaTuplaRobôID()
    Descrição: Extrai todas as tuplas de um mesmo robô da lista de robôs de entrada
    Escopo: função global paramétrica
    Dados de entrada: lista de robôs de entrada e id de um robô
    Dados de saída: tuplas de informações um único robô da lista de robôs
    Se não houver robô com o id fornecido ou o robô tiver percorrido menos de 2 pontos, retorna -1
    '''

    # def robôEscolhido(robo, id):
    #     if (tupla1(robo)) == f'robo{id}':
    #         return True
    #     else:
    #         return False

    return list(filter(lambda x: (tupla1(x) == id), listaRobôs))
    # return [x for x in listaRobôs if tupla1(x) == id]


# - Função para calcular a distância entre os pontos percorridos pelo robô
def pegaPontosRobô(listaRobôs, id):
    ''' Função: pegaPontosRobô()
    Descrição: Extrai todos os pontos percorridos por um mesmo robô da lista de robôs de entrada
    Escopo: função global paramétrica
    Dados de entrada: lista de robôs de entrada e id de um robô
    Dados de saída: lista de todos os pontos percorridos por um único robô da lista de robôs
    '''

    tuplasRobô = listaTuplaRobôID(listaRobôs, id)
    return list(map(tupla3, tuplasRobô))


def pegaPontosTuplaRobô(tuplasRobô):
    ''' Função: pegaPontosTuplaRobô()
    Descrição: Cria todos os pontos percorridos por um robô de uma lista de tuplas de informações um mesmo robô
    Escopo: função global paramétrica
    Dados de entrada: lista de tuplas de um robô
    Dados de saída: lista de todos os pontos percorridos pelo robô
    '''

    return list(map(tupla3, tuplasRobô))


def distânciaTotal(pontos):
    ''' Função: distânciaTotal()
    Descrição: Calcula a distância total entre uma lista de pontos somando
    a distância entre um ponto e o próximo até o fim da lista
    Escopo: função global paramétrica
    Dados de entrada: Lista de pontos
    Dados de saída: Distância total somando a distância entre um ponto e o próximo até o fim da lista
    '''

    if len(pontos) < 2:
        return -1
    elif len(pontos) == 2:
        return distEuclid(pontos[0], pontos[1])
    else:
        return distEuclid(pontos[0], pontos[1]) + distânciaTotal(pontos[1:])

    return distânciaTotal(distânciasRobô)


def distânciaTotalRobô(listaRobôs, id):
    ''' Função: distânciaTotalRobô() zoada
    Descrição: Calcula a distância percorrida por um robô da lista de robôs dado seu id
    Escopo: função global paramétrica
    Dados de entrada: lista de tuplas de um robô
    Dados de saída: lista de todos os pontos percorridos pelo robô
    '''
    tuplasRobô = listaTuplaRobôID(listaRobôs, id)
    pontosPercorridosRobô = pegaPontosTuplaRobô(tuplasRobô)
    return distânciaTotal(pontosPercorridosRobô)


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
# - Função para extrair maior número da lista obtida no último item -OK
# - Função para buscar na lista original os robôs que obtiveram o número obtido no último item e retornar os IDs - OK
# - Função para determinar tempo de percurso de um robô, dado seu percurso
# - Função para imprimir percurso de um robô - OK

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


def idsRobôs(listaRobôs):
    ''' Função idsRobôs
    Descrição: Cria uma lista com os ids dos robôs existentes
    na lista de robôs (sem repetição)
    Escopo: Função global paramétrica
    Dados de entrada: lista de robôs
    Dados de saída: lista com ids dos robôs, sem repetição de id
    '''

    listaIdsRepetidos = list(map(tupla1, listaRobôs))
    return removeDuplicata(listaIdsRepetidos)


def caminhosPercorridos(listaRobôs):
    ids = idsRobôs(listaRobôs)
    caminhos = (map(lambda x: pegaPontosRobô(listaRobôs, x), ids))
    return list(caminhos)


def distânciasTotaisRobôs(listaRobôs):
    return list(map(distânciaTotal, caminhosPercorridos(listaRobôs)))


def imprimePercurso(listaRobôs, id):
    print(pegaPontosRobô(listaRobôs, id))
    return 1


def últimosPontosRobôs(listaRobôs):
    percursos = caminhosPercorridos(listaRobôs)
    return list(map(tupla4, percursos))


def distOrigemPonto(p):
    return distEuclid((0,0), p)


def distOrigemÚltimoPonto(percursos):
    return list(map(lambda x: distOrigemPonto(x), percursos))

def índicesMáximos(lista):
    maximo = maxLista(lista)
    return [x for x, i in enumerate(lista) if i == maximo]

def índicesMaisDistantes(listaRobôs):
    distsÚltimosPontos = distOrigemÚltimoPonto(últimosPontosRobôs(listaRobôs))
    maiorDistância = maxLista(distsÚltimosPontos)

    ids = idsRobôs(listaRobôs)
    indices = índicesMáximos(distsÚltimosPontos)

    return indices

def robôsMaisDistantes(ids, indicesDistancia):
    if len(indicesDistancia) == 1:
        return [ids[indicesDistancia[0]]]
    else:
        return [ids[indicesDistancia[0]]] + robôsMaisDistantes(ids, indicesDistancia[1:])


print("Índices dos robôs mais distantes:")

print(índicesMaisDistantes(listaRobôs))

ids = idsRobôs(listaRobôs)
indices = índicesMaisDistantes(listaRobôs)

print("Robôs mais distantes:")
print(robôsMaisDistantes(ids, indices))

# print(últimosPontosRobôs(listaRobôs))

# ============ QUESTÃO C ============ #
# c) Exiba os caminhos percorridos por todos os robôs que entraram no terreno de busca,
# ordenados crescentemente pela distância total percorrida;

# COMPREENSÃO DO PROBLEMA: deve-se calcular as distâncias percorridas por todos os robôs, adicionando-as
# em uma lista que será ordenada, imprimida na tela e então retornada

# PLANEJAMENTO:
# Criar as seguintes funções:
# - Função para ordenar lista em ordem crescente - OK
# - Função para aplicar a função da questão (a) em todos os robôs da lista de entrada - OK?
# - Ordenar essa lista de distâncias e retornar (a menos que queira a lista de tuplas original, ver isso depois) - OK?

def exibeCaminhosRobôsCrescente(listaRobôs):
    ''' Função exibeCaminhosRobôsCrescente()
    Descrição: Dada a lista de robôs, imprime o caminho de cada robô (em ordem crescente de distância)
    Escopo: Função global paramétrica
    Dados de entrada: A lista de dados sobre os robôs
    Dados de saída: Uma lista de distâncias ordenada
    '''
    ids = idsRobôs(listaRobôs)

    listaDistânciasOrdenadas = mergeSort(listaDistâncias)
    print(listaDistânciasOrdenadas)
    return listaDistânciasOrdenadas

# def distânciasTotaisRobôs(listaRobôs, listaIds):




def mergeOrdenada(l1, l2):
    ''' Função mergeOrdenada()
    Descrição: Com duas listas ordenadas de entrada, junta as duas de forma ordenada
    Escopo: Função global paramétrica
    Dados de entrada: Duas listas numéricas ordenadas
    Dados de saída: Uma lista ordenada tuplasRobôIdda a partir da junção ordenada das duas de entrada
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


def listaVítimasRobô(listaRobôs, id):
    ''' Função listaVítimasRobô
    Descrição: Retorna a lista de vítimas avistadas por um robô dado seu id
    Escopo: Função global paramétrica
    Dados de entrada: lista com informações sobre todos os robôs e o id de um robô da lista
    Dados de saída: lista com vítimas avistadas por um robô
    '''

    ids = idsRobôs(listaRobôs)
    return [tupla4(x) for x in listaRobôs if tupla1(x) == id]

def totalVítimasRobô(listaRobôs, id):
    ''' Função totalVítimasRobô
    Descrição: Retorna o total de vítimas avistadas por um robô dado seu id
    Escopo: Função global paramétrica
    Dados de entrada: lista com informações sobre todos os robôs e o id de um robô da lista
    Dados de saída: total de vítimas avistadas por um robô
    '''

    listaVítimas = listaVítimasRobô(listaRobôs, id)
    return reduce(lambda x, y: x + y, listaVítimas)


def idMaisVítimas(listaRobôs):
    ''' Função idMaisVítimas
    Descrição: Retorna os ids do robôs que avistaram o maior número de vítimas
    Escopo: Função global paramétrica
    Dados de entrada: lista com informações sobre todos os robôs
    Dados de saída: lista com ids de robôs (pode haver mais de um) que avistaram o maior número de vítimas
    '''

def totalVítimasRobôs(listaRobôs):
    print("n sei")
    # ids = idsRobôs(listaRobôs)
    # return [totalVítimasRobôs(listaRobôs, x) for x in ids]
    # nMaisVítimas = maiorLista(totalVítimasRobôsLista)


def tuplasRobôId(listaRobôs, id):
    ''' Função tuplasRobôID
    Descrição: Retorna as tuplas de um robô na lista dado seu id
    Escopo: Função global paramétrica
    Dados de entrada: lista com informações sobre todos os robôs
    Dados de saída: lista de tuplas de um robô
    '''

    if listaRobôs == []:
        return []
    elif tupla1(listaRobôs[0]) == id:
        return [listaRobôs[0]] + tuplasRobôId(listaRobôs[1:], id)
    else:
        return tuplasRobôId(listaRobôs[1:], id)

# ============ TESTES ============ #
# "Os testes propriamente ditos devem estar automatizados no arquivo de código"
# Aqui ficarão os testes do programa, inclusive os testes que estarão na versão final
# dist01 = distEuclid((0,0),(1,1))
# print(f"Distância entre (0,0 e (1,1): {dist01}")

# listaTeste = [random.randrange(1, 100) for _ in range(0, 100)]
# print(listaTeste)
# print(mergeSort(listaTeste))

# print(listaTuplaRobôID(listaRobôs, 'robo3'))

# Testes A
# pontos1 = []
# pontos2 = [(1,1)]
# pontos3 = [(1,1), (3,1)]
# pontos4 = [(1,1), (3,1), (6,1)]
# print(distânciaTotal(pontos1), distânciaTotal(pontos2), distânciaTotal(pontos3), distânciaTotal(pontos4))

# print(distânciaTotalRobô(listaRobôs, 'robo4'))

# print("\nImprimindo tuplas do robo3:")
# print(tuplasRobôId(listaRobôs, "robo3"))

# print("\nImprimindo lista de vítimas avistadas pelo robo3:")
# print(listaVítimasRobô(listaRobôs, "robo3"))
# print("\nImprimindo total de vítimas avistadas pelo robo3:")
# print(totalVítimasRobô(listaRobôs, "robo3"))

# print("\nImprimindo percurso do robo3:")
# imprimePercurso(listaRobôs, 'robo3')

print("\nImprimindo caminhos percorridos pelos robos:")
print(caminhosPercorridos(listaRobôs))

print("Últimos pontos dos robôs:")
print(últimosPontosRobôs(listaRobôs))

print("\nImprimindo distâncias totais percorridas pelos robos:")
print(distânciasTotaisRobôs(listaRobôs))

print("Distância da origem até os últimos pontos dos robôs:")
print(distOrigemÚltimoPonto(últimosPontosRobôs(listaRobôs)))

print()
print(minLista(distOrigemÚltimoPonto(últimosPontosRobôs(listaRobôs))))
