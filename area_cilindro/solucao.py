#UFCG - PROG1
#LUCAS SANTIAGO - 14/10/2021
#MATRICULA: 120210478

print("Cálculo da Superfície de um Cilindro")
print("---")

# entrada
m_diametro = float(input("Medida do diâmetro? "))
m_altura = float(input("Medida da altura? "))
print("---")

#calculo
raio = m_diametro / 2
area_total = 2 * (3.141592 * raio * raio) + 2 * (3.141592 * raio * m_altura)
#saida
print(f"Área calculada: {area_total:.2f}")
