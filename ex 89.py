lista = []
aluno = ['', [0, 0, 0]]
media = cont = 0
while True:
    nome = str(input('Nome: ')).title().strip()
    aluno[0] = nome
    nota1 = float(input('Nota 1: '))
    aluno[1][0] = nota1
    nota2 = float(input('Nota 2: '))
    aluno[1][1] = nota2
    media = (nota1 + nota2) / 2
    aluno[1][2] = media
    lista.append(aluno[:])
    aluno.clear()
    cont += 1
    aluno = ['', [0, 0, 0]]
    continuar = str(input('Deseja continuar? [S] ou [N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Digite apenas [S] ou [N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(lista)
print('='*40)
print(f'{"BOLETIM":^40}')
print('='*40)
print(f'{"Cód     Aluno     Média":^20}')
for c, aluno in enumerate(lista, start=1):
    print(f'{c:<5} {aluno[0]:^10}  {aluno[1][2]:>5.2f}')
resp = 0
while resp != 999:
    for c, aluno in enumerate(lista, start=1):
        resp = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
        print(f'As notas do/a {aluno[0]} são {aluno[1][0]} e {aluno[1][1]}')
    if resp == 999:
        break