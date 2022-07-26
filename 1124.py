numero = int(input())
par = numero % 2 == 0
nimpar = 0
npar = 0

if par:
  nimpar = numero - 1
  npar = numero + 2
else:
  nimpar = numero - 2
  npar = numero + 1

print(f"{nimpar} {npar}")