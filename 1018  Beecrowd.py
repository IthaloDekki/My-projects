n = int(input())
nota100 = n // 100
resto100 = n % 100
nota50 = resto100 // 50
resto50 = resto100 % 50
nota20 = resto50 // 20
resto20 = resto50 % 20
nota10 = resto20 // 10
resto10 = resto20 % 10
nota5 = resto10 // 5
resto5 = resto10 % 5
nota2 = resto5 // 2
resto2 = resto5 % 2
nota1 = resto2 // 1

print(n)
print(f'{nota100} nota(s) de R$ 100,00')
print(f'{nota50} nota(s) de R$ 50,00') 
print(f'{nota20} nota(s) de R$ 20,00')
print(f'{nota10} nota(s) de R$ 10,00')
print(f'{nota5} nota(s) de R$ 5,00')
print(f'{nota2} nota(s) de R$ 2,00')
print(f'{nota1} nota(s) de R$ 1,00')
