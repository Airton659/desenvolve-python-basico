avalia = 6

while avalia > 5 or avalia < 1:
    avalia = int(input("Digite a avaliação do filme: "))

if avalia == 5:
    print("Excelente!")
if avalia == 4:
    print("Muito Bom!")
if avalia == 3:
    print("Bom!")
if avalia == 2:
    print("Regular.")
if avalia == 1:
    print("Ruim.")