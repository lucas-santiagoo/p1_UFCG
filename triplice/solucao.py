#entrada

candidato_A = int(input())
candidato_B = int(input())
candidato_C = int(input())   

soma = candidato_A + candidato_B + candidato_C

#porcentagam
porcen_A = (candidato_A * 100) / soma
porcen_B = (candidato_B * 100) / soma
porcen_C = (candidato_C * 100) / soma

#saida
print(f"A: {candidato_A} ({porcen_A:.2f}%)")
print(f"B: {candidato_B} ({porcen_B:.2f}%)")
print(f"C: {candidato_C} ({porcen_C:.2f}%)")


#condições

if candidato_A > candidato_B and candidato_A > candidato_C:
    print("Mais votado: A")
    if porcen_A > 50:
        print("Segundo turno: não")
    else:
        print("Segundo turno: sim")

elif candidato_B > candidato_A and candidato_B > candidato_C:
    print("Mais votado: B")
    if porcen_B > 50:
        print("Segundo turno: não")
    else:
        print("Segundo turno: sim")

elif candidato_C > candidato_A and candidato_C > candidato_B:
    print("Mais votado: C")
    if porcen_C > 50:
        print("Segundo turno: não")
    else:
        print("Segundo turno: sim")

elif candidato_A == candidato_B or candidato_A == candidato_C:
    print("Mais votado: A")
    if porcen_A > 50:
        print("Segundo turno: não")
    else:
        print("Segundo turno: sim")

elif candidato_B == candidato_C:
    print("Mais votado: B")
    if porcen_B > 50:
        print("Segundo turno: não")
    else:
        print("Segundo turno: sim")
  




