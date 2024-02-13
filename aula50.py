"""
    
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indices e fatiamento
Métodos úteis: 
append - Adiciona um item ao final
insert - Adiciona um item no indice escolhido
pop - remove do final ou indice escolhido
del - apaga um indice
clear - limpa a lista
extend - estende a lista
+ - concatena listas
create, read, update, delete
criar, ler, alterar, apagar = lista[1] (CRUD)
    
"""


lista = [10,20,30,40]
lista.append('primeiro')
nome = lista.pop()
lista.append(1234)
del lista[-1]
# lista.clear()
lista.insert(0, 'mais um')
print(lista[5])