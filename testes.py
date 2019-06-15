from problemaA import *
from problemaB import *
from problemaC import *
from problemaD import *


# Entradas
listaRobos = [('robo3', 1, (7, 7), 3), ('robo4', 2, (7, 5), 2), ('robo3', 3, (5, 4), 3), ('robo3', 4, (8, 1), 4), ('robo4', 5, (4, 5), 3), ('robo5', 6, (7, 7), 4), ('robo5', 7, (6, 4), 5), ('robo3', 8, (7, 2), 3), ('robo5', 9, (6, 4), 4)]

listaRobos2 = [('robo28', 1, (1, 1), 3), ('robo1', 2, (9, 11), 14), ('robo2', 3, (1, 0), 1), ('robo28', 4, (2, 3), 4), ('robo1', 5, (4, 5), 5), ('robo28', 6, (3, 2), 2), ('robo32', 7, (4, 5), 2), ('robo11', 8, (1, 3), 11)]

listaRobos3 = [('robo666', 1, (1, 1), 3), ('robo0', 2, (-3, -6), 14), ('roboJordana', 3, (-6, 0), 100), ('robo28', 4, (5, 5), 4), ('roboJordana', 5, (10, 10), 1), ('robo33', 6, (5, 5), 4), ('robo17', 7, (3, 2), 2), ('robo38', 8, (4, 5), 2), ('robo2077', 9, (16, 4), 2020), ('roboTheWitcher3', 15, (19, 5), 2015), ('roboTheWitcher4', 10, (5, 19), 2015)]

print("\n=== TESTES ===\n\n")


ids = idsRobos(listaRobos3)
indices = indicesMaisDistantes(listaRobos3)

# print(f"Robôs: {ids}\n")
# print(f"Índices dos robôs mais distantes: {indices}")

# print("Robôs mais distantes:")
# print(robosMaisDistantes(ids, indices))


# print("\nImprimindo caminhos percorridos pelos robos:")
# print(caminhosPercorridos(listaRobos3))

# print("Últimos pontos dos robôs:")
# print(ultimosPontosRobos(listaRobos3))

# print("\nImprimindo distâncias totais percorridas pelos robos:")
# print(distanciasTotaisRobos(listaRobos3))
# caminhosRobosCrescente(listaRobos3)
# print("Distância da origem até os últimos pontos dos robôs:")
# print(distOrigemUltimoPonto(ultimosPontosRobos(listaRobos3)))

print("Problema A:")
# idEntrada = input("Informe um id para calcular distância percorrida: ")
idEntrada = "robo0"
print(f"Distância total de {idEntrada}: {distanciaTotalRobo(listaRobos, idEntrada)}.")
print(f"Distância total de {'robo2077'}: {distanciaTotalRobo(listaRobos, 'robo2077')}.")
print(f"Distância total de {'roboTheWitcher3'}: {distanciaTotalRobo(listaRobos, 'roboTheWitcher3')}.")
print(f"Distância total de {'robo10'}: {distanciaTotalRobo(listaRobos, 'robo10')}.")
print(f"Distância total de {'robo3'}: {distanciaTotalRobo(listaRobos, 'robo3')}.")
print("\n")

print("Problema B:")
imprimeRobosMaisDistantes(listaRobos)
print("\n")

print("Problema C:")
listaDistanciasOrdenadas = caminhosRobosCrescente(listaRobos)
print(f"Imprimindo distâncias em ordem crescente:\n{listaDistanciasOrdenadas}")
print("\n")

print("Problema D:")
# print(listaVitimasRobo(listaRobos, 'roboJordana'))
# print(totalVitimasRobo(listaRobos, 'roboJordana'))
# print(totalVitimasRobos(listaRobos))
listaIdsMaisVitimas = idsMaisVitimas(listaRobos)
print(f"Robôs que avistaram mais vítimas: {listaIdsMaisVitimas},",\
        f"avistando {totalVitimasRobo(listaRobos, listaIdsMaisVitimas[0])} vítimas.")
