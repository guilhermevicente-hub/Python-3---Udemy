"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

# v1 = 'a'
# v2 = '1'
# print(id(v1))
# print(id(v2))

condição = True
passou = None

if condição:
    passou = True
    print('Faça algo')
else:
    print('Não faça algo')

print(passou, passou is None)
print(passou, passou is not None)