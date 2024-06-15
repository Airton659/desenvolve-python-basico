
sequencia4 = [i for i in range(0,30,3)]
pares = [i for i in range(20,51) if i%2 == 0 ]
quadrados = [n**2 for n in range(1,10)]
divisiveis = [ i for i in range(1,101) if i%7 == 0]
par_ou_impar = ["par" if i % 2 == 0 else "impar" for i in range(0, 30, 3)]


print (par_ou_impar)