distancia = int(input("Digite a distância em km do local da entrega: "))
peso = float(input("Digite o peso em quilograma da entrega: "))

if distancia <= 100:
    if peso > 10:
        valor= peso + 10
        print(f"O valor do frete é: R${valor}")
    else:
        print(f"O valor do frete é: R${peso}")
if distancia > 100 and distancia <=300:
    valor = peso * 1.5
    if peso > 10:
        valor= valor + 10
        print(f"O valor do frete é: R${valor}")
    else:
        print(f"O valor do frete é: R${valor}")