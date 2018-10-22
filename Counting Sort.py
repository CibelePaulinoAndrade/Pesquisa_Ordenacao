# -*- coding: utf-8 -*-
#Counting Sort 
#Princípio: Determinar, para cada entrada, o número de elementos menor que ela.
#Essa informação é utilizada para colocar a entrada na sua posição no array de saída.
#Complexidade O(n).

import random
lista = []
listaaux = []

def countSort(lista):
    #Função que implementa o método de ordenamento Counting Sort.
    maximo = max(lista)
    minimo = min(lista)
    count_array = [0]*(maximo-minimo+1)
 
    for val in lista:
        count_array[val-minimo] += 1
    for i in range(minimo, maximo+1):
        if count_array[i-minimo] > 0:
            for j in range(0, count_array[i-minimo]):
                listaaux.append(i)


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


listaRan(20, lista)
countSort(lista)
print("Lista Ordenada (Counting Sort):")
print(listaaux)

