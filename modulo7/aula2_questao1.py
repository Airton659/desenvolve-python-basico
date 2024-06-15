meses = ["Janeiro", "Fevereiro","Março", "Abril",
         "Maio", "Junho","Julho","Agosto","Setembro",
         "Outubro","Novembro","Dezembro"]

data = input("Digite uma data de nascimento: ")

dia, mes, ano = data.split('/')

dia = int(dia)
mes = int(mes)
ano = int(ano)

if mes < 1 or mes > 12:
    print("Data incorreta")
else:
    print(f"Você nasceu em {dia} de {meses[mes - 1]} de {ano}.")