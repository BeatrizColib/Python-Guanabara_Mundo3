num = [2, 5, 9, 1, 2]
print(num)
num[2] = 3 #substituir na posição 2, para 3
print(num)
num.append(7) #inseriu no final da lista 7
print(num)
num.sort() #ordem crescente
print(num)
num.sort(reverse=True) #ordem decrescente
print(num)
num.insert(2, 0) #inseriu na posição 2, o numero 0
print(num)
len(num)
print(len(num)) #conta quantos elementos tem - diz o total de elementos - mas lembrar que a posição começa no 0
num.pop() #assim elimina o último elemento - diminui o tamanho da lista
print(num)
num.pop(2) #elimina o elemento do INDICE 2 - diminui o tamanho da lista
print(num)
num.remove(2) #irá eliminar O ELEMENTO 2, se tiver mais de um 2, eliminará apenas o que aparecer primeiro

if 2 in num:
    num.remove(2)
    print(num)
else:
    print('nao achei o 2.')
#####################################################
valores = [] #começar uma lista vazia / equivalente a valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores): # c de chave e v de valor
    print(f'Na posição {c + 1}, encontrei: {v}')
print('chegamos ao final')

################################################
numeros = list()
for cont in range(0,5):
    numeros.append(int(input(f'Digite o {cont + 1}º valor: ')))
for cont, n in enumerate(numeros):
    print(f'Na posição {cont + 1}ª, encontrei: {n}')
print('acabou')
########################
a = [2, 3, 4, 7]
b = a    #ao se igualar duas listas, elas se unem, o python cria uma ligação entre elas. o que alterar em B, irá mudar em A.
b[2] = 8
print(f'lista a: {a}')
print(f'lista b: {b}')
##########################
t = [2, 3, 4, 7]
z = t[:]  #aqui ele cria uma cópia, nao cria uma ligação entre as duas listas
t[2] = 8 #so em t ficará com 8
print(list(t))
print(list(z))






