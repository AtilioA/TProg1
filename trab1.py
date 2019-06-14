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
# listaRobos = [(id1, instante1, ponto1, nVítimas1), (id2, instante2, ponto2, nVítimas2)]

# Compreensão do problema e planejamento da solução

# "(Ao importar funções de algum módulo, utilize a opção de importação específica)"
from problemaA import *
from problemaB import *
from problemaC import *
from problemaD import *
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

listaRobos = [('robo3', 1, (7, 7), 3), ('robo4', 2, (7, 5), 2), ('robo3', 3, (5, 4), 3), ('robo3', 4, (8, 1), 4), ('robo4', 5, (4, 5), 3), ('robo5', 6, (7, 7), 4), ('robo5', 7, (6, 4), 5), ('robo3', 8, (7, 2), 3), ('robo5', 9, (6, 4), 4)]


# ============ TESTES ============ #
# "Os testes propriamente ditos devem estar automatizados no arquivo de código"
# Aqui ficarão os testes do programa, inclusive os testes que estarão na versão final
# dist01 = distEuclid((0,0),(1,1))
# print(f"Distância entre (0,0 e (1,1): {dist01}")

# listaTeste = [random.randrange(1, 100) for _ in range(0, 100)]
# print(listaTeste)
# print(mergeSort(listaTeste))

# print(listaTuplaRoboID(listaRobos, 'robo3'))

# Testes A
# pontos1 = []
# pontos2 = [(1,1)]
# pontos3 = [(1,1), (3,1)]
# pontos4 = [(1,1), (3,1), (6,1)]
# print(distanciaTotal(pontos1), distanciaTotal(pontos2), distanciaTotal(pontos3), distanciaTotal(pontos4))

# print(distanciaTotalRobo(listaRobos, 'robo4'))

# print("\nImprimindo tuplas do robo3:")
# print(tuplasRoboId(listaRobos, "robo3"))

# print("\nImprimindo lista de vítimas avistadas pelo robo3:")
# print(listaVitimasRobo(listaRobos, "robo3"))
# print("\nImprimindo total de vítimas avistadas pelo robo3:")
# print(totalVítimasRobô(listaRobos, "robo3"))

# print("\nImprimindo percurso do robo3:")
# imprimePercurso(listaRobos, 'robo3')


exec(open('./testes.py').read())
