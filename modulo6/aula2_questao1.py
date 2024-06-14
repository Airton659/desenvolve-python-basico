import random
lista = []

for i in range (20):
    lista.append(random.randint(-100,100))

print(sorted(lista))
print(lista)
print("O índice do maior valor da lista é: ", lista.index(max(lista))+1)
print("O índice do menor valor da lista é: ", lista.index(min(lista))+1)



