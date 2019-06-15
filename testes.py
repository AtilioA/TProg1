from problemaA import *
from problemaB import *
from problemaC import *
from problemaD import *

from random import randint

# Entradas
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

listaRobos4 = [
    ('robo2', 1, (7, 7), 3), ('robo2', 2, (7, 5), 2), ('robo3', 3, (5, 4), 3),
    ('robo4', 4, (8, 1), 4), ('robo3', 5, (4, 5), 3), ('robo2', 6, (7, 7), 4),
    ('robo4', 7, (6, 4), 5), ('robo3', 8, (7, 2), 6), ('robo4', 9, (6, 4), 4),
    ('robo4', 10, (8, 1), 4), ('robo2', 11, (4, 5), 2), ('robo2', 12, (7, 7), 0),
    ('robo3', 13, (6, 4), 5), ('robo4', 14, (7, 2), 1), ('robo5', 15, (6, 4), 8),
    ('robo4', 16, (0, 0), 0), ('robo2', 17, (4, 5), 4), ('robo2', 18, (7, 7), 1),
    ('robo2', 19, (1, 4), 2), ('robo3', 20, (1, 1), 8), ('robo5', 21, (4, 2), 5),
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
listaRobosAleatória = [
    (f'robo{randint(0, 10)}', 1, (randint(1, 15), randint(1, 15)), randint(0, 10)),
    (f'robo{randint(0, 10)}', 2, (randint(0, 15), randint(0, 15)), randint(0, 10)),
    (f'robo{randint(0, 10)}', 3, (randint(0, 15), randint(0, 15)), randint(0, 10)),
    (f'robo{randint(0, 10)}', 4, (randint(0, 15), randint(0, 15)), randint(0, 10)),
    (f'robo{randint(0, 10)}', 5, (randint(0, 15), randint(0, 15)), randint(0, 10)),
    (f'robo{randint(0, 10)}', 6, (randint(0, 15), randint(0, 15)), randint(0, 10)),
    (f'robo{randint(0, 10)}', 7, (randint(0, 15), randint(0, 15)), randint(0, 10)),
    (f'robo{randint(0, 10)}', 8, (randint(0, 15), randint(0, 15)), randint(0, 10)),
    (f'robo{randint(0, 10)}', 9, (randint(0, 15), randint(0, 15)), randint(0, 10)),
    (f'robo{randint(0, 10)}', 10, (randint(0, 15), randint(0, 15)), randint(0, 10)),
    (f'robo{randint(0, 10)}', 11, (randint(0, 15), randint(0, 15)), randint(0, 10)),
    (f'robo{randint(0, 10)}', 12, (randint(0, 15), randint(0, 15)), randint(0, 10)),
    (f'robo{randint(0, 10)}', 13, (randint(0, 15), randint(0, 15)), randint(0, 10)),
    (f'robo{randint(0, 10)}', 14, (randint(0, 15), randint(0, 15)), randint(0, 10)),
    (f'robo{randint(0, 10)}', 15, (randint(0, 15), randint(0, 15)), randint(0, 10)),
    (f'robo{randint(0, 10)}', 16, (randint(0, 15), randint(0, 15)), randint(0, 10)),
    (f'robo{randint(0, 10)}', 17, (randint(0, 15), randint(0, 15)), randint(0, 10)),
    (f'robo{randint(0, 10)}', 18, (randint(0, 15), randint(0, 15)), randint(0, 10)),
    (f'robo{randint(0, 10)}', 19, (randint(0, 15), randint(0, 15)), randint(0, 10)),
    (f'robo{randint(0, 10)}', 20, (randint(0, 15), randint(0, 15)), randint(0, 10)),
    (f'robo{randint(0, 10)}', 21, (randint(0, 15), randint(0, 15)), randint(0, 10)),
    (f'robo{randint(0, 10)}', 22, (randint(0, 15), randint(0, 15)), randint(0, 10)),
    (f'robo{randint(0, 10)}', 23, (randint(0, 15), randint(0, 15)), randint(0, 10)),
    (f'robo{randint(0, 10)}', 24, (randint(0, 15), randint(0, 15)), randint(0, 10)),
    (f'robo{randint(0, 10)}', 25, (randint(0, 15), randint(0, 15)), randint(0, 10)),
]


print("\n\n====== TESTES ======\n\n")


ids = ids_robos(listaRobos3)
indices = indices_ids_mais_Distantes(listaRobos3)

# print(f"Robôs: {ids}\n")
# print(f"Índices dos robôs mais distantes: {indices}")

# print("Robôs mais distantes:")
# print(robos_mais_distantes(ids, indices))


# print("\nImprimindo caminhos percorridos pelos robos:")
# print(caminhos_percorridos(listaRobos3))

# print("Últimos pontos dos robôs:")
# print(ultimos_pontos_robos(listaRobos3))

# print("\nImprimindo distâncias totais percorridas pelos robos:")
# print(distancias_totais_robos(listaRobos3))
# caminhos_robos_crescente(listaRobos3)
# print("Distância da origem até os últimos pontos dos robôs:")
# print(dist_origem_ultimo_ponto(ultimos_pontos_robos(listaRobos3)))

print(listaRobosAleatória)

print("Problema A:")
# idEntrada = input("Informe um id para calcular distância percorrida: ")
# idEntrada = "robo0"
# print(f"Distância total de {idEntrada}: {distancia_totalRobo(listaRobosAleatória, idEntrada)}.")
# print(f"Distância total de {'robo2077'}: {distancia_totalRobo(listaRobosAleatória, 'robo2077')}.")
# print(f"Distância total de {'roboTheWitcher3'}: {distancia_totalRobo(listaRobosAleatória, 'roboTheWitcher3')}.")
# print(f"Distância total de {'robo10'}: {distancia_totalRobo(listaRobosAleatória, 'robo10')}.")
print(f"Distância total de {'robo3'}: {distancia_totalRobo(listaRobosAleatória, 'robo3')}.")
print("\n")

print("Problema B:")
imprime_robos_mais_distantes(listaRobosAleatória)
print("\n")

print("Problema C:")
listaDistanciasOrdenadas = caminhos_robos_crescente(listaRobosAleatória)
print(f"Imprimindo distâncias em ordem crescente:\n{listaDistanciasOrdenadas}")
print("\n")

print("Problema D:")
# print(lista_vitimas_robo(listaRobosAleatória, 'roboJordana'))
# print(total_vitimas_robo(listaRobosAleatória, 'roboJordana'))
# print(total_vitimas_robos(listaRobosAleatória))
listaids_mais_vitimas = ids_mais_vitimas(listaRobosAleatória)
print(f"Robôs que avistaram mais vítimas: {listaids_mais_vitimas},",
      f"avistando {total_vitimas_robo(listaRobosAleatória, listaids_mais_vitimas[0])} vítimas.")


ultimos_pontos_robos(listaRobos)
