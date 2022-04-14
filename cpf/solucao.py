#UFCG - PROG1
#LUCAS SANTIAGO - 14/10/2021
#MATRICULA: 120210478

#entrada
cpf = int(input())
cpf1 = int(input())
cpf2 = int(input())

#calculo1
valor11 = cpf // 10000000000 % 10
valor10 = cpf // 1000000000 % 10
valor9 = cpf // 100000000 % 10
valor8 = cpf // 10000000 % 10
valor7 = cpf // 1000000 % 10
valor6 = cpf // 100000 % 10
valor5 = cpf // 10000 % 10
valor4 = cpf // 1000 % 10
valor3 = cpf // 100 % 10
valor2 = cpf // 10 % 10
valor1 = cpf // 1 % 10
soma = valor1 + valor2

#calculo2
valore11 = cpf1 // 10000000000 % 10
valore10 = cpf1 // 1000000000 % 10
valore9 = cpf1 // 100000000 % 10
valore8 = cpf1 // 10000000 % 10
valore7 = cpf1 // 1000000 % 10
valore6 = cpf1 // 100000 % 10
valore5 = cpf1 // 10000 % 10
valore4 = cpf1 // 1000 % 10
valore3 = cpf1 // 100 % 10
valore2 = cpf1 // 10 % 10
valore1 = cpf1 // 1 % 10
soma2 = valore1 + valore2

#calculo3
valores11 = cpf2 // 10000000000 % 10
valores10 = cpf2 // 1000000000 % 10
valores9 = cpf2 // 100000000 % 10
valores8 = cpf2 // 10000000 % 10
valores7 = cpf2 // 1000000 % 10
valores6 = cpf2 // 100000 % 10
valores5 = cpf2 // 10000 % 10
valores4 = cpf2 // 1000 % 10
valores3 = cpf2 // 100 % 10
valores2 = cpf2 // 10 % 10
valores1 = cpf2 // 1 % 10
soma3 = valores1 + valores2


#saida
print(f"{valor11}{valor10}{valor9}{valor8}{valor7}{valor6}{valor5}{valor4}{valor3}-{valor2}{valor1}")
print(f"{soma}")

#saida2
print(f"{valore11}{valore10}{valore9}{valore8}{valore7}{valore6}{valore5}{valore4}{valore3}-{valore2}{valore1}")
print(f"{soma2}")

#saida3
print(f"{valores11}{valores10}{valores9}{valores8}{valores7}{valores6}{valores5}{valores4}{valores3}-{valores2}{valores1}")
print(f"{soma3}")

