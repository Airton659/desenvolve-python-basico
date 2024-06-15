import os

frase = input("Digite uma frase: ")

caminho = os.path.join(os.getcwd(), "frase.txt")

with open(caminho, "w") as arquivo:
    arquivo.write(frase)

print(f"Frase salva em {caminho}")