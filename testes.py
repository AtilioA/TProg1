print("\n\n=== TESTES ===\n\n")

print("indices dos robôs mais distantes:")

print(indicesMaisDistantes(listaRobos))

ids = idsRobos(listaRobos)
indices = indicesMaisDistantes(listaRobos)

print("\nRobôs mais distantes:")
print(robosMaisDistantes(ids, indices))

print("\nImprimindo caminhos percorridos pelos robos:")
print(caminhosPercorridos(listaRobos))

print("Últimos pontos dos robôs:")
print(ultimosPontosRobos(listaRobos))

print("\nImprimindo distâncias totais percorridas pelos robos:")
print(distanciasTotaisRobos(listaRobos))

print("\nDistância da origem até os últimos pontos dos robôs:")
print(distOrigemUltimoPonto(ultimosPontosRobos(listaRobos)))
