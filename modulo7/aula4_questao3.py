import os

def analisa_arquivo(nome):
    with open(nome,"r") as arquivo:
        print("Texto das primeiras 25 linhas: ")
        for i in range(25):
            linha = arquivo.readline().strip()
            print(linha)

        arquivo.seek(0)

        num_linhas = sum(1 for _ in arquivo)
        print(f"Numero total de linhas do arquivo: {num_linhas}")

        arquivo.seek(0)
        linha_mais_longa = ""
        maximo = 0
        for linha in arquivo:
            quantidade = len(linha)
            if quantidade > maximo:
                maximo = quantidade
                linha_mais_longa = linha.strip()
        print("Linha com maior número de caracteres:")
        print(f"{linha_mais_longa} ({maximo} caracteres)")

        arquivo.seek(0)
        conteudo = arquivo.read().lower()
        nonato = conteudo.count("nonato")
        iria = conteudo.count("íria")
        print("Menção aos nomes dos personagens: ")
        print(f"Nonato: {nonato} vezes")
        print(f"Íria: {iria} vezes")

diretorio = os.getcwd()
arquivo = "aula4_questao3.txt"

caminho = os.path.join(diretorio,arquivo)

if os.path.exists(caminho):
    analisa_arquivo(caminho)
else:
    print(f"Arquivo {arquivo} não encontrado.")