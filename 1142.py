N = int(input())

if (N <= 10):
  contador = 1

  while (contador <= 10):
    print(f'{N} x {contador} = {N * contador}')
    contador += 1