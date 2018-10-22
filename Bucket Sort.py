#Bucket Sort 
#Princípio: Divida o vetor em um número finito de 'baldes' e ordene cada 'balde'
#individualmente (usando um algoritmo de ordenação qualquer, nesse caso utilizei
#o quick sort). 
#Complexidade (Θ(n)), quando o vetor contém elementos uniformemente distribuídos.

from RandomHelper import random_list

def quickSort(lista):
    #Função que implementa o método de ordenamento Quick Sort.
    L=[]
    R=[]
    if len(lista)<=1:
        return lista
    
    chave =lista[len(lista)//2]
    for i in lista:
        if i<chave:
            L.append(i)
        if i>chave:
            R.append(i)
    return quickSort(L)+[chave]+quickSort(R)

def bucketSort(lista):
    #Função que implementa o método de ordenamento Bucket Sort.
    partMax = max(lista)
    part1 = [list() for _ in range(partMax)]
    for i in lista:
        part1[(i//10)].append(i)
    list_aux = []
    for part2 in part1:
        if len(part2) > 0:
            list_aux.append(quickSort(part2))
    return list_aux



print("Lista Ordenada (Bucket Sort):")
print(bucketSort(random_list(20)))
