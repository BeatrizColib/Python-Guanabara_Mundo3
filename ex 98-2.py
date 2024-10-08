def contador(inicio, fim, passo):
    from time import sleep
    print('-'*40)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    sleep(1.5)
    if inicio < fim:
        if passo == 0:
            passo = 1
        if passo < 0:
            passo *= -1
        for c in range(inicio, fim + 1, passo):
            sleep(0.2)
            print(c, end=' ')
    if fim < inicio:
        if passo == 0:
            passo = -1
        fim += passo
        for c in range(inicio, fim, passo):
            sleep(0.2)
            print(c, end=' ')
    print('Fim')


contador(1, 10, 1)
contador(10, 0, -2)
print('-'*40)
print('Agora é sua vez de personalizar a contagem:')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)

###############################outra forma - guanabara
'''
def contador(i, f, p):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1    
print('-'*40)
print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
sleep(1.5)

    if i < f:
        cont = 1
        while cont <= f:
            print(f'{cont} ', end=' ')
            cont += p
        print('fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end=' ')
            cont -= p    
        print('fim')
'''