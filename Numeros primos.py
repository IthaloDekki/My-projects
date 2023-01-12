num = int(input('Digite um número: '))
count = 0
for i in range(1, num + 1):
    resto =  num % i
    if resto == 0:
        print(i, end =' ')
        count += 1
    elif resto != 0:
        print(f'[{i}]', end =' ')
print(f'\nO numero {num} foi divisivel {count} vezes', end=' ')
if count > 0:
    print('\nE por isso ele não é primo')
else:
    print('\nEle é primo')