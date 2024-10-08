usuario = {}
todos_usuarios = []
total_pessoas = 0
soma_idade = 0
media_idade = 0

while True:
    usuario['nome'] = str(input('Qual nome: ')).capitalize().strip()
    while True:
        usuario['gênero'] = str(input('Qual o gênero - Feminino ou Masculino: ')).upper().strip()[0]
        if usuario['gênero'] in 'FM':
            break
        print('Erro! Digite apenas F ou M')
    usuario['idade'] = int(input('Qual a idade: '))
    soma_idade += usuario['idade']
    total_pessoas += 1
    todos_usuarios.append(usuario.copy())
    usuario.clear()
    continuar = str(input('Deseja cadastrar outro usuário - Sim ou Não: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Erro! Digite apenas (S) ou (N): ')).upper().strip()[0]
    if continuar in 'N':
        break
print('-'*40)
print(f'1 - O total de pessoas cadastradas foi: {total_pessoas}')
media_idade = soma_idade / len(todos_usuarios)
print(f'2 - A média de idade do grupo é: {media_idade} anos.')
print(f'3 - As mulheres cadastradas foram: ')
for usuario in todos_usuarios:
    if usuario['gênero'] == 'F':
        print(f"{usuario['nome']} | ", end='')
print()
print(f'4 - Lista das pessoas acima da média da idade: ')
for usuario in todos_usuarios:
    if usuario['idade'] > media_idade:
        print(f'{usuario}')
print('-'*40)