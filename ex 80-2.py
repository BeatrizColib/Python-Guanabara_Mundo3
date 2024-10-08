import bisect #já insere na lista os numeros de forma ordenada
numeros = []
for c in range(0,5):
    n = int(input('digite um numero: '))
    bisect.insort(numeros, n)
    print(f'numero {n} incluido na posição {numeros.index(n)}')
print(f'numeros digitados: {numeros}')