# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy
# 0 0.0 '' False
# Também existe o tipo None que é 
# usado para representar um não valor

# entrada = input('[E]ntrar [S]air: ')
# senha_dig = input('Senha: ')

# senha_perm = '123456'

# if entrada == 'E' and senha_dig == senha_perm:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
print(True and True and False and True)
print(bool(''))
print(True and True and 0 and True)

