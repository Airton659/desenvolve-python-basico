import random

def embaralha(frase):
    palavras = frase.split()
    nova_frase = []

    for palavra in palavras:
        if len(palavra)> 2:
            primeira = palavra[0]
            ultima = palavra[-1]
            outras = list(palavra[1:-1])
            random.shuffle(outras)
            palavra = primeira + "".join(outras)+ ultima
            nova_frase.append(palavra)
        else:
            nova_frase.append(palavra)
    
    return " ".join(nova_frase)

frase = "Python é uma linguagem de programação"
frase_embaralhada = embaralha(frase)
print("Resultado:", frase_embaralhada)