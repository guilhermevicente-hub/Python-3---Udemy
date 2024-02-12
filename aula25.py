"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e x - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Guilherme'
preco = 1000.9587456
variavel = '%s, o preço é R$%d' % (nome, preco)
print(variavel)

print('O Hexadecimal de %d é %04X' % (150000, 150000)) 