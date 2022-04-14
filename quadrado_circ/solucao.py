import math

tamanho_lado = float(input())

raio = (tamanho_lado * (2 ** 0.5)) / 2
perimetro = 2 * math.pi * raio
area = math.pi * (raio ** 2)

print(f"Perímetro: {perimetro:.5f}")
print(f"Área: {area:.5f}")
