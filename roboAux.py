# Módulo com funções auxiliares
# Autores: Atílio Antônio Dadalto
# Disciplina: Programação I, 2019/1, ministrada por Jordana Sarmenghi Salamon em 2019/1

from functools import reduce

def maxLista(lista):
    ''' Função: maxLista()
    Descrição: Retorna o maior elemento de uma lista (assumida como numérica)
    Escopo: Função global paramétrica
    Dados de entrada: Lista (assumida como numérica)
    Dados de saída: Maior elemento da lista
    '''

    try:
        if len(lista) == 0:
            print("Lista vazia não possui máximo")
            raise Exception()
        else:
            return reduce(lambda a, b: a if (a > b) else b, lista)
    except:
        pass

def pegaID(tuplaRobos):
    ''' Função: pegaID()
    Descrição: retorna o primeiro elemento da tupla de um robô,
    isto é, o id do robô
    Escopo: função global paramétrica
    Dados de entrada: tupla de um robô
    Dados de saída: primeiro elemento da tupla de um robô
    '''

    try:
        if len(tuplaRobos) < 2: # Não funciona com < 4 (descobrir por quê)
            print("Tupla não possui elementos o suficiente.")
            raise Exception()
        else:
            return tuplaRobos[0]
    except:
        pass


def pegaInstante(tuplaRobos):
    ''' Função: pegaInstante()
    Descrição: retorna o segundo elemento da tupla de um robô,
    isto é, o instante da ocorrência
    Escopo: função global paramétrica
    Dados de entrada: tupla de um robô
    Dados de saída: segundo elemento da tupla de um robô
    '''

    try:
        if len(tuplaRobos) < 2: # Não funciona com < 4 (descobrir por quê)
            print("Tupla não possui elementos o suficiente.")
            raise Exception()
        else:
            return tuplaRobos[1]
    except:
        pass


def pegaLocal(tuplaRobos):
    ''' Função: pegaLocal()
    Descrição: retorna o terceiro elemento da tupla de um robô,
    isto é, a localização do robô na ocorrência
    Escopo: função global paramétrica
    Dados de entrada: tupla de um robô
    Dados de saída: terceiro elemento da tupla de um robô
    '''

    try:
        if len(tuplaRobos) < 2: # Não funciona com < 4 (descobrir por quê)
            print("Tupla não possui elementos o suficiente.")
            raise Exception()
        else:
            return tuplaRobos[2]
    except:
        pass



def pegaVitimas(tuplaRobos):
    ''' Função: pegaVitimas()
    Descrição: retorna o quarto (último) elemento da tupla de um robô,
    isto é, o número de vítimas avistadas
    Escopo: função global paramétrica
    Dados de entrada: tupla de um robô
    Dados de saída: quarto (último) elemento da tupla de um robô
    '''

    try:
        if len(tuplaRobos) < 2: # Não funciona com < 4 (descobrir por quê)
            print("Tupla não possui elementos o suficiente.")
            raise Exception()
        else:
            return tuplaRobos[-1]
    except:
        pass


def tupla1(tupla2):
    ''' Função: tupla1()
    Descrição: retorna o primeiro elemento de uma tupla de 2 elementos
    Escopo: função global paramétrica
    Dados de entrada: tupla de 2 elementos
    Dados de saída: primeiro elemento da tupla
    '''

    try:
        if len(tupla2) == 0:
            print("Tupla vazia não possui elementos.")
            raise Exception()
        else:
            return tupla2[0]
    except:
        pass


def tupla2(tupla2):
    ''' Função: tupla2()
    Descrição: retorna o segundo (último) elemento de uma tupla de 2 elementos
    Escopo: função global paramétrica
    Dados de entrada: tupla de 2 elementos
    Dados de saída: segundo (último) elemento da tupla
    '''

    try:
        if len(tupla2) < 2:
            print("Tupla não possui elementos o suficiente.")
            raise Exception()
        else:
            return tupla2[-1]
    except:
        pass
