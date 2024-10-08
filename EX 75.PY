num = (int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),
       int(input('Digite um valor: ')))
print(f'Você digitou os números: {num}')
print(f'O número 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O primeiro 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O número 3 não foi digitado nenhuma vez.')
print('Os números pares foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(f'{n} ', end='')