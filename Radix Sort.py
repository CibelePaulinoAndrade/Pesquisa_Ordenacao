#Radix Sort 
#Princípio: Ordenar elementos identificados por chaves únicas em qualquer ordem
#relacionada com a lexicografia
#Complexidade Θ(nk), onde k = tamanho string e n = número de elementos.

import random
lista = []

def radixSort(lista):
    #Função que implementa o método de ordenamento Radix Sort.
    RADIX = 10
    tamMax = False
    temp , aux = -1, 1
   
    while not tamMax:
        tamMax = True
        pilha = [list() for _ in range( RADIX )]
   
        for  i in lista:
            temp = i // aux
            pilha[temp % RADIX].append( i )
            if tamMax and temp > 0:
                tamMax = False
   
        a = 0
        for b in range( RADIX ):
            buck = pilha[b]
            for i in buck:
                lista[a] = i
                a += 1
   
        aux *= RADIX


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
radixSort(lista)
print("Lista Ordenada (Radix Sort):")
print(lista)
