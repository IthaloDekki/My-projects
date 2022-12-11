#1047 Beecrowd
hi, mi, hf, mf = map(int, input().split())
if hi < hf and mi < mf:
    horas = hf - hi 
    minutos = mf - mi
    print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')
elif mi == hi == hf == mf:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S')
elif hi == hf and mi < mf:
    minutos = mf - mi
    print(f'O JOGO DUROU 0 HORA(S) E {minutos} MINUTO(S)')
elif hi < hf and mf < mi:
    hi_minutos = hi * 60 
    hf_minutos = hf * 60 
    minuto_inicial = hi_minutos + mi 
    minuto_final = hf_minutos + mf
    sub_minutos = minuto_final - minuto_inicial
    horas = sub_minutos // 60
    minutos = sub_minutos % 60
    print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')
elif hi > hf and mi < mf:
    horas_dia1 = 24 - hi
    horas_total = horas_dia1 + hf
    minutos_total = mf - mi 
    print(f'O JOGO DUROU {horas_total} HORA(S) E {minutos_total} MINUTO(S)')
else:
    minutosdia = 24 * 60
    minutosdia1 = (hi*60) + mi 
    minutodia2 = (hf*60) + mf 
    minutos_dia_res = minutosdia - minutosdia1
    tempo_total_minutos = minutos_dia_res + minutodia2
    #convertendo o tempo total para horas e minutos 
    horas = tempo_total_minutos // 60
    minutos =tempo_total_minutos % 60 
    print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')