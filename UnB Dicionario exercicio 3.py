obj_preco = input().split()
objetos = []
precos = []
dic = {}
for i in range(0, len(obj_preco), 2):
    objetos.append(obj_preco[i])
for j in range(1, len(obj_preco), 2):
    precos.append(float(obj_preco[j]))
    
for key in objetos:                 # for para criar a key da lista
    for value in precos:            # for para criar um valor para a key na lista 
        dic[key] = value            # adiciionando o value na key o dicionario 
        precos.remove(value)        # dic = {objetos[i]: precos[i] for i in range(len(obejtos))}
        break                       # forma mais elegante de resolver o problema 

aux = input().split()
escolhido = []
quantidade = []
new_dic = {}
preco_total = 0 
for n in range(0, len(aux), 2):
    escolhido.append(aux[n])
for m in range(1,len(aux), 2):
    quantidade.append(aux[m])
new_dic ={escolhido[i]: quantidade[i] for i in range(len(escolhido))}

for p in new_dic.keys():
    if p in dic:
        preco_total += dic[p] * float(new_dic[p])
print(f'R$ {preco_total:.2f}')

