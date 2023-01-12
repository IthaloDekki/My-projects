num = 1
media = 0
max = 0
max_nome = ''
min_nome = ''
genero = ""
count = 0
for i in range(1,5):
    print(f'----- {num}ª PESSOA -----')
    nome = str(input('Nome: ')).capitalize()
    idade = int(input('Idade: '))
    sexo =  str(input('Sexo [M/F]: ')).upper()
    num += 1
    media = idade + media 
    
    if sexo == "M" and idade > max:
        max_nome = nome
        max = idade
        if sexo == "M":
            genero = 'O homem'
    elif sexo == "F" and idade > max:
        max_nome = nome
        max = idade
        if sexo == "F":
            genero = 'A mulher'
    
    if sexo == 'F'and idade < 20:
        count += 1

print(f'A média de idade do grupo é de {media/4} anos')
print(f'{genero} mais velho(a) tem {max} anos e se chama {max_nome}.')
print(f'Ao todo são {count} mulheres com menos de 20 anos.')