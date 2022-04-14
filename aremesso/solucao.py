#entrada
record = float(input())
distancia = float(input())


# condições
if record > distancia:
    print("recorde mantido")

elif record < distancia:
    print(f"recorde quebrado ({distancia}m)")

elif record == distancia:
    print("recorde empatado")
