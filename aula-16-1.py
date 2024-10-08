#Tuplas - são imutáveis / entre parênteses ou sem nada

lanche = 'hambuguer','suco','pizza','pudim'
print(lanche)
print(lanche[1]) #para referenciar é com []
print(lanche[-2]) #vai voltando, do fim para o início
print(lanche[-1])
print(lanche[:2]) #sempre desconsiderar o último, ele nao será mostrado
print()

# para ele imprimir sem as aspas e virgulas,
# em separado cada item, podemos usar o for

for comida in lanche:
    print(f'eu vou comer {comida}')
print("Comi muito!")

#ou

for cont in range(0, len(lanche)): #assim ele irá contar (de 0 ate 4)
    print(lanche[cont])

for cont in range(0, len(lanche)): #assim ele irá dizer cada item, como no primeiro for
    print(f'eu vou comer {lanche[cont]} na posiçao {cont}')

#outra forma de fazer o mesmo que o for acima é:
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posiçao {pos+1}') #somei 1 para nao começar do zero

print()

print(sorted(lanche)) #mostra em ordem (seja alfabética ou numérica crescente)
#pode-se ter dados numéricos e alfabéticos dentro da mesma tupla

