"""Aula 02 - Listas em Python.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.
"""

def remove_negativos(lista):
    novalista = []

    for i in lista:
        if i >= 0:
            novalista.append(i)
    return novalista



def inverte(lista):

    nova_lista = []

    i = len(lista) - 1

    while i >= 0:
        nova_lista.append(lista[i])
        i = i - 1

    return nova_lista


def busca_binaria(lista, alvo):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (alto + baixo) // 2

        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            baixo = meio + 1
        else:
            alto = meio - 1

    return -1


def intercala(lista_a, lista_b):

    novalista = []

    i = 0

    while i < len(lista_a):
        novalista.append(lista_a[i])
        novalista.append(lista_b[i])
        i = i + 1

    return novalista

def remove_repetidos(lista):

    nova_lista = []

    for numero in lista:

        i = 0
        repetido = False

        while i < len(nova_lista):

            if nova_lista[i] == numero:
                repetido = True

            i = i + 1

        if repetido == False:
            nova_lista.append(numero)

    return nova_lista