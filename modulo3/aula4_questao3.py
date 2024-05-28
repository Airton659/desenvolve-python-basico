ano = int(input("Digite o ano a ser verificado: "))

por_4 = ano % 4
por_100 = ano % 100
por_400 = ano % 400

if (por_4 == 0 and por_100 != 0) or por_400 == 0:
    print("Bissexto")
else:
    print("Não bissexto")