print("Análise da Turma")
print("===")

aprovados = int(input("Número de aprovados? "))
reprovados = int(input("Número de reprovados? "))
print("---") 
total = aprovados + reprovados
porc_apro = aprovados * 100 / total
porc_repro = reprovados * 100 / total

print(f"Total de alunos na turma: {total}")
print(f"Aprovados: {aprovados} = {porc_apro:.1f}%")
print(f"Reprovados: {reprovados} = {porc_repro:.1f}%")
