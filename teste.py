
encontra_maior = lambda x, y: x if x > y else y


encontra_menor = lambda x, y: x if x < y else y

opcao = 3
print("Escolha uma das opções:")
while opcao not in [1,2]:
    print("1 - Maior")
    print("2 - Menor")
    opcao = int(input("Opção: "))

print("Digite os valores de entrada. Digite 0 para finalizar a entrada de valores.")

numero = 1
maior = float('-inf')
menor = float('inf')
while numero != 0:
    numero = int(input())
    if numero != 0:
        if opcao == 1:
            maior = encontra_maior(numero,maior)
        else:
            menor = encontra_menor(numero,menor)

if opcao == 1:
    print(f"O maior valor é {maior}") 
else:
    print(f"O menor número é {menor}")