classe = "inicial"
forca = 00
magia = 0

while classe not in ["guerreiro", "Guerreiro", "mago", "Mago","arqueiro", "Arqueiro"]:
    classe = input("Digite a sua classe (Guerreiro, Mago ou Arqueiro): ")

while forca > 20 or forca < 1 :
    forca = int(input("Digite os pontos de força (de 1 a 20): "))

while magia > 20 or magia < 1 :
    magia = int(input("Digite os pontos de magia (de 1 a 20): "))

resultado = (classe in ["guerreiro", "Guerreiro"] and forca >=15 and magia <=10) or (classe in ["mago", "Mago"] and forca <= 10 and magia >=15) or (classe in ["arqueiro", "Arqueiro"] and (forca > 5 and forca <=15 ) and (magia > 5 and magia <= 15))

print(f"Pontos de atributo consistente com a classe escolhida: {resultado}")