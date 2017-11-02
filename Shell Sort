#Shell Sort (Extensão do Insertion Sort)
#Princípio: Considera vários segmentos do array (divide o array em arrays menores)
#e aplica o insertion sort em cada um deles.
#Possui um bom desempenho em grandes vetores

import random
lista = []

def shellSort(lista):
    #Função que implementa o método de ordenamento Shell Sort.
    aux = len(lista) // 2
    while aux > 0:
         for i in range(aux, len(lista)):
             temp = lista[i]
             j = i
             while j >= aux and lista[j - aux] > temp:
                 lista[j] = lista[j - aux]
                 j -= aux
             lista[j] = temp
         aux //= 2


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
shellSort(lista)
print("Lista Ordenada (Shell Sort):")
print(lista)

