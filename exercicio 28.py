from random import randint
# função random retorna um número decimal aleatório 
# randint retorna um número inteiro de 'inicio' até 'fim' ex.: randint(1,10)
computador = randint(0, 5) # Faz o computador "Pensar"
print('-=-' * 20 )
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei ?'))

if jogador == computador :
    print('Parabéns! Você conseguiu me vencer!')
else:
    print(f'Ganhei! Eu pensei no número {computador} e não no {jogador}')
    