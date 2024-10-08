pessoas = []
dados = []
maispes = maisleves = 0
while True:
    dados.append(str(input('nome: ')))
    dados.append(float(input('peso: ')))
    if len(pessoas) == 0: #ou seja, nao cadastrou ninguem ainda
        maispes = maisleves = dados[1]#que é o peso
    else:
        if dados[1] > maispes:
            maispes = dados[1]
        if dados[1] < maisleves:
            maisleves = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input('deseja continuar? [S] ou [N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Digite apenas S ou N: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Foram cadastradas {len(pessoas)} pessoa/s.') #ao mostrar o comprimento da lista, sabe-se a qnt de pessoas, nao precisa ter um contador
print(f'O maior peso foi {maispes} Kg, de: ', end=' ')
for p in pessoas:
    if p[1] == maispes:
        print(f'| {p[0]} |', end='')
print(f'\no menor peso foi {maisleves} Kg, de: ', end=' ')
for p in pessoas:
    if p[1] == maisleves:
        print(f'| {p[0]} |', end='')