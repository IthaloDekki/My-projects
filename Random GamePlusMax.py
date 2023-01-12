from random import randint
print('Sou seu computador ...')
print('Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi?')

palpite = int(input('Qual o seu palpite? '))
count = 0
tentativa = 0 
x = randint(0,10)

while count == 0:
    if palpite == x:
        print(f'Acertou em {tentativa} tentativas. Parabéns!')
        count += 1
        tentativa += 1
    elif palpite < x:
        print('Mais... Tente mais uma vez.')
        palpite = int(input('Qual é seu palpite? '))
        tentativa += 1
    else:
        print('Menos... Tente mais uma vez.')
        palpite = int(input('Qual é seu palpite? '))
        tentativa += 1