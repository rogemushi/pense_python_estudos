#2.3

horas = 6
minutos = 52
segundos = 0

horas_em_segundos = (horas * 60 ) * 60
minutos_em_segundos = minutos * 60

segundos_totais = segundos + minutos_em_segundos + horas_em_segundos
# no trecho acima se transforma o horário atual em segundos


parte_1_minutos = 8
parte_1_segundos = 15

parte_2_minutos = 7
parte_2_segundos = 12

parte_3_minutos = 8
parte_3_segundos = 15

# na parte acima se define o tempo de cada volta




tempo_final_em_segundos = segundos_totais

soma_parte_1 = (parte_1_minutos * 60)
soma_parte_1 += parte_1_segundos

soma_parte_2 = (parte_2_minutos * 60) * 3
soma_parte_2 += parte_2_segundos * 3

soma_parte_3 = (parte_3_minutos * 60)
soma_parte_3 += parte_3_segundos

#na parte acima transforma o tempo percorrido em segundos

tempo_final_em_segundos += soma_parte_1
tempo_final_em_segundos += soma_parte_2
tempo_final_em_segundos += soma_parte_3

horas_finais = (tempo_final_em_segundos // 60 ) // 60
minutos_finais = (tempo_final_em_segundos // 60 ) % 60
segundos_finais =  (tempo_final_em_segundos % 60 ) % 60
print(f"{horas_finais}:{minutos_finais}:{segundos_finais}")

# no trecho acima se faz a fatoração dos segundos para transformar em hora