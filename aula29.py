"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero = input('digite um numero: ')

try:
    print('STR:', numero)
    numero_float = float(numero)
    print('FLOAT', numero_float)
    print(f'o dobro do {numero} e {numero_float * 2:.2f}')
except:
    print('Isso não e um numero.')


# if numero.isdigit():
#     numero_float = float(numero)
#     print(f'o dobro do {numero} e {numero_float * 2:.2f}')
# else:
#     print('Isso não e um numero.')


