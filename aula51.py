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

lista_a = [1,2,3]

lista_b = [4,5,6]

lista_c  = lista_a + lista_b

lista_d = lista_a.extend(lista_b)

print(lista_c)

print(lista_a)