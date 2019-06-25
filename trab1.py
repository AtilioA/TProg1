# Auxílio ao resgate de vítimas por robôs em ambientes acidentados
# Autores: Atílio Antônio Dadalto
# Disciplina: Programação I, ministrada por Jordana Sarmenghi Salamon em 2019/1


# Importação de módulos
# "Ao importar funções de algum módulo, utilize a opção de importação específica"
from os import system  # Para limpar o terminal
from random import randint  # Para gerar entradas

from problemaA import distancia_total_robo
from problemaB import (caminhos_percorridos, ids_robos,
                       imprime_robos_mais_distantes,
                       indices_ids_mais_distantes)
from problemaC import (caminhos_robos_crescente, merge_sort_tupla,
                       tupla_caminhos_percorridos, distancias_totais_robos)
from problemaD import ids_mais_vitimas, total_vitimas_robo

# Compreensão do problema e planejamento da solução
# "Cada função deve ter um comentário com sua descrição, dados de entrada e saída.
# Na descrição, diga se a função é global ou local, paramétrica ou não, e por quê.
# Realizar a validação dos dados."

# ============ TESTES ============
# "Os testes propriamente ditos devem estar automatizados no arquivo de código"
# Aqui ficarão os testes do programa, inclusive os testes que estarão na versão final

# Entradas
# Exemplos oficiais de entrada
listaRobosRealOficial = [
    ('robo3', 1, (7, 7), 3), ('robo4', 2, (7, 5), 2), ('robo3', 3, (5, 4), 3),
    ('robo3', 4, (8, 1), 4), ('robo4', 5, (4, 5), 3), ('robo5', 6, (7, 7), 4),
    ('robo5', 7, (6, 4), 5), ('robo3', 8, (7, 2), 3), ('robo5', 9, (6, 4), 4)
]

listaRobosRealOficial2 = [
    ('robo1', 1, (5, 8), 4), ('robo2', 2, (5, 4), 4), ('robo3', 3, (2, 2), 1),
    ('robo1', 4, (4, 9), 4), ('robo3', 5, (1, 3), 3), ('robo4', 6, (7, 5), 3),
    ('robo5', 7, (8, 6), 1), ('robo1', 8, (3, 2), 4), ('robo2', 9, (1, 8), 4)
]

# Entradas criadas por mim
listaRobos2 = [
    ('robo28', 1, (1, 1), 3), ('robo1', 2, (9, 11), 14), ('robo2', 3, (1, 0), 1),
    ('robo28', 4, (2, 3), 4), ('robo1', 5, (4, 5), 5), ('robo28', 6, (3, 2), 2),
    ('robo32', 7, (4, 5), 2), ('robo11', 8, (11, 11), 11)
]

listaRobos3 = [
    ('roboJordana', 1, (1, 1), 3), ('roboMorgana', 2, (-3, -6), 14),
    ('roboFinalLixoDeGOT', 3, (-6, 0), -
     10), ('roboCapitãMarvelEmpoderada', 4, (1, 8), 53),
    ('roboLooana', 5, (5, 5), 4), ('roboClebson', 6, (3, 2), 2),
    ('roboTheWitcher3', 7, (19, 5), 2015), ('robo2077', 8, (16, 4), 2020),
    ('roboÍcaroCarregadoNoTrabAfkNaBase', 9,
     (0, 0), 0), ('robo2049', 10, (10, 10), 10),
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
                                randint(1, 10)))
# listaRobosAleatória = []

if __name__ == "__main__":

    # system('cls||clear')  # Limpa a tela do terminal

    print("====== TESTES ======\n")

    # Lista de robôs escolhida para testes
    listaRobosEscolhida = listaRobosRealOficial2

    ids = ids_robos(listaRobosEscolhida)
    caminhos = caminhos_percorridos(listaRobosEscolhida)
    distsTotais = distancias_totais_robos(listaRobosEscolhida)
    indices = indices_ids_mais_distantes(listaRobosEscolhida)

    print(f"Lista de robôs recebida pela CP:\n{listaRobosEscolhida}")
    print(f"Robôs:\n{ids}")

    print(f"\nQuantidade de robôs: {len(ids)}")
    print(f"Quantidade de ocorrências: {len(listaRobosEscolhida)}\n")

    print("- Problema A:")
    roboEscolhido = 'robo3'
    # roboEscolhido = input("Informe um id para calcular distância percorrida: ")

    distRoboEscolhido = distancia_total_robo(
        listaRobosEscolhida, roboEscolhido)
    if distRoboEscolhido is not None:
        print(f"Distância total de {roboEscolhido}: {distRoboEscolhido}.")
    else:
        pass
    print("\n")

    print("- Problema B:")
    imprime_robos_mais_distantes(listaRobosEscolhida)
    print("\n")

    print("- Problema C:")
    listaDistanciasOrdenadas = caminhos_robos_crescente(listaRobosEscolhida)
    print(
        f"Imprimindo tuplas com distâncias em ordem crescente:\n{listaDistanciasOrdenadas}")
    print("\n")

    print("- Problema D:")
    listaIDsMaisVitimas = ids_mais_vitimas(listaRobosEscolhida)
    if listaIDsMaisVitimas is not None:
        print(f"Robôs que avistaram mais vítimas: {listaIDsMaisVitimas},",
              f"avistando {total_vitimas_robo(listaRobosEscolhida, listaIDsMaisVitimas[0])} vítimas.")
    else:
        print("Lista vazia não possui robôs.\n\n")
