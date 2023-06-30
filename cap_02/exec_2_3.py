#2.3

hora = 6
minuto = 52
segundo = 0

tempo_total = (hora * 60) + minuto


parte1_min = 1 * 8
parte1_seg = 1 * 15


parte2_min = 3 * 7
parte2_seg = 3 * 12


parte3_min = 1 * 8
parte3_seg = 1 * 15

segundos  =  parte1_seg + parte2_seg + parte3_seg
minutos = parte1_min + parte2_min + parte3_min
print(minutos)
print(segundos)

hora_preproc = tempo_total 
minuto_processado = segundos // 60
segundo_processado_resto = segundos % 60


hora_processado = (minutos + tempo_total) // 60
hora_processado_resto = minutos % 60

hora_final = hora_processado
minuto_final = hora_processado_resto + minuto_processado
segundo_final = segundo_processado_resto

print(f"{hora_final}:{minuto_final-8}:{segundo_final}")


