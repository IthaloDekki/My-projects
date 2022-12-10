lista = map(float, input().split())
lista = sorted(lista, reverse=True)#Colocando a lista de forma decrescrente
#A lista, quando os inputs são dados na  mesma linha, é criada automatica
a = lista[0]
b = lista[1]
c = lista[2]
if a >= b + c:
    print('NAO FORMA TRIANGULO')
elif a**2 == b**2 + c**2:
    print('TRIANGULO RETANGULO')
elif a**2 > b**2 + c**2:
    print('TRIANGULO OBTUSANGULO')
if a**2 < b**2 + c**2:
    print('TRIANGULO ACUTANGULO')
if a == b and a == c:
    print('TRIANGULO EQUILATERO')
elif a == b or b == c:
    print('TRIANGULO ISOSCELES')
