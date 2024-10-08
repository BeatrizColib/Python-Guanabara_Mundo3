people = {'Name': 'Bia', 'Gender': 'Female', 'Age': 31}
print(f'A/o {people['Name']} tem {people['Age']} years.')
print(people.keys())
print(people.values())
print(people.items())

for k in people.values():
    print(k)

for k, v in people.items(): #no dic não se usa o enumerate, coloca-se o for com .items()
    print(f'{k} = {v}')

del people['Gender']
people['Name'] = 'Beatriz'
people['Weight'] = '55.5 kg'
print(people)