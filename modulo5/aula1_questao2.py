import random
import math

soma = 0

n = int(input("Digite a quantidade de valores: "))

for i in range (1,n+1):
    soma += random.randint(0,100)

raiz =  math.sqrt(soma)

print(f"A raiz quadrada da soma de {n} números é: {raiz}")