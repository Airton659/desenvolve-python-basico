import csv

livros = [
    ["Duna", "Frank Herbert", 1965, 412],
    ["A Fundação", "Isaac Asimov", 1951, 255],
    ["Star Wars: Herdeiro do Império", "Timothy Zahn", 1991, 404],
    ["O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 1216],
    ["O Guia do Mochileiro das Galáxias", "Douglas Adams", 1979, 224],
    ["Eu, Robô", "Isaac Asimov", 1950, 256],
    ["A Torre Negra", "Stephen King", 1982, 288],
    ["IT: A Coisa", "Stephen King", 1986, 1138],
    ["O Iluminado", "Stephen King", 1977, 447],
    ["Carrie, A Estranha", "Stephen King", 1974, 199],
]

with open("meus_livros.csv", mode='w', newline='', encoding='utf-8') as arquivo:
    escritor_csv = csv.writer(arquivo)
    escritor_csv.writerow(["Título", "Autor", "Ano de publicação", "Número de páginas"])
    escritor_csv.writerows(livros)

print("Arquivo 'meus_livros.csv' criado com sucesso!")
