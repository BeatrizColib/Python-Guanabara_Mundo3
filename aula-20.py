def titulo(txt):
    print('-'*50)
    print(txt)
    print('-'*50)

#Programa Principal
titulo('Hello, world!')
titulo('Me chamo Bia, prazer')

#######################################################################
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b #a e b são parâmetros
    print(f'A soma de A+B = {s}')
    print('-'*50)
#entre a def e o programa principal, deve-se ter 2 linhas no mínimo


#Programa Principal
soma(9, 2)
soma(82, 96)
soma(87, 2)
soma(b=5, a=10)  #escreveu mudando a ordem, mas ele entende
#######################################################################
#o *num significa que ele irá receber vários parâmetros/números, pode ser 1 ou quantos mais...
def contador(*num):
    for n in num:
        print(f'{n} ', end='')
    tam = len(num)
    print(f'- No total são {tam} números - ', end='')
    print('FIM!')
#exemplo de desempacotamento, *num - irá desempacotar valores

contador(2, 5, 6) #ele criará uma tupla com os números digitados
contador(1, 8)
contador(34,5, 67, 4, 2)
print('-'*50)
##########################################################################
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2  #dobrando o valor do número em cada posição
        pos +=1
#aqui não é um exemplo de desempacotamento, aqui usa-se listas

valores = [4, 5, 7, 3, 2]
dobra(valores)
print(valores)
print('-'*50)
###########################################################################
def somavarios(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Os valores: {valores} somados é igual a: {s}')
#exemplo de desempacotamento *valores


somavarios(4, 5, 6)
somavarios(1, 5)
somavarios(34, 5, 67, 6, 12, 34)
print('-'*50)



