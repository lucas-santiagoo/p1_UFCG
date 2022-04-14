#UFCG - PROG1
#LUCAS SANTIAGO - 14/10/2021
#MATRICULA: 120210478

cap_revestimento = float(input("Capacidade de revestimento? "))
print()
print("== Dados do vão a revestir ==")

compr = float(input("Comprimento? " ))
larg = float(input("Largura? " ))
altu = float(input("Altura? " ))
print()
print("== Resultados ==")


#calculo
area_cubo = (2 * compr * larg) + (2 * larg * altu) + (2 * compr)
total = area_cubo / cap_revestimento
print(f"Área total a revestir: {area_cubo:.1f} m2") 
print(f"Número de caixas: {total:.0f}")
