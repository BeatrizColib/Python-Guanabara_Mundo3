user = dict()
all_users = list()
sum_age = average = 0

while True:
    user.clear()
    user['name']=str(input("Name: ")).capitalize().strip()
    while True:
        user['gender']=str(input('Gender: Female (F) or Masculine (M): ')).upper()[0].strip()
        if user['gender'] in 'FM':
            break
        print('Error! Please type only F or M')
    user['age']=int(input('Age: '))
    sum_age += user['age']
    all_users.append(user.copy())
    while True:
        proceed = str(input('Do you wish to continue? Yes (Y) or No (N): ')).upper()[0].strip()
        if proceed in "YN":
            break
        print('Error! Answer Y or N!')
    if proceed == "N":
        break

print('-' * 90) #apenas fator estético, para aparece 90x o - após terminar os inputs.
# print(all_users) #assim escreve os usuários na mesma linha

for user in all_users:  # assim escreve os usuários em cada linha
    print(f'User: {user}')

print(f'1- Total registered users: {len(all_users)}')

average = sum_age / len(all_users)
print(f'2- The average age of users is {average:4.2f} years.')

print('3- The women registered were: ', end=' ')
for u in all_users:
    if u['gender'] in 'F':
        print(f'{u['name']}', end='|')
print() #este print vazio dá um enter para a linha abaixo, senão aparecia o item 4 na continuação da linha 3.

print('4- List of people above average age: ')
for user in all_users:
    if user['age'] > average:
        print('', end='') #mostra uma listagem das pessoas acima da média
        for k, v in user.items():
            print(f'{k} = {v}', end=' - ')
        print() # além do enter entre cada k = v, adiciona um 'espaço''parágrafo' a mais entre eles

print()
print('___CLOSED___')