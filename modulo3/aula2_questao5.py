genero = "i"

while genero not in ["M","m","F","f"]:
    genero = input("Digite o seu gênero (M ou F): ")

idade = int(input("Digite a sua idade: "))
tempo_de_servico = int(input("Digite o seu tempo de serviço em anos: "))

resultado = (genero in ["F","f"] and idade >= 60) or (genero in ["M","m"] and idade >= 65) or tempo_de_servico >= 30 or (idade >= 60 and tempo_de_servico >= 25)

print(f"A situação da aponsentadoria é: {resultado}")