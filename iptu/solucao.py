#UFCG - PROG1
#LUCAS SANTIAGO - 14/10/2021
#MATRICULA: 120210478

area = float(input("Área construída? "))
aliquota = float(input("Alíquota? "))

valor_sem_desconto = area * aliquota + 35

print(f"IPTU: R$ {valor_sem_desconto:.2f}")
print()
quota_unica = valor_sem_desconto - (valor_sem_desconto * 0.25)

quota_p6 = valor_sem_desconto - (valor_sem_desconto * 0.05)
p6 = quota_p6 / 6

quota_p10 = valor_sem_desconto
p10 = quota_p10 / 10


print("Pagamento:")
print(f"1. Quota única. R$ {quota_unica:.2f}")
print(f"2. Em 6 parcelas. Total: R$ {quota_p6:.2f}")
print(f"   6 x R$ {p6:.2f}")
print(f"3. Em 10 parcelas. Total: R$ {quota_p10:.2f}")
print(f"   10 x R$ {p10:.2f}")
