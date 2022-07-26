inicio = int(input()) 
fim = int(input())
anos_bissextos = 0

if 0 <= inicio <= fim <= 9999:
  for ano in range(inicio,fim+1,1):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
      print(f"{ano}")
      anos_bissextos +=1

  print(f"bissextos: {anos_bissextos}")