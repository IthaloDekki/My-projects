from math import ceil
while True:
    try:
        n = int(input())
        matriz = [[0]* n for x in range(n)]
            
        for i in range(n):
            for j in range(n):
                if i == j:
                    matriz[i][j] = 2
                if (j + i) == (n - 1):
                    matriz[i][j] = 3
                
                tamanho = n // 2
                terço = n // 3
                if (i >= terço and i < (n - terço)) and (j >= terço and j < (n - terço)):
                    matriz[i][j] = 1
                
                
                if i == tamanho and j == tamanho:
                    matriz[i][j] = 4
        for s in range(n):
            print(*matriz[s], sep= '')
        print('')   
        
        
        
    except EOFError:
        break