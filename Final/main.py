import csv
import os

# Imprimir diretório de trabalho atual
print("Diretório de trabalho atual:", os.getcwd())

# Estrutura de dados para armazenar usuários
usuarios = {}

# Estrutura de dados para armazenar produtos
produtos = []

# Funções de Usuário (CRUD)
def criar_usuario(id_usuario, nome, senha, tipo):
    if id_usuario in usuarios:
        return "Usuário já existe."
    usuarios[id_usuario] = {"nome": nome, "senha": senha, "tipo": tipo}
    return "Usuário criado com sucesso."

def ler_usuarios():
    return usuarios

def atualizar_usuario(id_usuario, nome=None, senha=None, tipo=None):
    if id_usuario not in usuarios:
        return "Usuário não encontrado."
    if nome:
        usuarios[id_usuario]["nome"] = nome
    if senha:
        usuarios[id_usuario]["senha"] = senha
    if tipo:
        usuarios[id_usuario]["tipo"] = tipo
    return "Usuário atualizado com sucesso."

def deletar_usuario(id_usuario):
    if id_usuario not in usuarios:
        return "Usuário não encontrado."
    del usuarios[id_usuario]
    return "Usuário deletado com sucesso."

# Funções de Produto (CRUD)
def criar_produto(id_produto, nome, preco, quantidade):
    for produto in produtos:
        if produto["id_produto"] == id_produto:
            return "Produto já existe."
    produtos.append({"id_produto": id_produto, "nome": nome, "preco": preco, "quantidade": quantidade})
    return "Produto criado com sucesso."

def ler_produtos():
    return produtos

def atualizar_produto(id_produto, nome=None, preco=None, quantidade=None):
    for produto in produtos:
        if produto["id_produto"] == id_produto:
            if nome:
                produto["nome"] = nome
            if preco:
                produto["preco"] = preco
            if quantidade:
                produto["quantidade"] = quantidade
            return "Produto atualizado com sucesso."
    return "Produto não encontrado."

def deletar_produto(id_produto):
    for produto in produtos:
        if produto["id_produto"] == id_produto:
            produtos.remove(produto)
            return "Produto deletado com sucesso."
    return "Produto não encontrado."

def buscar_produto(termo):
    for produto in produtos:
        if produto["id_produto"] == termo or produto["nome"].lower() == termo.lower():
            return produto
    return "Produto não encontrado."

def ordenar_produtos_nome():
    return sorted(produtos, key=lambda x: x["nome"])

def ordenar_produtos_preco():
    return sorted(produtos, key=lambda x: x["preco"])

# Funções para carregar e salvar dados em arquivos
def carregar_usuarios(arquivo):
    with open(arquivo, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            usuarios[int(row["id_usuario"])] = {"nome": row["nome"], "senha": row["senha"], "tipo": row["tipo"]}

def salvar_usuarios(arquivo):
    with open(arquivo, mode='w', newline='') as file:
        fieldnames = ["id_usuario", "nome", "senha", "tipo"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for id_usuario, dados in usuarios.items():
            writer.writerow({"id_usuario": id_usuario, "nome": dados["nome"], "senha": dados["senha"], "tipo": dados["tipo"]})

def carregar_produtos(arquivo):
    with open(arquivo, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            produtos.append({"id_produto": int(row["id_produto"]), "nome": row["nome"], "preco": float(row["preco"]), "quantidade": int(row["quantidade"])})

def salvar_produtos(arquivo):
    with open(arquivo, mode='w', newline='') as file:
        fieldnames = ["id_produto", "nome", "preco", "quantidade"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for produto in produtos:
            writer.writerow(produto)

# Usar caminho absoluto (exemplo)
# carregar_usuarios('c:/Users/Administrador/Documents/EPython/desenvolve-python-basico/Final/usuarios.csv')
# carregar_produtos('c:/Users/Administrador/Documents/EPython/desenvolve-python-basico/Final/produtos.csv')

# Carregar dados iniciais (usando caminho relativo)
carregar_usuarios('usuarios.csv')
carregar_produtos('produtos.csv')

# Exemplo de uso das funções
print(criar_usuario(4, "funcionario2", "senha123", "funcionario"))
print(ler_usuarios())
print(atualizar_usuario(2, nome="funcionario1_atualizado"))
print(deletar_usuario(3))

print(criar_produto(4, "Machine Learning", 150.00, 8))
print(ler_produtos())
print(atualizar_produto(2, preco=85.00))
print(deletar_produto(3))

print(buscar_produto("Python para Iniciantes"))
print(ordenar_produtos_nome())
print(ordenar_produtos_preco())

# Salvar dados atualizados
salvar_usuarios('usuarios.csv')
salvar_produtos('produtos.csv')
