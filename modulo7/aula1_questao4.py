numero = input("Digite o número: ")

if len(numero) == 8:
    numero = '9' + numero
elif len(numero) == 9:
    if numero[0] != "9":
        print("Entrada inválida")
        exit()
else:
    print("Entrada inválida")
    exit()

print(numero[:5] + '-' + numero[5:])


