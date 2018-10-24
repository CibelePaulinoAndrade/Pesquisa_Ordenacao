import random

def random_list(size):
    lista=[]
    random.seed()
    i=0
    while i<size:
        num = random.randint(1, 10*size)
        if num not in lista:
            lista.append(num)
            i+=1
    return lista