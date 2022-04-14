#entrada
salario = float(input())

#calculo
inss_empregador = (salario * 0.12)

empregado_8 = (salario * 0.08)
empregado_9 = (salario * 0.09)
empregado_11 = (salario * 0.11)

print(f"O valor da contribuição do INSS a ser pago pelo empregador é de R$ {inss_empregador:.2f}")

#condições
if salario <= 1317.07:
    print(f"O valor da contribuição do INSS a ser pago pelo empregado é de R$ {empregado_8:.2f}")

elif salario >= 1317.08 and salario <= 2195.12:
    print(f"O valor da contribuição do INSS a ser pago pelo empregado é de R$ {empregado_9:.2f}")

elif salario > 2195.12:
    print(f"O valor da contribuição do INSS a ser pago pelo empregado é de R$ {empregado_11:.2f}")
