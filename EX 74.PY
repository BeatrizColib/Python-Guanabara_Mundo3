from random import randint
numeros = (randint(1, 10), randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print('Os números sorteados foram: ', end='')
for i, n in enumerate(numeros):
    if i < len(numeros)-1:
        print(f'{n}, ', end='')
    else:
        print(f'{n}.')
print(f'O maior sorteado foi {max(numeros)}')
print(f'O menor sorteado foi {min(numeros)}')