"""
Repetições 
while (enquanto)
Executa uma ação enquanto um condição for verdadeira
loop infinito -> Quando um codigo não tem fim
"""

condicao = True

while True:
    nome = input('qual o seu nome:')
    print(f'Seu nome e {nome}')

    if nome == 'sair':
        break

print('Acabou')