tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze','treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('Digite um número entre 0 e 20: ')) 
    if 0 <= numero <= 20:
        print(f'O número que você digitou foi {tupla[numero]}')
    else:
        numero = int(input('Erro! Digite um número inteiro entre 0 e 20: '))
    continuar = str(input('Gostaria de continuar? Sim ou Não: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Digite uma opção válida: Sim ou Não: ')).upper().strip()[0]
    if continuar == 'N':
        break
print('Até breve!')