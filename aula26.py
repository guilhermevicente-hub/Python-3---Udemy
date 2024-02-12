"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere) (><^) (quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>100,.1f
Conversion flags - !r !s !a
"""

var = 'ABC'
print(f'{var}')
print(f'{var: >10}')
print(f'{var: <10}.')
print(f'{var: ^11}')
print(f'O Hexadecimal de 1500 é {1500:08X}') 