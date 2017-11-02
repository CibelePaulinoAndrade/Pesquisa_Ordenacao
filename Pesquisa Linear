#Pesquisa Linear
#Princípio: Pesquisa em vetores ou listas de modo sequencial, elemento por
#elemento. Dessa forma a função do tempo em relação ao número de elementos
#é linear, ou seja, cresce de forma proporcional.


import random

def pesLinear(elem, lista):
    #Função que implementa a pesquisa linear.
    for i in lista:
        if i == elem:
            return True
    return False

def listaRan(tam, lista):
    #Função gera uma 'lista' com 'tam' valores aleatórios.
    random.seed()
    i=0
    while i<tam:
        num = random.randint(1, 10*tam)
        if num not in lista:
            lista.append(num)
            i+=1
    print("Lista:")
    print(lista)

def valorBusca (tam):
    #Função que gera um inteiro aleatório.
    random.seed()
    elem = random.randint (1, 10*tam)
    return elem

lista = []
listaRan(20, lista)
elem = valorBusca (20)
result = pesLinear(20, lista)
print ("A busca pelo elemento ", elem, "retornou ", result)

