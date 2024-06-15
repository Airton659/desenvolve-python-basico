import random
import os

def ler_palavra():
    with open("gabarito_forca.txt", 'r') as arquivo:
        palavras = arquivo.readlines()
        palavra = random.choice(palavras).strip().lower()
    return palavra

def ler_estagios_enforcado():
    with open('gabarito_enforcado.txt', 'r') as arquivo:
        estagios_enforcado = arquivo.read().strip().split('\n\n')
    return estagios_enforcado

def imprime_enforcado(estagios, erros):
    print(estagios[erros])

def jogar_forca():
    palavra = ler_palavra()
    certo = ['_'] * len(palavra)
    errado = []
    estagios_enforcado = ler_estagios_enforcado()
    tentativas = 6
    erros = 0

    print(f'Palavra secreta: {" ".join(certo)}')

    while tentativas > 0:
        letra = input("Digite uma letra: ").lower()

        if letra in certo or letra in errado:
            print(f'A letra {letra} já foi tentada, tente outra.')
            continue
        
        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    certo[i] = letra
            print(f'Acertou! Palavra secreta: {" ".join(certo)}')
        else:
            errado.append(letra)
            tentativas -= 1
            erros += 1
            imprime_enforcado(estagios_enforcado, erros)
            print(f'Errou! Letras erradas: {", ".join(errado)}')
            print(f'Restam {tentativas} tentativas.')

        if '_' not in certo:
            print('Parabéns, você descobriu a palavra secreta.')
            break

    if '_' in certo:
        print(f'Você perdeu, a palavra secreta era {palavra}.')

# Inicia o jogo da forca
jogar_forca()