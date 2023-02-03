# A = algarismo mais significativo
# M = multiplicador 
# T = tolerancia
def IEC60062(resistencia):
    lista = []
    A = {'0':'Preta', '1':'Marrom', '2':'Vermelha', '3':'Laranja', '4':'Amarela', '5':'Verde'
        ,'6':'Azul', '7':'Violeta', '8':'Cinza', '9':'Branca'}
    
    M = {-3: 'Rosa', -2:'Prata', -1:'Dourada', 0:'Preta', 1:'Marrom', 2:'Vermelha', 3:'Laranja',
        4:'Amarela', 5:'Verde', 6:'Azul', 7:'Violeta', 8:'Cinza', 9:'Branca'}
    
    T = {'20':'Nenhuma', '10':'Prata', '5':'Dourada', '1':'Marrom', '2':'Vermelha', '0.05':'Laranja', '0.02':'Amarela', '0.5':'Verde', 
        '0.25':'Azul', '0.1':'Violeta', '0.01':'Cinza'}
    
    R = {'-':0, 'm':-3, 'K':3, 'M':6, 'G':9}
    
    dados = resistencia.split()
    tol = dados[1]
    mul =  dados[0][-1]
    numero = dados[0]
    numero = numero[:-1]
    if numero.count('.') != 0:    
        casa_decimal = len(numero) - numero.find('.') -1
    elif numero.count('.') == 0:
        casa_decimal = 0
    
    if len(numero) == 1:
        numero = int(numero)
        calculo = numero * 10 
        valor_mul = R[mul] -1 
        for i in str(calculo):
            if i in A:
                lista.append(A[i])
        
        if valor_mul in M:
            lista.append(M[valor_mul])
    else:   
        for i in numero:
            if i in A:
                lista.append(A[i])
        
        for s in mul:
            if s in R:
                new_mul = R[s] - casa_decimal
                lista.append(M[new_mul])
         
    if tol in T:
        lista.append(T[tol])

    return lista
print(IEC60062('1- 10'))



    


