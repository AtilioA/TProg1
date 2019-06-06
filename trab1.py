# Auxílio ao resgate de vítimas por robôs em ambientes acidentados
# Autores: Atílio Antônio Dadalto
# Disciplina: Programação I, 2019/1

# Cada função deve ter um comentário com sua descrição, dados de entrada e saída.
# Na descrição, diga se a função é global ou local, paramétrica ou não, e por quê.
# Realizar a validação dos dados.

# Considere que todos os robôs partem do mesmo ponto inicial: (0,0).
# As informações enviadas pelos robôs de resgate contêm os seguintes registros:
# a identificação do robô,
# o instante em que o robô passou em um determinado ponto da área afetada,
# o ponto no plano cartesiano referente ao incidente registrado, e
# o número de vítimas presentes na área de visibilidade do robô.

# Considerando uma lista com tais informações como os dados de entrada disponíveis, faça um programa em Python que responda às seguintes solicitações:
# Compreensão do problema e planejamento da solução:
# a) Calcular a distância percorrida por um determinado robô ao longo do processo de resgate das vítimas. Considere que a distância total percorrida deve ser calculada como a soma de todas as distâncias entre os pontos de passagem do robô;
# - Função de distância no plano cartesiano
# - Somar distâncias entre todos os pontos passados por um robô (pela sua identificação) na lista dada como entrada e retornar

# b) Determine qual dos robôs apresenta o seu último ponto de passagem no terreno de busca que possui a maior distância em relação à origem. Exiba o caminho percorrido pelo robô e o tempo total do percurso;
# - Extrair, da lista de entrada, o último ponto de passagem de todos os robôs
# - Determinar qual robô possui ponto mais longe da origem
# - Imprimir caminho percorrido pelo robô, determinar tempo do percurso

# c) Exiba os caminhos percorridos por todos os robôs que entraram no terreno de busca, ordenados crescentemente pela distância total percorrida;
# - Função de ordenar em ordem crescente
# - Somar distâncias de todos os robôs com função da (a)
# - Ordenar essa lista e retornar

# d) Forneça a identidade do(s) robô(s) que conseguiu(ram) informar o maior número de vítimas (considerando que não há duplicação de identificação de vítima por um mesmo robô).
def idMaisVitimas()
