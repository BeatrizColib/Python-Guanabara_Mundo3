def sort(*num):
    from random import randint
    from time import sleep
    listanum = []
    print(f'Sorteando 5 números da lista:', end=' ')
    for c in range(1, 6):
        sleep(0.3)
        num = randint(0, 10)
        listanum.append(num)
        print(f'{num}', end=' ')
    print('FIM')
    print('Somando os valores pares:', end= ' ')
    soma = 0
    for num in listanum:
        if num % 2 == 0:
            soma += num
    print(f'{listanum}, temos total de {soma}')


numeros = []
sort(numeros)

##############outra forma
def sorteia(lista):
    from random import randint
    print('Sorteando números')
    for cont in range(0, 5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n}', end=' ')
    print('Pronto!')


numeros = []
sorteia(numeros)

