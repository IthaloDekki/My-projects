n = float(input())
inteiro = n // 1 
resto = (n % 1) * 100

# Transformei o numero em float em inteiro para
#conseguir fazer o calculo sem problemas

nota100 = inteiro // 100
resto100 = inteiro % 100
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

print('NOTAS:')
print(f'{nota100:.0f} nota(s) de R$ 100.00')
print(f'{nota50:.0f} nota(s) de R$ 50.00') 
print(f'{nota20:.0f} nota(s) de R$ 20.00')
print(f'{nota10:.0f} nota(s) de R$ 10.00')
print(f'{nota5:.0f} nota(s) de R$ 5.00')
print(f'{nota2:.0f} nota(s) de R$ 2.00')

print('MOEDAS:')
m1 = resto2 
m50 = resto // 50
restom50 = resto % 50
m25 = restom50 // 25
restom25 = restom50 % 25
m10 = restom25 // 10
restom10 = restom25 % 10 
m5 = restom10 // 5
restom5 = restom10 % 5
m01 = restom5 

print(f'{m1:.0f} moeda(s) de R$ 1.00')
print(f'{m50:.0f} moeda(s) de R$ 0.50')
print(f'{m25:.0f} moeda(s) de R$ 0.25')
print(f'{m10:.0f} moeda(s) de R$ 0.10')
print(f'{m5:.0f} moeda(s) de R$ 0.05')
print(f'{m01:.0f} moeda(s) de R$ 0.01')
