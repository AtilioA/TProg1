# Módulo com funções auxiliares
# Autores: Atílio Antônio Dadalto e Ícaro Madalena do Nascimento
# Disciplina: Programação I, ministrada por Jordana Sarmenghi Salamon em 2019/1

from functools import reduce


def max_lista(lista):
    """ Retorna o maior elemento de uma lista (assumida como numérica)
    Escopo: Função global paramétrica
    Dados de entrada: Lista (assumida como numérica)
    Dados de saída: Maior elemento da lista
    """

    def maior(a, b):
        """ Retorna o maior dentre dois números
        Escopo: Função local paramétrica
        Dados de entrada: Dois números
        Dados de saída: O maior número
        """
        if a > b:
            return a
        else:
            return b

    try:
        if not lista:  # ValueError
            print("Lista vazia não possui máximo")
        else:  # Reduce para fazer comparações e reduzir lista a um número (o retorno de "maior" não é booleano)
            return reduce(maior, lista)
    except ValueError:
        pass


def soma_lista(lista):
    """ Soma os elementos de uma lista numérica
    Escopo: Função global paramétrica
    Dados de entrada: Lista numérica
    Dados de saída: Valor numérico
    """

    try:
        if not lista:  # ValueError
            print("Lista vazia não possui valor de soma")
        else:
            return reduce(lambda x, y: x + y, lista)
    except ValueError:
        pass


def pega_id(tuplaRobos):
    """ Retorna o primeiro elemento da tupla de um robô,
    isto é, o id do robô
    Escopo: função global paramétrica
    Dados de entrada: tupla de um robô
    Dados de saída: primeiro elemento da tupla de um robô
    """

    try:
        if len(tuplaRobos) != 4:  # ValueError
            print("Tupla de robôs malformada.")
        else:
            return tuplaRobos[0]
    except ValueError:
        pass


def pega_instante(tuplaRobos):
    """ Retorna o segundo elemento da tupla de um robô,
    isto é, o instante da ocorrência
    Escopo: função global paramétrica
    Dados de entrada: tupla de um robô
    Dados de saída: segundo elemento da tupla de um robô
    """

    try:
        if len(tuplaRobos) != 4:  # ValueError
            print("Tupla de robôs malformada.")
        else:
            return tuplaRobos[1]
    except ValueError:
        pass


def pega_local(tuplaRobos):
    """ Retorna o terceiro elemento da tupla de um robô,
    isto é, a localização do robô na ocorrência
    Escopo: função global paramétrica
    Dados de entrada: tupla de um robô
    Dados de saída: terceiro elemento da tupla de um robô
    """

    try:
        if len(tuplaRobos) != 4:  # ValueError
            print("Tupla de robôs malformada.")
        else:
            return tuplaRobos[2]
    except ValueError:
        pass


def pega_vitimas(tuplaRobos):
    """ Retorna o quarto elemento da tupla de um robô,
    isto é, o número de vítimas avistadas
    Escopo: função global paramétrica
    Dados de entrada: tupla de um robô
    Dados de saída: quarto elemento da tupla de um robô
    """

    try:
        if len(tuplaRobos) != 4:  # ValueError
            print("Tupla de robôs malformada.")
        else:
            return tuplaRobos[3]
    except ValueError:
        pass


def tupla1(tupla2):
    """ Retorna o primeiro elemento de uma tupla
    Escopo: função global paramétrica
    Dados de entrada: tupla não vazia
    Dados de saída: primeiro elemento da tupla
    """

    try:
        if not tupla2:  # ValueError
            print("Tupla vazia não possui elementos.")
        else:
            return tupla2[0]
    except ValueError:
        pass


def tupla2(tupla2):
    """ Retorna o segundo elemento de uma tupla
    Escopo: função global paramétrica
    Dados de entrada: tupla de pelo menos 2 elementos
    Dados de saída: segundo elemento da tupla
    """

    try:
        if len(tupla2) < 2:  # ValueError
            print("Tupla não possui elementos o suficiente.")
        else:
            return tupla2[1]
    except ValueError:
        pass


def ultimo(subscriptable):
    """ Retorna elemento de uma lista, tupla, dicionário ou string
    Escopo: Função global paramétrica
    Dados de entrada: Lista, tupla, dicionário ou string
    Dados de saídaelemento da estrutura
    """

    try:
        if not subscriptable:  # ValueError
            print("Objeto não possui elementos o suficiente.")
        else:
            return subscriptable[-1]
    except ValueError:
        pass
