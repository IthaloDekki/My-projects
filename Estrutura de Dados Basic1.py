import math
qtd_buracos = int(input())
coor_coelho = list(map(float, input().split()))
coor_raposa = list(map(float, input().split()))
escape = False
max_distancia = []


def distancia1(x1, y1, x2, y2):
    a = x2 - x1
    b = y2 - y1
    c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
    return c 

def distancia2(x1, y1, x2, y2):
    a = x2 - x1
    b = y2 - y1
    c = math.sqrt(math.pow(a,2) + math.pow(b, 2))
    return c

for i in range(qtd_buracos):
    coor_buraco = list(map(float, input().split()))
    coelho_dist_buraco= distancia1(coor_buraco[0], coor_buraco[1], coor_coelho[0], coor_coelho[1])
    raposa_dist_buraco = distancia2(coor_buraco[0], coor_buraco[1], coor_raposa[0], coor_raposa[1])
    if coelho_dist_buraco < (raposa_dist_buraco / 2):
        escape = True
        break
    
if escape == True:
    print(f'O coelho pode escapar pelo buraco ({coor_buraco[0]:.3f}, {coor_buraco[1]:.3f}).')
else:
    print('O coelho nao pode escapar.')
