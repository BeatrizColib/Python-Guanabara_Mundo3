aluno = {}
aluno['nome'] = str(input('Nome: ')).title()
aluno['média'] = float(input('Média: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'aprovado/a'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'em recuperação'
else:
    aluno['situação'] = 'reprovado/a'
print(f'O/A aluno {aluno['nome']} tem a média {aluno['média']} e está {aluno["situação"]}.')

for k, v in aluno.items():
    print(f'{k} é {v}')