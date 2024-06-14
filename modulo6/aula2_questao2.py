import random

elementos =[]

num_elementos = random.randint(5,20)
# print(num_elementos)

for i in range (num_elementos):
    elementos.append(random.randint(1,10))

soma = sum(elementos)
media = soma /num_elementos

print(elementos)
print(f"A soma dos valores da lista é: {soma}")
print(f"A média dos valores da lista é: {media: .2f}")
