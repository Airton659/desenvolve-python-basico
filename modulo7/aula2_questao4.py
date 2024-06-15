import string

def valida_senha(senha):
    if len(senha) < 8:
        return False
    
    if not any(letra.isupper() for letra in senha):
        return False
    
    if not any(letra.isdigit() for letra in senha):
        return False
    
    caracter = set(string.punctuation)
    if not any (letra in caracter for letra in senha):
        return False

    return True

senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"

print(valida_senha(senha1))
print(valida_senha(senha2))
print(valida_senha(senha3))    