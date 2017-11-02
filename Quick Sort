#Quick Sort
#Princípio: Rearranjar um vetor de modo que todos os elementos pequenos fiquem
#na parte esquerda (L) e todos os elementos grandes fiquem na parte direita(R).
#Em alguns casos pode ser tão lento quanto algoritmos elementares, mas no geral
#é muito rápido.
#Complexidade n log n em média e n^2 no pior caso.


import random

def quickSort(lista):
    #Função que implementa o método de ordenamento Quick Sort.
    L=[]
    R=[]
    if len(lista) <= 1:
        return lista
    chave = lista [len(lista)//2]
    for i in lista:
        if i < chave:
            L.append(i)
        if i > chave:
            R.append(i)
    return quickSort(L)+[chave]+quickSort(R)

def listaRan(tam, lista):
    #Função gera uma 'lista' com 'tam' valores aleatórios.
    random.seed()
    i=0
    while i<tam:
        num = random.randint(1, 10*tam)
        if num not in lista:
            lista.append(num)
            i+=1
    print("Lista Desordenada:")
    print(lista)

lista = []
listaRan(20, lista)
lista = quickSort(lista)
print("Lista Ordenada (Quick Sort):")
print(lista)
