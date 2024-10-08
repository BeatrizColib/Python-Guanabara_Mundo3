from random import randint
qnt = int(input('Quantos jogos você quer que eu sorteie: '))
todos_jogos = []
for c in range(0, qnt):
    jogo = []
    while len(jogo) < 6:
        num = randint(1,60)
        if num not in jogo:
            jogo.append(num)
    todos_jogos.append(jogo)
for i, v in enumerate(todos_jogos):
    print(f'Jogo {i+1} foi: {sorted(v)}')