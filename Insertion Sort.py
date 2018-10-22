#Insertion Sort
#Princípio: Lembra a maneira como classificamos as cartas em nossas mãos. Pega
#um elemento, percorre o array comparando com cada elemento presente, insere
#o novo elemento no lugar adequado. Repete o processo até que todos os elementos
#estejam ordenados. 
#Eficiente para vetores pequenos ou quando já está quase ordenado.
#Complexidade de ordem quadrática (n^2) no pior caso.
#Requer espaço constante de mémoria adicional.


from RandomHelper import random_list

def insertionSort(lista):
    #Função que implementa o método de ordenamento Insertion Sort.
    for i in range (1, len(lista)):
        chave = lista[i]
        j=i-1
        while j>=0 and chave<lista[j]:
            lista[j+1] = lista[j]
            j-=1
        lista[j+1]=chave
        
    return lista


print(insertionSort(random_list(20)))
