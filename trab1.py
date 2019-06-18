# Auxílio ao resgate de vítimas por robôs em ambientes acidentados
# Autores: Atílio Antônio Dadalto
# Disciplina: Programação I, ministrada por Jordana Sarmenghi Salamon em 2019/1


# Importação de módulos
# "(Ao importar funções de algum módulo, utilize a opção de importação específica)"
from problemaA import *
from problemaB import *
from problemaC import *
from problemaD import *

from random import randint

# Compreensão do problema e planejamento da solução
# "Cada função deve ter um comentário com sua descrição, dados de entrada e saída.
# Na descrição, diga se a função é global ou local, paramétrica ou não, e por quê.
# Realizar a validação dos dados."

# ============ TESTES ============
# "Os testes propriamente ditos devem estar automatizados no arquivo de código"
# Aqui ficarão os testes do programa, inclusive os testes que estarão na versão final

# Entradas
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
    ('roboJordana', 1, (1, 1), 3), ('roboMorgana', 2, (-3, -6), 14),
    ('roboFinalLixoDeGOT', 3, (-6, 0), -10), ('roboCapitãMarvelEmpoderada', 4, (1, 8), 53),
    ('roboLooana', 5, (5, 5), 4), ('roboClebson', 6, (3, 2), 2),
    ('roboTheWitcher3', 7, (19, 5), 2015), ('robo2077', 8, (16, 4), 2020),
    ('roboÍcaroCarregadoNoTrabAfkNaBase', 9, (0, 0), 0), ('robo2049', 10, (10, 10), 10),
    ('roboRyanGoslingLiteralDeus', 11, (12, 11), 3), ('roboJordana', 12, (1, 1), 3),
    ('roboCapitãMarvelEmpoderada', 13, (2, 6), 5), ('roboMorgana', 14, (2, 2), 2),
    ('roboRyanGoslingLiteralDeus', 15, (6, 6), 6), ('roboClebson', 16, (1, 5), 7),
    ('roboÍcaroCarregadoNoTrabAfkNaBase', 17, (0, 0), 0)
]

listaRobos4 = [
    ('robo2', 1, (7, 7), 3), ('robo2', 2, (7, 5), 2), ('robo3', 3, (5, 4), 3),
    ('robo4', 4, (8, 1), 4), ('robo3', 5, (4, 5), 3), ('robo2', 6, (7, 7), 4),
    ('robo4', 7, (6, 4), 5), ('robo3', 8, (7, 2), 6), ('robo4', 9, (6, 4), 4),
    ('robo4', 10, (8, 1), 4), ('robo2', 11, (4, 5), 2), ('robo2', 12, (7, 7), 0),
    ('robo3', 13, (6, 4), 5), ('robo4', 14, (7, 2), 1), ('robo5', 15, (6, 4), 8),
    ('robo4', 16, (0, 0), 0), ('robo2', 17, (4, 5), 4), ('robo2', 18, (7, 7), 1),
    ('robo2', 19, (1, 4), 2), ('robo3', 20, (1, 1), 8), ('robo5', 21, (4, 2), 5),
]

# Entrada gerada aleatoriamente
listaRobosAleatória = []
for i in range(1, randint(1, 50)):
    listaRobosAleatória.append((f'robo{randint(0, 10)}',
                                i,
                                (randint(1, 15), randint(1, 15)),
                                randint(0, 10)))
# listaRobosAleatória = []


print("\n\n====== TESTES ======\n\n")

listaRobosEscolhida = listaRobos3

ids = ids_robos(listaRobosEscolhida)
indices = indices_ids_mais_distantes(listaRobosEscolhida)

print(f"Lista de robôs recebida pela CP:\n{listaRobosEscolhida}")
print(f"Robôs:\n{ids}")

print(f"\nQuantidade de robôs: {len(ids)}")
print(f"Quantidade de ocorrências: {len(listaRobosEscolhida)}\n")


print("Problema A:")
# idEntrada = input("Informe um id para calcular distância percorrida: ")
# idEntrada = "robo0"

roboEscolhido = 'roboÍcaroCarregadoNoTrabAfkNaBase'
distRoboEscolhido = distancia_totalRobo(listaRobosEscolhida, roboEscolhido)
if distRoboEscolhido is not None:
    print(f"Distância total de {roboEscolhido}: {distRoboEscolhido}.")
else:
    pass
print("\n")

print("Problema B:")
imprime_robos_mais_distantes(listaRobosEscolhida)
print("\n")

print("Problema C:")
listaDistanciasOrdenadas = caminhos_robos_crescente(listaRobosEscolhida)
print(f"Imprimindo distâncias em ordem crescente:\n{listaDistanciasOrdenadas}")
print("\n")

print("Problema D:")
listaIDsMaisVitimas = ids_mais_vitimas(listaRobosEscolhida)
if listaIDsMaisVitimas is not None:
    print(f"Robôs que avistaram mais vítimas: {listaIDsMaisVitimas},",
          f"avistando {total_vitimas_robo(listaRobosEscolhida, listaIDsMaisVitimas[0])} vítimas.")
else:
    print("Lista vazia não possui robôs.")
