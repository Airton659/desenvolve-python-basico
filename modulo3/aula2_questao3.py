idade = int(input("Digite sua idade: "))

resposta = "truefalse"

while resposta not in ['True', 'true', 'False','false']:       
    resposta = input("Já jogou pelo menos 3 jogos de tabuleiro (True/False) ")

vitoria = int(input("Quantos jogos já venceu? "))

apto = idade >= 16 and idade <= 18 and (resposta == 'true' or resposta == "True") and vitoria >1

print(f"Apto para ingressar no clube de jogos de Tabuleiro: {apto}")
