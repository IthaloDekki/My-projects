'''
n = int(input())
t =  int(input())
matriz = []
 
for i in range(n):
    lista = list(map(int, input().split()))
    matriz.append(lista)

matriz = sorted(matriz, key=lambda new_matriz: (new_matriz[t], sum(new_matriz)))

for item in matriz:
    print(*item)
'''
'''

qtd = int(input())
indice = int(input())
matriz = []

for i in range(qtd):
    matriz.append([int(x) for x in input().split()])
    
for i in range(qtd - 1):
    for j in range(qtd - 1 - i):
        if matriz[j][indice] > matriz[j+1][indice]:
            matriz[j], matriz[j+1] = matriz[j+1], matriz[j]
        elif matriz[j][indice] == matriz[j+1][indice]:
            if sum(matriz[j]) > sum(matriz[j+1]):
               matriz[j], matriz[j+1] = matriz[j+1], matriz[j]
               
for item in range(qtd):
    print(*matriz[item]) 
    
'''
'''
l,c = [int(i) for i in input().split()]
matriz = [[0]*c for i in range(l)]

nb = int(input()) #numero de bombas
for a in range(0,nb):
    bomba = [int(i) for i in input().split()] #(x,y)
    for b in range(c):
        matriz[bomba[0]-1][b] += 1
 
    for d in range(l): #d corresponde a linha atual do for
        if d == bomba[0]-1: # verificar se está passando pela mesma linha passada no for anterior
            pass
        else: #se não estiver na linha que já foi adicionada, adiciona.
            matriz[d][bomba[1]-1] += 1
    
    
    
cont = 0
for i in range(l):
    cont += matriz[i].count(max(max(matriz)))
print(cont)
'''

'''
n, m, f = (int(x) for x in input().split())
matriz = []

for i in range(n):
    matriz.append([int(x) for x in input().split()])
    
for i in range(0,n,f):
    out = ''
    for j in range(0,m,f):
        maior = -1
        for x in range(i,i+f):
            for y in range(j,j+f):
                maior = max(maior, matriz[x][y])
        
        out += str(maior)
        if j < m:
            out += ' '
        else:
            out +='\n'
    print(out)
''' 

'''  
lojas, mangos, minimo = [int(x) for x in input().split()]
qtd_prod = [int(x) for x in input().split()]
produtos = []
comprados = [0 for x in range(lojas)]
com_mangos = True
objetivo_completo = True
for i in range(lojas):
    produto = [int(x) for x in input().split()]
    produto.sort(reverse=True)
    produtos.append(produto)

while com_mangos and sum(qtd_prod) > 0:
    for loja in range(lojas):
        if qtd_prod[loja] > 0:
            barato = min(produtos[loja])
            if mangos - barato >= 0:
                mangos -= barato
                produtos[loja].pop()
                qtd_prod[loja] -= 1
                comprados[loja] += 1
            else:
                com_mangos = False
        
                
for produto in comprados:
    if produto < minimo:
        objetivo_completo = False

if objetivo_completo:
    print('Sim')
else:
    print('Nao')
'''