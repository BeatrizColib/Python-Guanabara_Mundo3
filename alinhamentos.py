text = "Texto"
print(text.ljust(50))  # Alinha à esquerda com 50 caracteres de largura
print(text.ljust(50, '-'))  # Alinha à esquerda e preenche com hífens

print(text.rjust(50))  # Alinha à direita com 50 caracteres de largura
print(text.rjust(50, '*'))  # Alinha à direita e preenche com asteriscos

print(text.center(50)) #centraliza
print(text.center(50, '-')) #centraliza e preenche com o símbolo entre as aspas

numero = "42"
print(numero.zfill(5))  # Preenche com zeros à esquerda até atingir 5 caracteres
preenchido_direita = numero.ljust(5, '0')  # Preenche com zeros à direita até atingir 5 caracteres
print(preenchido_direita)

espacos = "   Texto com espaços   "
print(espacos.strip())  # Remove espaços de ambos os lados
print(espacos.lstrip())  # Remove espaços à esquerda
print(espacos.rstrip())  # Remove espaços à direita

frase = "Olá, Bia!"
print(frase.replace("Bia", "Biazinha :)"))  # Substitui "Mundo" por "Python"

texto = "Olá Mundo"
print(texto.upper())  # Tudo maiúsculo
print(texto.lower())  # Tudo minúsculo
print(texto.title())  # Capitaliza cada palavra
print(texto.capitalize())  # Apenas a primeira letra em maiúsculo

frase = "Isso é uma frase"
lista_palavras = frase.split()  # Divide em palavras
print(lista_palavras)
novafrase = '-'.join(lista_palavras)  # Junta com hifens
print(novafrase)
novafrase2 = ' '.join(lista_palavras) # junta sem hífens
print(novafrase2)

url = "https://example.com"
print(url.startswith("https"))  # Verifica se começa com "https"
print(url.endswith(".com"))  # Verifica se termina com ".com"
#str.startswith(prefix) / str.endswith(suffix):
#Verifica se uma string começa com um determinado prefixo ou termina com um determinado sufixo.


