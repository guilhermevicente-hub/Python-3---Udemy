"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Guilherme', 'Silva', 'Vicente']
lista.append('Ariel')


for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)
    
    
