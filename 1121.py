preco = float(input())
quantidade = int(input())
desconto = (10 + quantidade) / 100 #passando para percentual

preco_real = quantidade * preco
preco_desconto = preco_real * ( 1 - desconto )

print(f"{preco_real:.2f}")
print(f"{preco_desconto:.2f}")