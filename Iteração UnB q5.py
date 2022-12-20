N = int(input())
contador = 0
media = 0
maior_salario = 0
menor_salario = 0
menor_nome = ''
maior_nome = ''
while N != 0:
    nome, num = input().split(',')
    N -= 1
    num = float(num)
    media += num
    contador += 1
    if num > maior_salario:
        maior_salario = num
        maior_nome = nome
    if num < menor_salario or menor_salario == 0:
        menor_salario = num
        menor_nome = nome
if contador == 0:
    print('Não tem média')
else:
    print(f'{(media/contador):.2f}')
if maior_salario == 0:
    print('Não tem')
else:
    print(f'{maior_nome} {maior_salario:.2f}')
if menor_salario == 0:
    print('Não tem')
else:
    print(f'{menor_nome} {menor_salario}')







