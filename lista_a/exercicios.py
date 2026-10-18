"""Lista A - Python, listas, busca e custo.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

Os exercicios do Bloco 3 devolvem DOIS valores: o resultado e a contagem.
"""

# ---------- Bloco 1: listas e percurso ----------

def conta_negativos(lista):
    """Quantos numeros da lista sao menores que zero."""
    cont = 0
    for x in lista:
        if x < 0:
            cont += 1
    return cont


def media(lista):
    """Media dos numeros. Lista vazia devolve 0."""
    if len(lista) == 0:
        return 0
    total = 0
    for x in lista:
        total += x
    return total / len(lista)


def sem_o_maior(lista):
    """Lista NOVA sem o maior valor. Se o maior repete, tira so o primeiro."""
    if len(lista) == 0:
        return []
    pos_maior = 0
    for i in range(1, len(lista)):
        if lista[i] > lista[pos_maior]:
            pos_maior = i
    return lista[:pos_maior] + lista[pos_maior + 1:]


def acumulada(lista):
    """Lista NOVA onde cada posicao e a soma de tudo ate ali."""
    resultado = []
    soma = 0
    for x in lista:
        soma += x
        resultado.append(soma)
    return resultado


def achata(lista_de_listas):
    """Junta as sublistas numa lista so."""
    resultado = []
    for sub in lista_de_listas:
        for x in sub:
            resultado.append(x)
    return resultado


# ---------- Bloco 2: busca ----------

def busca_ultima(lista, alvo):
    """ULTIMA posicao do alvo, ou -1."""
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] == alvo:
            return i
    return -1


def conta_ocorrencias(lista, alvo):
    """Quantas vezes o alvo aparece."""
    cont = 0
    for x in lista:
        if x == alvo:
            cont += 1
    return cont


def primeiro_maior_que(lista, limite):
    """Posicao do primeiro elemento maior que limite, ou -1."""
    for i in range(len(lista)):
        if lista[i] > limite:
            return i
    return -1


def busca_binaria_primeira(lista, alvo):
    """Lista JA ORDENADA, o alvo pode repetir. PRIMEIRA posicao, ou -1."""
    ini, fim = 0, len(lista) - 1
    achado = -1
    while ini <= fim:
        meio = (ini + fim) // 2
        if lista[meio] == alvo:
            achado = meio        # guarda e continua procurando a esquerda
            fim = meio - 1
        elif lista[meio] < alvo:
            ini = meio + 1
        else:
            fim = meio - 1
    return achado


# ---------- Bloco 3: custo ----------

def soma_pares_contando(lista):
    """(soma_dos_pares, operacoes). 1 por elemento examinado."""
    soma = 0
    ops = 0
    for x in lista:
        ops += 1
        if x % 2 == 0:
            soma += x
    return soma, ops


def maior_contando(lista):
    """(maior, comparacoes). Lista nao vazia."""
    maior = lista[0]
    comps = 0
    for i in range(1, len(lista)):
        comps += 1
        if lista[i] > maior:
            maior = lista[i]
    return maior, comps


def tem_soma_contando(lista, alvo):
    """(True/False, comparacoes). 1 por par comparado; para ao achar."""
    comps = 0
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            comps += 1
            if lista[i] + lista[j] == alvo:
                return True, comps
    return False, comps


def ordenada_contando(lista):
    """(True/False, comparacoes). 1 por par de vizinhos; para no primeiro fora de ordem."""
    comps = 0
    for i in range(len(lista) - 1):
        comps += 1
        if lista[i] > lista[i + 1]:
            return False, comps
    return True, comps


# ---------- Bloco 4: padroes ----------

def inverte_no_lugar(lista):
    """Inverte a PROPRIA lista. Nao cria lista nova e nao devolve nada."""
    i, j = 0, len(lista) - 1
    while i < j:
        lista[i], lista[j] = lista[j], lista[i]
        i += 1
        j -= 1


def eh_palindromo(lista):
    """True se a lista e igual lida de tras para frente."""
    i, j = 0, len(lista) - 1
    while i < j:
        if lista[i] != lista[j]:
            return False
        i += 1
        j -= 1
    return True


def par_que_soma(lista, alvo):
    """Lista JA ORDENADA. (i, j) cujos valores somam alvo, ou (-1, -1)."""
    i, j = 0, len(lista) - 1
    while i < j:
        s = lista[i] + lista[j]
        if s == alvo:
            return (i, j)
        elif s < alvo:
            i += 1
        else:
            j -= 1
    return (-1, -1)


def soma_maxima_janela(lista, k):
    """Maior soma de k elementos seguidos."""
    if k <= 0 or k > len(lista):
        return 0
    janela = 0
    for i in range(k):
        janela += lista[i]
    melhor = janela
    for i in range(k, len(lista)):
        janela += lista[i] - lista[i - k]
        if janela > melhor:
            melhor = janela
    return melhor


def parenteses_balanceados(texto):
    """True se os ( ) e [ ] do texto abrem e fecham na ordem certa."""
    pares = {")": "(", "]": "["}
    pilha = []
    for c in texto:
        if c in "([":
            pilha.append(c)
        elif c in ")]":
            if len(pilha) == 0 or pilha[-1] != pares[c]:
                return False
            pilha.pop()
    return len(pilha) == 0
