def substitui(frase):
    vogais = "aeiouAEIOU"

    modificada = "".join("*" if letra in vogais else letra for letra in frase)

    return modificada

frase = input("Digite uma frase: ")
alterada = substitui(frase)

print("Frase modificada: ", alterada)

