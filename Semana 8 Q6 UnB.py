string = input()
palavra = input().split()
simbolo = '*'

for i in palavra:
    if i in string:
        string = string.replace(i, str(simbolo))
        print(string)
    else:
        print('tudo certo :)')