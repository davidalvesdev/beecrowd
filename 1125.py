ntrabalho = float(input())
nprova = float(input())

media = (ntrabalho + nprova) / 2

if media >=6:
  print("aprovado")
elif ((ntrabalho + 10) / 2 ) >=6:
  print('talvez com a sub')
else:
  print("reprovado")