import random

numero = random.randint(1,10)
palpite = 11

print(numero)

while palpite != numero:
    palpite = int(input("Adivinha o número entre 1 e 10: "))
    if palpite < numero:
        print("Muito baixo, tente novamente")
    else:
        print("Muito alto, tente novamente")

print(f"Correto! O número é {numero}")