#Bubble Sort
#Princípio: Troca de valores entre posições consecutivas.
#Não é um algoritmo eficiente quando é necessária velocidade
#ou se tem um número elevado de elementos.
#Complexidade de ordem quadrática (n^2).


import random

def bubbleSort(lista):
    #Função que implementa o método de ordenamento Bubble Sort.
    for i in range (0, len(lista)):
        for j in range (0, len(lista)-1):
            if lista[j]>lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    print("Lista Ordenada (Bubble Sort):")
    print(lista)

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
bubbleSort(lista)

