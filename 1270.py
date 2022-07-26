tabuada_inicio = int(input())
tabuada_fim = int(input())

if tabuada_fim >= tabuada_inicio:
   for tabuada in range(tabuada_inicio, tabuada_fim + 1):
     for multiplicador in range(1,11):
      print(f"{tabuada} x {multiplicador} = {tabuada * multiplicador}")
     print('-'*10)
else:
  print("Nenhuma tabuada no intervalo!")