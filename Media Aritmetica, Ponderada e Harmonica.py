x ,y ,z = map(float, input().split())
media = input()
if media == 'P':
    px, py, pz = map(int, input().split())
    formula_p = ((x * px) + (y * py) + (z * pz))/ (px + py + pz)
    print('Ponderada')
    print(f'{formula_p:,.2f}')
elif media == 'A':
    formula_a = (x + y + z)/3
    print('Aritmetica')
    print(f'{formula_a:,.2f}')
elif media == 'H':
    formula_h = 3/((1/x) + (1/y) + (1/z))
    print('Harmonica')
    print(f'{formula_h:,.2f}')
else:
    print('Operacao inexistente')