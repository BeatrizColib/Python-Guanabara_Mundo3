nomes = ('raissa','beatriz','faynara','anne','ana','raquel','julio','juli','lili','mulbia','vildomar','rita','andre','tadeu')
vogais = 'aeiou'
for nome in nomes:
    print(f'\nNo nome \033[35m{nome.title()}\033[m temos: ', end='')
    for letra in nome:
        if letra in 'aeiou': #se for para add com acentuação é so escrever ãâá ...
            print(f'\033[31m{letra}\033[m ', end='')