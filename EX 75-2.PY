valores = tuple(int(input('Digite valores '))for c in range(1, 5)) #irá pedir 4x o num para o usuario e formará a tupla
print(f'Você digitou os números: {valores}')
print(f'O número 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O primeiro 3 apareceu na {valores.index(3)+1}ª posição')
else:
    print('O número 3 não foi digitado nenhuma vez.')
pares_encontrados = False
for n in valores:
    if n % 2 == 0:
        pares_encontrados = True
    else:
        pares_encontrados = False
if pares_encontrados == True:
    print('Os pares encontrados foram: ', end='')
    for n in valores:
        if n % 2 ==0:
            print(f'{n} ', end='')
else:
    print('Nenhum valor par foi digitado.')