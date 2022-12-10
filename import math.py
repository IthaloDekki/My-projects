import math
a, b, c = map(float, input().split())

def verificacao():
    global a
    global b
    global c
    bc = b-c
    ac = a-c
    ba = b-a
    classe_a = (a > math.fabs(bc)) and (a < (b+c)) 
    classe_b = (b > math.fabs(ac)) and (b < (a+c))
    classe_c = (c > math.fabs(ba)) and (c < (b+a))
    #A função math.fabs calcula o valor absoluto 
    #Foi utilizado proque o resultado da subtração pode ser negativo
    #Daria pra fazer manualmente 
    if classe_a and classe_b and classe_c:
        perimetro = (a+b+c)
        print(f'Perimetro = {perimetro:.1f}')
    else:
        area_trapezio = (a+b)*c/2
        print(f'Area = {area_trapezio:.1f}')
verificacao()