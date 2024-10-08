listanum = []
while True:
    n = int(input('Digite um número: '))
    if n not in listanum:
        listanum.append(n)
        print('Número adicionado com sucesso!')
    else:
        print('Esse número já foi cadastrado!')
    continuar = str(input('Deseja continuar? Sim ou Não: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Digite apenas Sim ou Não: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Os números digitados foram: {sorted(listanum)}')