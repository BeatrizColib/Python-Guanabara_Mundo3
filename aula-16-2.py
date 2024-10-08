a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #ela junta uma tupla na outra
print(c)
print(sorted(c)) #coloca em ordem as duas juntas
print(c.count(2))  #mostra quantas vezes aparece o '2',
print(c.index(8))  #mostra em que posiçao está o '8' se tem mais de uma ocorrência: mostrará a vez que aparecerá primeiro
print(c.index(5, 1)) #mostra o primeiro 5 a aparecer após a posição 1
print()

# a tupla é imutável, a unica coisa que se pode fazer é apagá-la
# del(nomedatupla) apaga por inteiro