# Módulo com funções auxiliares
# Autores: Atílio Antônio Dadalto
# Disciplina: Programação I, ministrada por Jordana Sarmenghi Salamon em 2019/1

from functools import reduce


def max_lista(lista):
    """ Retorna o maior elemento de uma lista (assumida como numérica)
    Escopo: Função global paramétrica
    Dados de entrada: Lista (assumida como numérica)
    Dados de saída: Maior elemento da lista
    """

    try:
        if len(lista) == 0:
            print("Lista vazia não possui máximo")
            raise Exception()
        else:
            return reduce(lambda a, b: a if (a > b) else b, lista)
    except:
        pass


def soma_lista(lista):
    """ Soma os elementos de uma lista numérica
    Escopo: Função global paramétrica
    Dados de entrada: Lista numérica
    Dados de saída: Valor numérico
    """

    try:
        if len(lista) == 0:
            print("Lista vazia não possui valor de soma")
            raise Exception()
        else:
            return reduce(lambda x, y: x + y, lista)
    except:
        pass


def pega_id(tuplaRobos):
    """ Retorna o primeiro elemento da tupla de um robô,
    isto é, o id do robô
    Escopo: função global paramétrica
    Dados de entrada: tupla de um robô
    Dados de saída: primeiro elemento da tupla de um robô
    """

    try:
        if len(tuplaRobos) < 2:  # Não funciona com < 4 (descobrir por quê)
            print("Tupla não possui elementos o suficiente.")
            raise Exception()
        else:
            return tuplaRobos[0]
    except:
        pass


def pega_instante(tuplaRobos):
    """ Retorna o segundo elemento da tupla de um robô,
    isto é, o instante da ocorrência
    Escopo: função global paramétrica
    Dados de entrada: tupla de um robô
    Dados de saída: segundo elemento da tupla de um robô
    """

    try:
        if len(tuplaRobos) < 2:  # Não funciona com < 4 (descobrir por quê)
            print("Tupla não possui elementos o suficiente.")
            raise Exception()
        else:
            return tuplaRobos[1]
    except:
        pass


def pega_local(tuplaRobos):
    """ Retorna o terceiro elemento da tupla de um robô,
    isto é, a localização do robô na ocorrência
    Escopo: função global paramétrica
    Dados de entrada: tupla de um robô
    Dados de saída: terceiro elemento da tupla de um robô
    """

    try:
        if len(tuplaRobos) < 2:  # Não funciona com < 4 (descobrir por quê)
            print("Tupla não possui elementos o suficiente.")
            raise Exception()
        else:
            return tuplaRobos[2]
    except:
        pass


def pega_vitimas(tuplaRobos):
    """ Retorna o quarto (último) elemento da tupla de um robô,
    isto é, o número de vítimas avistadas
    Escopo: função global paramétrica
    Dados de entrada: tupla de um robô
    Dados de saída: quarto (último) elemento da tupla de um robô
    """

    try:
        if len(tuplaRobos) < 2:  # Não funciona com < 4 (descobrir por quê)
            print("Tupla não possui elementos o suficiente.")
            raise Exception()
        else:
            return tuplaRobos[-1]
    except:
        pass


def tupla1(tupla2):
    """ Retorna o primeiro elemento de uma tupla de 2 elementos
    Escopo: função global paramétrica
    Dados de entrada: tupla de 2 elementos
    Dados de saída: primeiro elemento da tupla
    """

    try:
        if len(tupla2) == 0:
            print("Tupla vazia não possui elementos.")
            raise Exception()
        else:
            return tupla2[0]
    except:
        pass


def tupla2(tupla2):
    """ Retorna o segundo (último) elemento de uma tupla de 2 elementos
    Escopo: função global paramétrica
    Dados de entrada: tupla de 2 elementos
    Dados de saída: segundo (último) elemento da tupla
    """

    try:
        if len(tupla2) < 2:
            print("Tupla não possui elementos o suficiente.")
            raise Exception()
        else:
            return tupla2[-1]
    except:
        pass


def ultimo(subscriptable):
    """ Retorna o último elemento de uma lista, tupla, dicionário ou string
    Escopo: Função global paramétrica
    Dados de entrada: Lista, tupla, dicionário ou string
    Dados de saída: Último elemento da estrutura
    """

    try:
        if len(subscriptable) == 0:
            print("Não possui elementos o suficiente.")
            raise Exception()
        else:
            return subscriptable[-1]
    except:
        pass
