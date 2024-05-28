num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2
resultado = num1 % num2

if resultado == 0:
    print(f"A soma dos números {num1} e {num2} é {soma} e é um número par.")
else:
    print(f"A soma dos números {num1} e {num2} é {soma} e é um número impar.")
