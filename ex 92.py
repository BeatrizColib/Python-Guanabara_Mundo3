from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: ')).strip()
ano_nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - ano_nasc
dados['ctps'] = int(input('Número da CTPS (Digite 0 caso não possua): '))
if dados['ctps'] != 0:
    dados['ano de contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['idade da aposentadoria'] = dados['ano de contratação'] + 35 - ano_nasc
print('-='*30)
for k, v in dados.items():
    print(f'- {k.capitalize()} -> {v}')
