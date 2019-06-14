# Módulo com funções auxiliares
# Autores: Atílio Antônio Dadalto
# Disciplina: Programação I, 2019/1, ministrada por Jordana Sarmenghi Salamon em 2019/

from functools import reduce


def maxLista(lista):
    return reduce(lambda a, b: a if (a > b) else b, lista)


def minLista(lista):
    return reduce(lambda a, b: a if (a < b) else b, lista)


def tupla1(tupla4):
    ''' Função: tupla1()
    Descrição: retorna o primeiro elemento de uma tupla de 4 elementos
    Escopo: função global paramétrica
    Dados de entrada: tupla de 4 elementos
    Dados de saída: primeiro elemento da tupla
    '''

    return tupla4[0]


def tupla2(tupla4):
    ''' Função: tupla2()
    Descrição: retorna o segundo elemento de uma tupla de 4 elementos
    Escopo: função global paramétrica
    Dados de entrada: tupla de 4 elementos
    Dados de saída: segundo elemento da tupla
    '''

    return tupla4[1]


def tupla3(tupla4):
    ''' Função: tupla3()
    Descrição: retorna o terceiro elemento de uma tupla de 4 elementos
    Escopo: função global paramétrica
    Dados de entrada: tupla de 4 elementos
    Dados de saída: terceiro elemento da tupla
    '''

    return tupla4[2]


def tupla4(tupla4):
    ''' Função: tupla4()
    Descrição: retorna o quarto (último) elemento de uma tupla de 4 elementos
    Escopo: função global paramétrica
    Dados de entrada: tupla de 4 elementos
    Dados de saída: quarto (último) elemento da tupla
    '''

    return tupla4[-1]
