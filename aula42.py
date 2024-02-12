frase = 'O python é uma linguagem de programação ' \
        'multiparadigma. ' \
        'Python foi criado por Guido van Rossum'

i = 0
apareceu_mais = 0
letra_mais = ''
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
     i += 1
     continue

    qts_letras = frase.count(letra_atual)

    if apareceu_mais < qts_letras:
        apareceu_mais = qts_letras
        letra_mais = letra_atual

    i += 1

print(f'A letra que apareceu mais vezes foi "{letra_mais}" e apareceu {apareceu_mais}X')