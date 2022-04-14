#entrada
graus = int(input())
minutos = int(input())
segundos = int(input())


#calculo
conver_m_h = minutos / 60
conver_s_h = segundos / 3600
total = graus + conver_m_h + conver_s_h


#saida
print(f"graus = {total:.4f}")
