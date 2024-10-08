teste = list()
teste.append('gustavo')
teste.append(40)
galera = list()
#galera.append(teste) # assim ele link as duas listas e elas mudam juntas
galera.append(teste[:]) #assim cria uma copia e o que alterar em uma, nao irá se alterar na outra
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(teste)
print(galera)
teste[0] = 'Marcela'
teste[1] = 19
galera.append(teste[:])
print(galera)
###########################################
pessoas = [['joao', 19],['ana', 22],['rafa', 13],['pedro', 7]]
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade')
####################################
alunos = list()
dados = list()
totmaior = totmenor = 0
for c in range(0,3):
    dados.append(str(input('nome: ')))
    dados.append(int(input('idade: ')))
    alunos.append(dados[:])
    dados.clear()
for p in alunos:
    if p[1] >=21:
        print(f'{p[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1
print(f'temos {totmaior} pessoas maiores de idade e {totmenor} menores de idade.')