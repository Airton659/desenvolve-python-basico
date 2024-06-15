import re

def limpa_e_divide(texto):
    limpo = re.sub(r"[^a-zA-Z\s]","",texto)
    palavras = limpo.split()
    return palavras

caminho = "frase.txt"

with open(caminho,"r") as arquivo:
    conteudo = arquivo.read()

palavras = limpa_e_divide(conteudo)

caminho_destino = "palavras.txt"
with open(caminho_destino,"w") as arquivo_destino:
    for palavra in palavras:
        arquivo_destino.write(palavra + "\n")

with open(caminho_destino, "r") as arquivo_destino_leitura:
    conteudo_palavras = arquivo_destino_leitura.read()
    print(conteudo_palavras)