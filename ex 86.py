matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0,3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'digite um número [{linha}, {coluna}]: '))
print('*'*50)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'{matriz[linha][coluna]:^5}', end='')  #:^5 é para centralizar os numeros em até 5 casas
    print() #este print é para dar parágrafo a cada final de linha, criando assim, três linhas para a matriz
