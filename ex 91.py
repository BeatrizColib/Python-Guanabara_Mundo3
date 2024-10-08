from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
ranking = []
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #ele criou uma lista para deixar na ordem crescente
#colocando os itens do dic jogo em ordem(sorted)(reverse, decrescente), tomando como referencia o indice 1, que
#no caso é numero, e o 0 é o jogador, para isso, precisa importar o itemgetter da biblioteca operator. e entre
#parenteses, diz qual o indice para ser tomado como referencia -> itemgetter(1)
print('#'*30)
print('RANKING JOGADORES')
for i, v in enumerate(ranking):
    print(f'O {i+1}º lugar foi do {v[0]}, tirou {v[1]}')