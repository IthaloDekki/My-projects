programa = input('O programa funciona?\n')
if programa == 'SIM':
    programa = input('Você entende o que fez?\n')
    if programa == 'SIM':
        print('Ótimo. Então não mexe!')
    else:
        programa = input('Já foi na tutoria?\n')
        if programa == 'SIM':
            print('Choremos!\n')
        else:
            print('Temos um time a disposição!\n')

else:
    programa = input('Você sabe onde está o erro?\n')
    if programa == 'SIM':
        programa = input('Acha que pode solucionar sozinho?\n')
        if programa == 'SIM':
            print('Então mão na massa!')
        else:
            programa = input('Já pesquisou no Google?\n')
            if programa == 'SIM':
                programa = input('Já foi na tutoria?\n')
                if programa == 'SIM':
                    print('Choremos!\n')
                else:
                    print('Temos um time a disposição!\n')

            else:
                print('Corre lá então!')
    else:
        programa = input('Já foi na tutoria?\n')
        if programa == 'SIM':
            print('Choremos!\n')
        else:
            print('Temos um time a disposição!\n')
