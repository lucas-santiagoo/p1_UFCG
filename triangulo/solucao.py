#UFCG - PROG1
#LUCAS SANTIAGO - 15/10/2021
#MATRICULA: 120210478

#entrada

a = int(input())
b = int(input())
c = int(input())

# calculo
sub1 = b - c
soma1 = b + c

sub2 = a - c 
soma2 = a + c

sub3 = a - b
soma3 = a + b

soma_total = a + b + c

#condições 
if sub1 < a < soma1 or sub2 < b < soma2 or sub3 < c < soma3:
    print(f"triangulo valido. {soma_total}")
else:
    print(f"triangulo invalido.")
