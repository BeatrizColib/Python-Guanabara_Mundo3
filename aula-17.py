#Listas - mutáveis e entre []

lanche.append('cookie') #adiciona no final da lista
lanche.insert(0,'pão') #adiciona no indice 0 o item 'pao'

del lanche[3] #apaga o item da posição 3
lanche.pop(3) #normalmente usado para apagar o ultimo elemento, mas pode-se dizer o indice
lanche.remove('pizza') #remove pelo conteudo. Elimina o elemento e redefine os elementos restantes

if 'pizza' in lanche:   #metodo para verificar se existe pizza, e caso sim, elimina-la
    lanche.remove('pizza')

valores = list(range(4,11)) #cria uma lista do 4 ao 10, ultimo elemento nao é contabilizado
valores = list(range(0,20,2)) #criará do 0 ao 19, pulando de 2 em 2

valores.sort() #ordena a lista em ordem crescente
valores.sort(reverse=True) #ordena em ordem decrescente
len(valores) #dirá o tamanho dos valores.

