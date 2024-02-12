nome = 'Guilherme Vicente'
altura = 1.69
peso = 95
imc = peso/(altura * altura)

# f-strings

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'


# print(nome, 'tem', altura, 'de altura,', 'pesa', peso, 'quilos e seu IMC é:', imc )
print(linha_1)
print(linha_2)
print(linha_3)

