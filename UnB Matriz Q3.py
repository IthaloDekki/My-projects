linha, coluna = [int(x) for x in input().split()]
matriz = [[0]*coluna for x in range(linha)]

num = int(input())# numero de bombas 

for i in range(num):
    bomba = [int(x) for x in input().split()] # x,y
    for j in range(coluna):
        matriz[bomba[0]-1[j]] += 1
        
    for z in range(linha):
        if z == bomba[0]-1:
            pass
        else:
            matriz[z][bomba[1]-1] += 1
            
count = 0 
for i in range(linha):
    count += matriz[i].count(max(max(matriz)))
print(count)