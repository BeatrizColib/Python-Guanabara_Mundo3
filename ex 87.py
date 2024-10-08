matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = somatc = maiorsl = 0
for linha in range(0,3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'digite um número [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            somapares += matriz[linha][coluna]
        if linha == 1:
            if coluna == 0:
                maiorsl = matriz[1][coluna]
            elif matriz[1][coluna] > maiorsl:
                maiorsl = matriz[1][coluna]
        if coluna == 2:
            somatc += matriz[linha][coluna]
print('*'*50)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'{matriz[linha][coluna]:^5}', end='')
    print()
print(f'A soma de todos os valores pares foi: {somapares}')
print(f'A soma dos valores da terceira coluna foi: {somatc}')
print(f'O maior valor da segunda linha foi: {maiorsl}')


#outra forma para somar os valores da terceira coluna
somatercoluna = 0
for linha in range(0, 3):
    somatercoluna += matriz[linha][2]
#outra forma de achar o maior valor da segunda linha
maiorseglinha = 0
for coluna in range(0, 3):
    if coluna == 0:
        maiorseglinha = matriz[1][0]
    elif matriz[1][coluna] > maiorseglinha:
        maiorseglinha = matriz[1][coluna]