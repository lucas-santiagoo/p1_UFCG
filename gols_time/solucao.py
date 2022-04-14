#PROG1 - UFCG
#Lucas Santiago
#indica qual time ganhou ou se houve empate.

gols_time_a = int(input())
gols_time_b = int(input())

if gols_time_a > gols_time_b:
    print("Time A ganhou!")
elif gols_time_b > gols_time_a:
    print("Time B ganhou!")
else:
    print("Empate!")
