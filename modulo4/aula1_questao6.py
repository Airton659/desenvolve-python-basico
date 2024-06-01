n = int(input("Digite a quantidade de experimentos realizados: "))

cont = 1
tipo = "k"
total_sapo = 0
total_rato = 0
total_coelho = 0
total = 0

while cont <= n:
    quantia = int(input(f"Digite a quantidade de cobaias do experimento nº {cont}:"))
    while tipo not in ["S", "s", "R", "r", "C", "c"]:
        tipo = input("Digite o tipo de cobaia (S, R ou C): ")
    if tipo == "S" or tipo == "s":
        total_sapo = total_sapo + quantia
        total = total + quantia
    elif tipo == "R" or tipo == "r":
        total_rato = total_rato + quantia
        total = total + quantia
    else:
        total_coelho = total_coelho + quantia
        total = total + quantia
    cont += 1
    tipo = "K"

percentual_coelhos =  (total_coelho / total) * 100
percentual_ratos =  (total_rato / total) * 100
percentual_sapos =  (total_sapo / total) * 100

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {total_coelho}")
print(f"Total de ratos: {total_rato}")
print(f"Total de sapos: {total_sapo}")
print(f"Percentual de coelhos: {percentual_coelhos:.2f}%")
print(f"Percentual de ratos: {percentual_ratos:.2f}%")
print(f"Percentual de sapos: {percentual_sapos:.2f}%")