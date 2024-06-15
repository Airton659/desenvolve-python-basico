import re

def calcular_digito(cpf, multiplicadores):
    soma = sum(int(cpf[i]) * multiplicadores[i] for i in range(len(multiplicadores)))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

def validar_cpf(cpf):
    
    if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
        return "Inválido"
    
    cpf = re.sub(r'\D', '', cpf)
    cpf_base = cpf[:9]

    primeiro_digito = calcular_digito(cpf_base, range(10, 1, -1))
    cpf_base += str(primeiro_digito)

    segundo_digito = calcular_digito(cpf_base, range(11, 1, -1))
    cpf_calculado = cpf_base + str(segundo_digito)
    
    if cpf_calculado == cpf:
        return "Válido"
    else:
        return "Inválido"


cpf_usuario = input("Digite um CPF na forma XXX.XXX.XXX-XX: ")
resultado = validar_cpf(cpf_usuario)
print(resultado)
