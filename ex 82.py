numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar: Sim ou Não: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Digite apenas Sim ou Nao: ')).upper().strip()[0]
    if continuar == 'N':
        break
print('-'*40)
print(f'Os números digitados foram: {numeros}')
pares = []
impares = []
for n in numeros: #poderia ser: for i, n in enumerate(numeros):
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'Números pares digitados: {pares}')
print(f'Números ímpares digitados: {impares}')
