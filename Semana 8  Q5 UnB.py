dicionario = {'zero': 0, 'um': 1, 'dois':2, 'três':3, 'quatro':4, 'cinco':5, 'seis':6,
'sete': 7, 'oito':8, 'nove': 9 } #dicionario para linkar a palavra por extenso ao seu valor escrito

string = input()
for i in dicionario:
    if i in string:
        string = string.replace(i, str(dicionario[i]))
print(string)
