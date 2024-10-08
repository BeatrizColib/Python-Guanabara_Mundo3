# outra forma: lista = list(int(input('digite um valor: '))for c in range(0,5))
lista = []
maior = menor = 0
for c in range(0,5):
    lista.append(int(input(f'digite um numero para a posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f'voce digitou: {lista}')
print()
print(f'O maior valor digitado foi {maior}, na/s posição/ões: ',end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i} -', end='')
print()
print(f'O menor valor digitado foi {menor}, na/s posição/ões: ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i} -', end='')

print()
print(maior, lista.index(maior)) #aqui ele imprime o valor maior e a posição em que apareceu primeiro
print(menor, lista.index(menor))