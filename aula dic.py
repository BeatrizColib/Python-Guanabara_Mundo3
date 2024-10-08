aluno = dict()
lista_alunos = list()

while True:
    alunos.clear()
    alunos['Nome'] = str(input('Qual nome do aluno? ')).capitalize().strip()
    alunos['Idade'] = int(input('Qual sua idade? '))
    while True:
        alunos['Sexo:'] = str(input('Qual sexo: Feminino (F) ou masculino (M)? ')).capitalize().strip()
        if alunos in 'FM':
            break
        print('Erro! Digite apenas Feminino ou Masculino')
    alunos['Curso:'] = str(input('Qual seu curso? '))
    lista_alunos.append(aluno.copy())

