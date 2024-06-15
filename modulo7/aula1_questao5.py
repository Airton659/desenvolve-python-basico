frase = input("Digite uma frase: ")


indices = [i for i in range (len(frase)) if frase[i] in "aeiouAEIOU"]
print(f"{len(indices)} vogais")
print(indices)