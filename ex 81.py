continuar = ''
pos = 0
numeros = []
while True:
    n = int(input('digite um numero: ')) #pode ser: numeros.append(int(input('digite: '))
    numeros.append(n)
    pos += 1
    continuar = str(input('deseja continuar: Sim ou Não: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('digite sim ou nao: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'foram digitados {pos} números.')
inversao = sorted(numeros, reverse=True)
print(f'A ordem decrescente dos números digitados é: {inversao}')
print(f'A lista na ordem de digitação foi: {numeros}')
if 5 in numeros: #o in faz buscas dentro de listas,duplas, dicionários...
    print(f'O numero 5 foi digitado na/s posição/ões: ', end=' ')
    for pos, n in enumerate(numeros):
        if n == 5:
            print(f'{pos}', end='-')
else:
    print('O numero 5 não foi digitado')