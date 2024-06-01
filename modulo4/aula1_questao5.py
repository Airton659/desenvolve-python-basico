n = int(input("Digite a quantidade de respondentes: "))

cont = 1
idade = 0

while cont <= n:
    idade = idade + int(input(f"Digite a idade da {cont} pessoa: "))
    cont +=1

print (idade / n)