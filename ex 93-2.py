jogador = {}
gols = []
jogador['nome'] = str(input('Nome: ')).title().strip()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for c in range(1, partidas +1):
    gols.append(int(input(f'   - Quantos gols fez na partida {c}: ')))
jogador['gols do jogador'] = gols[:] #aqui ele joga pra o final do dicionario a chave/key 'gols' com valor/value da lista dos gols
jogador['total de gols'] = sum(gols)
print('__'*20)
print(jogador)
print('__'*20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('__'*20)
print(f'O jogador {jogador['nome']} jogou {partidas} partidas.') #aqui ao inves de partidas, eu poderia colocar o len a lista que tem os gols de cada partida
for pos, v in enumerate(jogador['gols do jogador']):
    print(f'Na partida {pos+1}, fez {v} gols.')
print(f'O jogador {jogador['nome']} fez um total de {jogador["total de gols"]} gols.')
