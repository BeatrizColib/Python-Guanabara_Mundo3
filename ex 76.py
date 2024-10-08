produtos = ('Lápis', 2.50, 'Caneta', 4.70, 'Borracha', 1.20, 'Caderno', 15.70, 'fichário', 35.9, 'Calculadora', 8.90, 'Resma', 33.8, 'Régua', 5.9)
print('-'*38)
print(f'\033[7:35m{"Listagem de Preços":^38}\033[m')
print('-'*38)
for pos in range(0, len(produtos)):
    if pos % 2 ==0:
        print(f'{produtos[pos]:_<30}', end='')
    else:
        print(f'R$ {produtos[pos]:>5.2f}')
print('-'*38)