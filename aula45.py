"""
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor 
iter -> me entregue seu iterador
"""


texto = 'MACACO'
iterador = iter(texto)

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break


###################### mesma coisa #########################

for letra in texto:
    print(letra)




