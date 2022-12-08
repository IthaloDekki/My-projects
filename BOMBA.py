N = int(input())
P = int(input())
explosao = N
recorde = P
def regressiva(N):
    global recorde
    global explosao

    if N == 0:
        print('Cabum!!!! Explodiu')
    else:
        if N == 5:
            print('Seu tempo está acabando!')
            regressiva(N-1)
        elif N == 1 and explosao > recorde:
                print('Seja rápido. Falta 1 segundo')
                regressiva(N-1)
        elif N == 1 and explosao <= recorde:
                print('Bomba desativada automaticamente!')
        else:
            print(f'Atenção faltam {N} segundos...')
            regressiva(N-1)

regressiva(N)