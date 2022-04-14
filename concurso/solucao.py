#entrada1
primeira_nota = float(input())
segunda_nota = float(input())
terceira_nota = float(input())
idade = int(input())

escrita = primeira_nota * 0.30
didatica = segunda_nota * 0.40
titulacao = terceira_nota * 0.30 

total_nota = escrita + didatica + titulacao
####################################################

#entrada2
primeira_nota2 = float(input())
segunda_nota2 = float(input())
terceira_nota2 = float(input())
idade2 = int(input())

escrita2 = primeira_nota2 * 0.30
didatica2 = segunda_nota2 * 0.40
titulacao2 = terceira_nota2 * 0.30

total_nota2 = escrita2 + didatica2 + titulacao2

#condições

if total_nota > total_nota2:
    print(f"O primeiro candidato foi aprovado com média {total_nota:.1f}.")

elif total_nota < total_nota2:
    print(f"O segundo candidato foi aprovado com média {total_nota2:.1f}.")

elif total_nota == total_nota2 and idade > idade2:
    print(f"O primeiro candidato foi aprovado com média {total_nota:.1f}.")

elif total_nota == total_nota2 and idade < idade2:
     print(f"O segundo candidato foi aprovado com média {total_nota2:.1f}.")

elif total_nota == total_nota2 and idade == idade2:
    print(f"Empate.")



