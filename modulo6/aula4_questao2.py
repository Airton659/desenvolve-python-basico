frase = input ("Digite uma frase: ")

vogais = [letra.lower() for letra in frase if letra.lower() in "aeiou"]
consoantes = [letra for letra in frase if letra.isalpha() and letra.lower() not in "aeiou"]

print(vogais)
print(consoantes)