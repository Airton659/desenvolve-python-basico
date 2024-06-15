import string

def eh_palindromo(frase):    
    frase_filtrada = ''.join(char.lower() for char in frase if char.isalnum())
    return frase_filtrada == frase_filtrada[::-1]

while True:    
    frase_usuario = input('Digite uma frase (digite "fim" para encerrar): ')
    if frase_usuario.lower() == "fim":
        break

    if eh_palindromo(frase_usuario):
        print(f'"{frase_usuario}" é um palíndromo.')
        
    else:
        print(f'"{frase_usuario}" não é um palíndromo.')
