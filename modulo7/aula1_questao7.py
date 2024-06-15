import random

def encrypt(nome,chave):
    encrypted =[]
    for letra in nome:
        if ord(letra) >= 33 and ord(letra)<=126:
            ordem = (ord(letra) + chave)
            encrypted.append(chr(ord(letra) + chave))
        else:
            encrypted.append(letra)
    return "".join(encrypted)

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
chave_aleatoria = random.randint(1,10)

encrypted = [encrypt(nome, chave_aleatoria) for nome in nomes]
print(f"Nomes = {nomes}")
print(f"Chave aleatória: {chave_aleatoria}")
print(f"Nomes criptografádos = {encrypted}")