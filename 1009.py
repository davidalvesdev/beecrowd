vendedor = str(input())
salario = float(input())
totalvendas = float(input())

comissao = totalvendas * 0.15
total = comissao + salario

print(f"TOTAL = R$ {total:.2f}")