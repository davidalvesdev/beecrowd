cont = 0
soma = 0
while True:
    numero = int(input())
    if numero >= 0:
        cont +=1 
        soma = numero + soma
    else:
        break
media = soma / cont
print(f'{media:.2f}')