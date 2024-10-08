state = dict()
brazil = list()

for c in range(0,2):
    state['st'] = str(input('State: '))
    state['acronym'] = str(input('Acronym: '))
    state['population'] = float(input('Population: '))
    brazil.append(state.copy())

for s in brazil:
    for v in s.values():
        print(v, end=' ')
    print()