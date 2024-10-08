def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} é de {area}m².')
    print('-' * 45)
    print('Encerrado'.center(45, '-'))

print('Calculadora de m²'.center(45, '-'))
print('-'*45)
l = float(input('Qual largura (m): '))
c = float(input('Qual comprimento (m): '))
area(l, c)

