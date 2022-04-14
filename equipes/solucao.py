somador = []
while True:
    jogador = input()
    if jogador != "-":
        somador.append(jogador)
        quantidade = len(somador)
    if jogador == "-" :
        break

if quantidade == 11:
    print("Modalidade -> Futebol")
elif quantidade == 5:
    print("Modalidade -> Basquete")
elif quantidade == 6:
    print("Modalidade -> Vôlei")
elif quantidade == 7:
    print("Modalidade -> Handebol")
else:
    print("Equipe Inválida")


