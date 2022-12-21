dados = input().split(" ")
pop_a = int(dados[0])
pop_b = int(dados [1])
taxa_1 = float(dados [2])
taxa_2 = float(dados [3])
crescimento_a = 0
crescimento_b = 0
controle = 0 #variavel auxiliar para o controle do tempo

if taxa_1 < taxa_2:
    print('A nunca alcancara B.')
else:
    while pop_a < pop_b and controle < 1000:
        crescimento_a = int((pop_a * (taxa_1/100)))#calcula a parte inteira da nova população com o passar de um ano
        crescimento_b = int((pop_b * (taxa_2/100)))#converte pra inteiro; evitando a mensagem de erro
        pop_a += crescimento_a
        pop_b += crescimento_b
        controle += 1
    if controle >= 1000:
        print('Mais de um milenio.')
    else:
        print(f'Vai alcancar em {controle} ano(s).')