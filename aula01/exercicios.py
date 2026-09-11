"""Aula 01 - De C para Python.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.
"""


def soma_lista(lista):
    soma = 0
    for n in lista:
        soma = soma + n 
    return soma

def conta_pares(lista):
    cont = 0
    for n in lista:
        if n % 2 == 0:
            cont = cont + 1
    return cont


def maior_valor(lista):
    maior = lista[0]
    for n in lista[i]:
        if n > maior:
            maior = n 
    return maior

def existe(lista, alvo):
    for i in lista: 
        if n == i:
            return True
    
    return False


def busca_linear(lista, alvo):
    for i in range (len ( lista ) ) :
        if lista [ i ] == alvo :
            return i
    return -1

def segundo_maior(lista):
    maior = lista[0]
    segundo = lista[1]
    if maior < segundo:
        maior, segundo = segundo, maior

    for n in lista[2:]:
        if n > maior:
            segundo = maior
            maior = n
        elif n > segundo:
            segundo = n
            
    return segundo

