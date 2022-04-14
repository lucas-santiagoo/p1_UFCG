#UFCG - PROG1
#LUCAS SANTIAGO - 15/10/2021
#MATRICULA: 120210478
ano = int(input())

if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print(f"{ano} é bissexto")
else : 
    print(f"{ano} não é bissexto")


