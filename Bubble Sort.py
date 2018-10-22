# -*- coding: utf-8 -*-
#Bubble Sort
#Princípio: Troca de valores entre posições consecutivas.
#Não é um algoritmo eficiente quando é necessária velocidade
#ou se tem um número elevado de elementos.
#Complexidade de ordem quadrática (n^2).


from RandomHelper import random_list

def bubbleSort(lista):
    #Função que implementa o método de ordenamento Bubble Sort.
    for i in range (0, len(lista)):
        for j in range (0, len(lista)-1):
            if lista[j]>lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    print("Lista Ordenada (Bubble Sort):")
    print(lista)

bubbleSort(random_list(20))

