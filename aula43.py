"""
Introdução ao for / in - estrutura de repetição para coisas finitas
"""

# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x)')

#     repeticoes += 1
# print('Laço pode ser infinito')


texto = 'macaco'

novo = ''
for letra in texto:
    novo += f'*{letra}'
print(novo)

