from random import choice, shuffle

n1 = input('Digite un nome >> ')
n2 = input('Digite un nome >> ')
n3 = input('Digite un nome >> ')
n4 = input('Digite un nome >> ')
n5 = input('Digite un nome >> ')

#um agrupamento 
lista = [n1, n2, n3, n4, n5]

shuffle(lista)
print(lista)

sorteio = choice(lista)
print(sorteio)