jogador = {}
jogador['nome'] = str(input('Nome: ')).title().strip()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
gols = []
totalgols = 0
for c in range(1, partidas +1):
    gol = int(input(f'   - Quantos gols fez na partida {c}: '))
    gols.append(gol)
    totalgols += gol
jogador['gols'] = gols
jogador['total de gols'] = totalgols
print('__'*20)
print(jogador)
print('__'*20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('__'*20)
print(f'O jogador {jogador['nome']} jogou {partidas} partidas.')
for pos, v in enumerate(gols):
    print(f'Na partida {pos+1}, fez {v} gols.')
print(f'O jogador {jogador['nome']} fez um total de {totalgols} gols.')