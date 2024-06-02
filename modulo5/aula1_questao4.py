import datetime

data_atual = datetime.datetime.now()
data = data_atual.strftime('%d/%m/%Y')
hora = data_atual.strftime('%H:%M')

print("Data: {}" .format(data_atual.strftime('%d/%m/%Y')))
print("Hora: {}" .format(data_atual.strftime('%H:%M')))