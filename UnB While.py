# UnB while 
count = 0
media = 0
while True:
    nome, num = input().split(',')
    if nome == "Fim":
        break
    num = float(num)
    media += num 
    count += 1
if count == 0 :
    print('0.00')
else:
    print(f'{(media/count):.2f}')

    
    
 # UnB Maior salario(While)

maior_valor = 0

while True:
    nome, num = input().split(',')
    if nome == "Fim":
        break
    num = float(num)
    if num > maior_valor:
        maior_valor = num 
if maior_valor == 0:
    print('Não tem')
else:
    print(f'{maior_valor:.2f}')
    
    
    
#UnB Menor salario(While)

menor_valor = 0 
menor_nome = ''

while True:
    nome, num = input().split(',')
    if nome == 'Fim':
        break 
    num = float(num)
    if num < menor_valor or menor_valor == 0:
        menor_nome = nome
        menor_valor = num
if menor_valor == 0:
    print('Não tem')
else:
    print(menor_nome)

