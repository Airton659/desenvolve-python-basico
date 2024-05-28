entrada = int(input("Digite o valor a ser dividido: "))

n_100 = entrada // 100
entrada = entrada % 100

n_50 = entrada // 50
entrada = entrada % 50

n_20 = entrada // 20
entrada = entrada % 20

n_10 = entrada // 10
entrada = entrada % 10

n_5 = entrada // 5
entrada = entrada % 5

n_2 = entrada // 2

n_1 = entrada % 2

print(f"{n_100} nota(s) de R$100,00")
print(f"{n_50} nota(s) de R$50,00")
print(f"{n_20} nota(s) de R$20,00")
print(f"{n_10} nota(s) de R$10,00")
print(f"{n_5} nota(s) de R$5,00")
print(f"{n_2} nota(s) de R$2,00")
print(f"{n_1} nota(s) de R$1,00")

