divida = int(input())
mensalidade = int(input())
continua = True
contador = 0

while True:
  
  if divida > 0 :
    
    contador +=1
    print(f"pagamento: {contador}")
    print(f"antes = {divida}")
    divida -= mensalidade
    if divida < 0 :
      divida=0
      print(f"depois = {divida}")
      print("-----")
      break
    print(f"depois = {divida}")
    print("-----")
  
  else:
    break