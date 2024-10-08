lista = []
for c in range(0, 5):
    n = int(input('\nDigite um valor: '))
    if c == 0 or n > lista[-1]: #adicionará no final da lista se for o primeiro numero / e também se for maior que o último:
        lista.append(n)
        print('adicionado no final da lista')
    else:
        pos = 0 #posição
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print('-'*30)
print(f'Os valores digitados em ordem foram: {lista}')

