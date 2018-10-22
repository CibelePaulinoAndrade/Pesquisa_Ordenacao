#Merge Sort
#Princípio: Dividir o problema em vários sub-problemas, resolver esses
#sub-problemas através da recursividade e, por fim, unir as resoluções dos
#sub-problemas.
#Eficiente quando existe uma grande quantidade de elementos
#Complexidade n log n.


from RandomHelper import random_list

def mergeSort(lista):
    #Função que implementa o método de ordenamento Merge Sort.
    if len(lista) > 1:
        meio = len(lista)//2
        listaDaEsquerda = lista[:meio]
        listaDaDireita = lista[meio:]
        mergeSort(listaDaEsquerda)
        mergeSort(listaDaDireita)
        i = 0
        j = 0
        k = 0
        while i < len(listaDaEsquerda) and j < len(listaDaDireita):
            if listaDaEsquerda[i] < listaDaDireita[j]:
                lista[k]=listaDaEsquerda[i]
                i += 1
            else:
                lista[k]=listaDaDireita[j]
                j += 1
            k += 1
        while i < len(listaDaEsquerda):
            lista[k]=listaDaEsquerda[i]
            i += 1
            k += 1
        while j < len(listaDaDireita):
            lista[k]=listaDaDireita[j]
            j += 1
            k += 1
    return lista


print(mergeSort(random_list(20)))

