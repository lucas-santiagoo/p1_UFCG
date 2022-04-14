#entrada
minuto = int(input())

#calculo
menor_minutos = 1 + (minuto * 0.50)

divisao = minuto // 5 
resto = (minuto % 5) 
total = (divisao * 3) + (resto * 0.70) + 1 

#condição

if minuto <= 3:
    print(f"R$ {menor_minutos:.2f}")

elif minuto == 4:
     print(f"R$ 3.20")

elif minuto == 5:
    print(f"R$ 3.00")

elif minuto > 5:
    print(f"R$ {total:.2F}")
