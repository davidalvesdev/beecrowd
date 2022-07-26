lista = []
n = 0 
c = 0
while True:
    n = int(input())
    lista.append(n)
    c +=1
    if c == 100:
        break

print(max(lista))
posicao = max(lista)
print(lista.index(posicao) + 1)
    