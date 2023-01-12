primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
x = False

while not x:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        valor = primeiro + segundo
        print(valor)
        x = True
    elif opcao == 2:
        valor = primeiro * segundo
        print(valor)
        x = True
    elif opcao == 3:
        valor = primeiro - segundo 
        if valor < 0:
            print(segundo)
        elif valor > 0:
            print(primeiro)
        x = True
    elif opcao == 4:
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
    else:
        print('Exit')
        x = True