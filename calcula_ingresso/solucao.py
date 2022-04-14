#UFCG - PROG1
#LUCAS SANTIAGO - 14/10/2021
#MATRICULA: 120210478
#ingresso cinema

n_adultos = float(input())
n_criancas = float(input())
valor = float(input())

total = (valor * n_adultos + valor * n_criancas / 2)

print(f'Total: R$ {total:.2f}')


