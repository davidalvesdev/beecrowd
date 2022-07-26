a,b,c = input().split()
a =  float(a)
b = float(b)
c = float(c)

#a
triangulo = (a * c) / 2

#b
circulo = 3.14159 * c ** 2

#c
trapezio = ((a+b)*c)/2

#d
quadrado = b * b

#e
retangulo = a * b

print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")