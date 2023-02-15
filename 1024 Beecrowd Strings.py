from math import ceil
num = int(input())

for i in range(num):
    msg = input()
    tamanho = len(msg)
    frase = ''
    for j in msg:
        if (j.isalpha() == True):
            frase += chr(ord(j) + 3)
        else:
            frase += j
    reversao = frase[::-1]
    metade = ceil(len(reversao)/2)
    msg2 = reversao[-metade:]
    msg3 = ''
    
    for x in msg2:
        msg3 += chr(ord(x) - 1)
    saida = reversao.replace(msg2,msg3)
    print(saida)
    
        
