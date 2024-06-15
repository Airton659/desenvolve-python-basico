alunos = ["Maria", "Jose", "Carla", "Sol"]
notas = [35, 50, 20, 80]
# aprovados = []
# for i in range(len(notas)):
#     if notas[i] >= 60:
#         aprovados.append(alunos[i])
# print(aprovados)


aprovado = [alunos[i] for i in range(len(notas)) if notas[i]>=60]

print(aprovado)