# Script para testes
# Autores: Atílio Antônio Dadalto
# Disciplina: Programação I, ministrada por Jordana Sarmenghi Salamon em 2019/1


from problemaA import *
from problemaB import *
from problemaC import *
from problemaD import *

from random import *

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
listaRobosAleatória = []
for i in range(1, randint(1, 50)):
    listaRobosAleatória.append((f'robo{randint(0, 10)}',
                                i,
                                (randint(1, 15), randint(1, 15)),
                                randint(0, 10)))

print("\n\n====== TESTES ======\n\n")

ids = ids_robos(listaRobosAleatória)
indices = indices_ids_mais_distantes(listaRobosAleatória)

print(f"Lista de robôs recebida pela CP:\n{listaRobosAleatória}")
print(f"Robôs:\n{ids}")

print(f"\nQuantidade de robôs: {len(ids)}")
print(f"Quantidade de ocorrências: {len(listaRobosAleatória)}\n")


print("Problema A:")
# idEntrada = input("Informe um id para calcular distância percorrida: ")
# idEntrada = "robo0"

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
listaIDsMaisVitimas = ids_mais_vitimas(listaRobosAleatória)
if listaIDsMaisVitimas is not None:
    print(f"Robôs que avistaram mais vítimas: {listaIDsMaisVitimas},",
          f"avistando {total_vitimas_robo(listaRobosAleatória, listaIDsMaisVitimas[0])} vítimas.")
else:
    print("Lista vazia não possui robôs")

# Testes com entrada vazia
# print("Problema A:")

# print(f"Distância total de {'robo3'}: {distancia_totalRobo([], 'robo3')}.")
# print("\n")

# print("Problema B:")
# imprime_robos_mais_distantes([])
# print("\n")

# print("Problema C:")
# listaDistanciasOrdenadas = caminhos_robos_crescente([])
# print(f"Imprimindo distâncias em ordem crescente:\n{listaDistanciasOrdenadas}")
# print("\n")

# print("Problema D:")

# listaIDsMaisVitimas = ids_mais_vitimas([])
# if listaIDsMaisVitimas != None:
#     print(f"Robôs que avistaram mais vítimas: {listaIDsMaisVitimas},",
#           f"avistando {total_vitimas_robo([], listaIDsMaisVitimas[0])} vítimas.")
# else:
#     print("Lista vazia não possui robôs")
