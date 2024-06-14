numeros = []
while len(numeros) < 4:
    numeros.append(int(input("Digite um número inteiro: ")))

opcao = int(input("Digite um número inteiro ou 0 para finalizar: "))

if opcao != 0:
    numeros.append(opcao)
    while opcao != 0:
        opcao = int(input("Digite um número inteiro ou 0 para finalizar: "))
        if opcao == 0:
            break
        else:
            numeros.append(opcao)

print(f"A lista original é: {numeros}")
print(f"Os 3 primeiros elementos: {numeros[:3]}")
print(f"Os 2 últimos elementos: {numeros[-2:]}")
print(f"Lista invertida: {numeros[::-1]}")
print(f"Elementos de índice par: {numeros[::2]}")
print(f"Elementos de índice impar: {numeros[1::2]}")