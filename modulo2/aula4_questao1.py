#Solicitando e armazenando o comprimento do terreno
comprimento = int(input("Digite o comprimento do terreno:"))

#Solicitando e armazenando a largura do terreno 
largura = int(input("Digite a largura do terreno:"))

#Solicitando e armazenando o preço do metro quadrado na região
preco = float(input("Digite o valor do metro quadrado na regiao"))

#Calculando o tamanho do terreno
tamanho = comprimento * largura

#Calculando o valor do terreno
valor = tamanho * preco

#Imprimindo o resultado
print(f"O terreno possui {tamanho}m2 e custa R${valor}")