produto1 = input("Digite o nome do produto 1: ")
preco_unitario1 = float(input("Digite o preço unitário do produto 1:"))
quantidade1 = int(input("Digite a quantidade comprada do produto 1: ")) 

produto2 = input("Digite o nome do produto 2: ")
preco_unitario2 = float(input("Digite o preço unitário do produto 2:"))
quantidade2 = int(input("Digite a quantidade comprada do produto 2: "))

produto3 = input("Digite o nome do produto 3: ")
preco_unitario3 = float(input("Digite o preço unitário do produto 3:"))
quantidade3 = int(input("Digite a quantidade comprada do produto 3: ")) 

total = (preco_unitario1 * quantidade1) + (preco_unitario2 * quantidade2) + (preco_unitario3 * quantidade3)

print(f"R${total:,.2f}")