n = int(input())
alunos_notas = {}
semelhantes = []
count = 0
for i in range(n):
    nome, nota = input().split(', ')
    nota = float(nota)
    alunos_notas[nome] = nota

aux = float(input())

for c, v in alunos_notas.items():
    if v == aux:
        semelhantes.append(c)
        
semelhantes.sort()


if len(semelhantes) == 0:
    print('Você foi o único aluno com essa nota.')
else:
    print(*semelhantes, sep='/')