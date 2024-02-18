"""
Cuidado com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ['guilherme', 'ariel']

lista_b = lista_a.copy()

lista_a[0] = lista_a[0].upper()

print(lista_b)
