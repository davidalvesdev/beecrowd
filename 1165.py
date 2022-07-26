soma = 0
continua = True

while continua:
  
  doacao = float(input())
  if doacao >= 0 :
    soma += doacao
  else:
    continua = False

print(f"VC$ {soma:.2f}")
print(f"R$ {soma*2.5:.2f}")