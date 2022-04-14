# Computação - UFCG
# Programação 1 - 2021.1e
# <Lucas Santiago> | Matrícula: <120210478>
# <Encontra elementos>
# Descrição< Escreva a função encontra_menores(num, lista) que receba um número inteiro e uma lista de
#inteiros. A função deve retornar o primeiro valor da lista que seja menor que o número ou -1, se
#não houver valor que atenda à condição.>

def encontra_menores(num, lista):
  for numeros in lista:
    if int(numeros) < num:
      return numeros

  return -1


lista1 = [100,200,300,400]
lista2 = [15, 12, 4, 9, 10]
assert encontra_menores(100, lista1) == -1
assert encontra_menores(10, lista2) == 4