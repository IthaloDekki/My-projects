#Beecrowd 1038
#Lista  de preço
x, y = map(int, input().split())
if x == 1:
    preco = float(4.0 * y)
elif x == 2:
    preco = float(4.50 * y)
elif x == 3:
    preco = float(5.00 * y)
elif x == 4:
    preco = float(2.00 * y)
elif x == 5:
    preco = float(1.50 * y)
print(f'Total: R$ {preco:.2f}')
