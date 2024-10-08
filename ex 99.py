def maiornum(* num):
    listanum = [*num]
    listanumordem = sorted(listanum, reverse=True)
    tamlistanum = len(listanum)
    print('-' * 80)
    print(f'Os números digitados foram: {listanum}. Total de {tamlistanum} números.')
    print(f'O maior deles foi {listanumordem[0]}')
    print('FIM'.center(80, '-'))


maiornum(6, 54, 3, 6, 89, 10, 3, 1)
maiornum(5, 4, 23, 1)
maiornum(23, 300, 1, 98)

###################outra forma - guanabara
def maior(*numeros):
    cont = maior = 0
    print('-'*30)
    print('Analisando valores...')
    for n in numeros:
        print(f'{n} ', end=' ')
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print(f'Valores digitados {numeros}')
    print(f'O maior foi {maior}')


maior(6, 54, 3, 6, 89, 10, 3, 1)
maior(5, 4, 23, 1)
maior(23, 300, 1, 98)

#pode-se usar a função própria do python em que ele analisa o maior - max(listadenumeros)