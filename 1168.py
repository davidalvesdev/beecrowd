inicio = int(input()) 
fim = int(input())
primos = 0

# executa o laço do número inicial 
# até o final
for numero in range(inicio,fim+1,1):
  divisoes = 0
  cont = 1

  # para cada número posicionado, 
  # executa laço de 1 até ele mesmo, 
  # para verificar a quantidade de 
  # divisores  entre 1 e ele mesmo.
  while cont <= numero:

    #verifica se o número é divisível pelo contador, de 1 ao contador cont
    if numero % cont == 0 and numero != 1:
      divisoes +=1
    cont +=1

  # caso tenha apenas 2 divisores, 
  # marca numero como primo  
  if divisoes == 2:
    print(f"{numero}")
    primos +=1  

print(f"primos: {primos}")