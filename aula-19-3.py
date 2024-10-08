state = dict()
brazil = list()

for c in range(0,2):
    state['st'] = str(input('State: '))
    state['acronym'] = str(input('Acronym: '))
    state['population'] = float(input('Population: '))
    brazil.append(state.copy())
print(brazil)

for s in brazil:
    print(s)

for s in brazil: #para cada estado na lista brasil:
    for k, v in s.items(): # para cada chave e valor na estado.items(): - ou seja, para cada estado, ele fará essa ação,
        print(f'O campo {k} tem resposta {v}.')