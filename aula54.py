"""
Exercicio
Exiba os indices da lista
0 Guilherme
1 Silva
2 Vicente
"""

lista = ['Guilherme', 'Silva', 'Vicente']

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))