jogador = {}
time = []
gols_partidas = []

while True:
    jogador.clear()
    gols_partidas.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize().strip()
    num_partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou: '))
    for c in range(1, num_partidas + 1):
        gols_partidas.append(int(input(f'Quantos gols ele fez na partida {c}: ')))
    jogador['gols'] = gols_partidas[:]
    jogador['total'] = sum(gols_partidas)
    time.append(jogador.copy())
    while True:
        continuar = str(input('Deseja acrescentar mais jogadores - Sim ou Não: ')).upper().strip()[0]
        if continuar in 'SN':
            break
        print('Erro! Digite apenas Sim ou Não')
    if continuar == 'N':
        break
print('-'*50)
print(f'{"CÓD"}', end='')
for i in jogador.keys(): #imprimirá o nome de cada chave: nome/gols/total
    print(f'{i.upper():^15}', end='') # o .upper imprimirá tudo maisculo
print()
for k, v in enumerate(time): #aqui o K nao representa key/chave, no enumerate, o k representa o indice, e o V representa o valor desse indice
    #o k começa com o indice 0 na lista
    #o V representa o dicionario inteiro do jogador, com key e value.
    print(f'{k+1:^4}', end='')
    for d in v.values(): #aqui se quer imprimir apenas os values do dicionario, entao coloca-se V.VALUES, pois assim não imprimirá o nome da key(nome, gols, total)
        print(f'{str(d):^15}', end='') # str(d) converte o valor de d em uma string, p/ garantir que qualquer tipo de dado, inclusive números, possa ser printada formatado corretamente
    print()
print('-'*50)
while True:
    busca = int(input('Qual jogador você quer ver os dados? (digite 999 p/ SAIR)'))
    if busca == 999:
        break
    if busca <= 0 or busca > len(time):
        print(f'Erro. Não existe jogador com o codigo: {busca}')
    else:
        jogador_escolhido = time[busca - 1] #corrige o índice, pois acima acrescentamos +1 para o CÓD não começar em 0
        print(f'--- Levantamento de dados --- {jogador_escolhido["nome"]}:'.center(50))
        for i, g in enumerate(jogador_escolhido['gols']):
            print(f'O jogador fez no jogo {i+1} -> {g} gols.')
    print('-'*50)
print(f'{"ENCERRADO"}'.center(50, '-'))