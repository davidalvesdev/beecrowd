dia = input()
prazo = int(input())
dias_semana = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta' , 'sabado']
aux = 0

if prazo == 0:
  print("chega hoje!")
else:
  #procura dia da semana no array
  for i in range(6):
    if dia == dias_semana[i]:    
      break
    aux += 1  
  #soma prazo  
  for j in range(1,prazo+1):   
    if aux == 6:
      aux = 0 
    else:   
      aux += 1     
  print(f"sera entregue {dias_semana[aux]}")