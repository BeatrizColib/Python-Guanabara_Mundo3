cbp = 'Flamengo', 'Vasco', 'Fluminense', 'Botafogo RJ', 'Botafogo SP', 'Palmeiras', 'Corinthias', 'São Paulo', 'Galo', 'Campinense', 'Chapecoense', 'Natal', 'Atlético Mineiro', 'Atlético Paranaense', 'Grêmio', 'Goias', 'Vitória', 'Bahia', 'Nautico', 'Sport'

print('-='*50)
print(f'Lista de times do Brasileirão: {cbp}')
print('-='*50)
print(f'Os primeiro 5 colocados são: {cbp[:5]}')#até o quinto colocado - posiçao 0 a 4
print(f'Os últimos 4 colocados são: {cbp[-4:]}') #os ultimos quatro
print(f'Em ordem alfabética: {sorted(cbp)}') #ordem alfabética
print(f'O time da Chapecoense está em {cbp.index('Chapecoense') + 1}º lugar')
