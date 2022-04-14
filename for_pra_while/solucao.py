# Computação - UFCG
# Programação 1 - 2021.1e
# <Lucas Santiago> | Matrícula: <120210478>
# <tabuada em while True>

fator = int(input())
num = 0
while True:
  num += 1
  produto = num * fator
  if num == 11: break
  
  print(f"{fator}  x {num}  = {produto}")