
# Computação - UFCG
# Programação 1 - 2021.1e
# <Lucas Santiago> | Matrícula: <120210478>
# <Soma Intervalo>
#Descrição <Escreva uma função soma_intervalo(a, b) que recebe dois números inteiros, a e b, a <= b, e retorna a soma dos inteiros entre a e b, inclusive. Você não deve usar a função sum().>

def soma_intervalo(a, b):
    num = 0
    for i in range(a,b + 1):
        num += i
    return num

assert soma_intervalo(5,15) == 110
assert soma_intervalo(10,10) == 10