# 1045 Beecrowd
x, y = map(int, input().split())
if x < y:
    print(f'O JOGO DUROU {y - x} HORA(S)')
elif x == y:
    print(f'O JOGO DUROU 24 HORA(S)') 
else:
    dia1 = 24 - x
    tempo = dia1 + y
    print(f'O JOGO DUROU {tempo} HORA(S)')