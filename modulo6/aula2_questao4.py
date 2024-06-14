quantidade= int(input("Digite a quantidade de elementos da lista 1: "))
lista1,lista2,resultado = [],[],[]


for i in range (quantidade):
    lista1.append(int(input()))

print()
quantidade= int(input("Digite a quantidade de elementos da lista 2: "))

for i in range (quantidade):
    lista2.append(int(input()))

menor = min(len(lista1), len(lista2))

for i in range (menor):
    resultado.append(lista1[i])
    resultado.append(lista2[i])

if len(lista1) > len(lista2):
    resultado.extend(lista1[menor:])
else:
    resultado.extend(lista2[menor:])

print(f"Lista intercalada: {resultado}")