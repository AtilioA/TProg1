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

# Exemplo oficial de entrada
listaRobos = [
    ('robo3', 1, (7, 7), 3), ('robo4', 2, (7, 5), 2), ('robo3', 3, (5, 4), 3),
    ('robo3', 4, (8, 1), 4), ('robo4', 5, (4, 5), 3), ('robo5', 6, (7, 7), 4),
    ('robo5', 7, (6, 4), 5), ('robo3', 8, (7, 2), 3), ('robo5', 9, (6, 4), 4)
]

# Entradas criadas por mim
listaRobos2 = [
    ('robo28', 1, (1, 1), 3), ('robo1', 2, (9, 11), 14), ('robo2', 3, (1, 0), 1),
    ('robo28', 4, (2, 3), 4), ('robo1', 5, (4, 5), 5), ('robo28', 6, (3, 2), 2),
    ('robo32', 7, (4, 5), 2), ('robo11', 8, (11, 11), 11)
]

listaRobos3 = [
    ('robo666', 1, (1, 1), 3), ('robo0', 2, (-3, -6), 14), ('robo2', 3, (-6, 0), 100),
    ('robo33', 4, (5, 5), 4), ('robo33', 5, (5, 5), 4), ('robo17', 6, (3, 2), 2),
    ('robo38', 7, (4, 5), 2), ('robo2077', 8, (16, 4), 2020)
]

# Importação de módulos
# "(Ao importar funções de algum módulo, utilize a opção de importação específica)"
from problemaA import *
from problemaB import *
from problemaC import *
from problemaD import *

from roboAux import *
from math import *
from functools import reduce


# Compreensão do problema e planejamento da solução
# "Cada função deve ter um comentário com sua descrição, dados de entrada e saída.
# Na descrição, diga se a função é global ou local, paramétrica ou não, e por quê.
# Realizar a validação dos dados."

# Vamos comentar as funções assim:
def template(entradas):
    """ o que a função faz
    Escopo: escopo da função (global/local, paramétrica/constante)
    Dados de entrada: x, y válidos, etc
    Dados de saída: z, w, l lista numérica, b valor booleano, etc
    """

    # Resto da função. A validação ocorre aqui, com try, Exception() e etc

# ============ TESTES ============ #
# "Os testes propriamente ditos devem estar automatizados no arquivo de código"
# Aqui ficarão os testes do programa, inclusive os testes que estarão na versão final


import subprocess
subprocess.call(["python", "testes.py"])
