#entrada
ano_atual = int(input("Ano atual? "))
ano_nasc = int(input("Ano de nascimento? "))



#calculo
idade = ano_atual - ano_nasc
print(f"Idade calculada: {idade}")
 
#condições
if idade >= 16 : 
    print(f"Entrada permitida")

elif idade <= 14 :
    print(f"Entrada proibida para menores de 14 anos")

elif idade > 14 and idade < 16:
    acomp = str(input("Com os pais? "))

elif acomp == "n":
    print(f"Entrada proibida para menores de 16 anos sem os pais")

else:
    print("Entrada permitida")


