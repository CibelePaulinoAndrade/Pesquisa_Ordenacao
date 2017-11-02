#Selection Sort
#Princípio: Colocar o menor valor na primeira posição e assim sucessivamente
#até que toda a lista esteja ordenada.
#Eficiente para vetores pequenos.
#Complexidade de ordem quadrática (n^2).


import random

def selectionSort(lista):
    #Função que implementa o método de ordenamento Selection Sort.
    for i in range (len(lista)-1,0,-1):
        valorminimo = 0
        for j in range (1, i+1):
            if lista[j] > lista[valorminimo]:
                valorminimo = j
        lista[i], lista[valorminimo] = lista[valorminimo], lista[i]
        
    print("Lista Ordenada (Selection Sort):")
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
selectionSort(lista)
