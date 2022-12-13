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

