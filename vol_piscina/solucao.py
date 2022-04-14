comprimento = float(input())
largura = float(input())
profundidade = float(input())

volume = comprimento * largura * profundidade 
vol_litros = volume * 1000
print(f"A piscina comporta {vol_litros:.2f} litros de água.")
