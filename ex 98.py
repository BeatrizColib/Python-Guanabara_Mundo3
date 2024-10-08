def contador(inicio, fim, passo):
    from time import sleep
    print('-'*40)
    print('Contagem de 1 até 10 de 1 em 1:')
    for c in range(1, 10 +1, 1):
        print(c, end=' ')
        sleep(0.2)
    print('Fim!')
    print('-'*40)
    print('Contagem de 10 até 0 de 2 em 2:')
    for c in range(10, -1, -2):
        print(c, end=' ')
        sleep(0.2)
    print('Fim!')
    print('-'*40)
    print('Agora é a sua vez de personalizar a contagem!')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    if inicio < fim:
        if passo == 0:
            passo = 1
        for c in range(inicio, fim + 1, passo):
            print(c, end=' ')
    else:
        if passo == 0:
            passo = -1
        fim += passo
        for c in range(inicio, fim +1, passo):
            print(c, end=' ')
    print('Fim')
    print('')


contador(0, 0, 0)

