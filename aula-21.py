#interactive help
#docstrings
#argumentos opcionais
#escopo de variáveis
#retorno de resultados

############ INTERACTIVE HELP
print('Interactive help'.center(50,'-'))
#pode ser no console ou aqui colocando help(print) help(nomedocomando)
help(print)
#mostra os parametros de uma função - parecido com o help
print(input.__doc__)
print()

######### DOCSTRINGS
print('Docstrings'.center(50, '-'))
def contador(i, f, p):
    """
    -Faz uma contagem e mostra na tela
    :param i: início da contagem  #eu que digitei essas partes
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Bia
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')


contador(2, 10, 2)
help(contador) #aqui ele mostrará o docstrings que eu criei
print()

########## PARÂMETROS OPCIONAIS
print('Parâmetros opcionais'.center(50,'-'))
def somar(a,b,c=0):
    #o c=0 é um parâmetro opcional, que caso sejam digitados apenas dois valores, o c assumirá valor 0.
    #poderia ser tambem somar(a=0, b=0, c=0)
    s = a+b+c
    print(f'A soma vale {s}')


somar(1,5,6) #ele somará todos
somar(4,7) #se eu nao colocar o parâmetro opcional, ele dará erro.
print()

########  ESCOPO DE VARIÁVEIS: global x local
print('Escopo de variáveis - global e local'.center(50,'-'))
def teste3(b):
    a = 8  #escopo local, só funciona dentro da função
    b += 4 #idem
    c = 2 #idem
    print(f'A dentro vale {a}') #aqui printará a como = 8
    print(f'B dentro vale {b}') #printará b como = 9
    print(f'C dentro vale {c}') #printará c como = 2


a = 5  #esse a tem escopo global e dessa forma, temos duas variáveis a (uma com escopo local e outra global)
teste3(a)
print(f'A fora vale {a}') #aqui printará 5
#print(f'B fora vale {b}') #aqui dará erro, pois B e C não tem escopo global e nao funciona aqui
#print(f'C fora vale {c}')  #idem
print()


#porém, se eu quiser que o a de fora assuma o a de dentro, eu escrevo assim:
print(f'com global dentro da função'.center(50,'-'))
def teste4(b1):
    global a1
    a1 = 8
    b1 += 2
    c1 = 2
    print(f'A dentro vale {a1}') #aqui printará a como = 8
    print(f'B dentro vale {b1}') #printará b como = 9
    print(f'C dentro vale {c1}') #printará c como = 2


a1 = 5  #esse a será substituído pelo a da função pq assumiu o escopo de global
teste4(a1)
print(f'A fora vale {a1}') #aqui printará 8, pois assumirá o valor de dentro da função para a1, que é o novo global
#print(f'B fora vale {b1}') #aqui dará erro, pois B e C não tem escopo global e nao funciona aqui
#print(f'C fora vale {c1}')  #idem
print()

############ RETORNO DE VALORES
print('RETORNO DE VALORES'.center(50, '-'))
def somar2(a=0,b=0,c=0):
    s = a +b +c
    print(f'soma vale {s}')


somar2(2,3,5)
somar2(10,7)
somar2(8)                   #essa forma é ineficiente para formatar resultados.
print()

#é melhor fazer assim com return
print('melhor com return: ')
def somar3(a=0,b=0,c=0):  #assim é melhor
    s = a + b + c
    return s

#posso declarar uma variável, ou simplesmente colocar dentro do print(somar3(5,8,10)) e posso formatar
r1 = somar3(2,4,6)
r2 = somar3(5,6)
r3 = somar3(7)
print(f'Os resultados foram: {r1}, {r2}, {r3}')
print()