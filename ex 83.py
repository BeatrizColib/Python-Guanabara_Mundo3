expressao = str(input('digite sua expressão matemática: '))
parenteses = []
for simbolo in expressao:
    if simbolo == '(':
        parenteses.append('(')
    elif simbolo == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break
if len(parenteses) == 0:
    print('sua expressão é valida')
else:
    print('expressão inválida')

#############################outra forma

exp = str(input('digite sua expressão: '))
parent = []
for simb in exp:
    if simb in '()':
        parent.append('(')
        parent.append(')')
if len(parenteses) % 2 == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão é inválida')    #porem dessa forma, ele nao faz o balanceamento de parenteses.