alunos = []
while True:
    nome = str(input('Nome: ')).title().strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media]) #aqui ele já jogou uma lista feita com cada aluno para dentro da lista geral
    resp = str(input('Deseja continuar? S ou N: ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('Digite apenas S ou N: ')).upper().strip()[0]
    if resp == 'N':
        break
print('-'*30)
print(f'{"Cód":<4}{"Nome":<10}{"Média":>8}')
print('-'*30)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*30)
    cod = int(input('Digite o código de qual aluno quer ver as notas (999 - interrompe): '))
    if cod == 999:
        break
    if cod <= len(alunos) - 1:
        print(f'As notas de {alunos[cod][0]} são: {alunos[cod][1]}')
    elif cod > len(alunos):
        print(f'Não há esse aluno. Total de alunos: {len(alunos)}')
print(f'{"ENCERRADO":-^30}')