def encontra_anagrama(frase, objetivo):
    def sao_anagramas(palavra1,palavra2):
        return sorted(palavra1.lower()) == sorted(palavra2.lower())
    
    palavras = frase.split()

    anagramas = [palavra for palavra in palavras if len(palavra) == len(objetivo) and sao_anagramas(palavra,objetivo)]

    return anagramas

frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")
anagramas = encontra_anagrama(frase, palavra_objetivo)
print("Anagramas:", anagramas)