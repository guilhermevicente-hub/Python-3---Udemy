"""
Exercicio
Peça ao usuario para diitar seu nome
Pela para o usuario digitar sua idade 
Se o nome e idade forem digitados:

    Exiba
    Seu nome e {nome}
    Seu nome invertido é {nome_inv}
    Se contem (ou não) espaços
    Seu nome tem {n} letras 
    A primeira letra do seu nome é {letra}
    A ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    Exiba "Desculpe, você deixou campos vazios."

"""


nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome e : {nome}')
    print(f'Seu nome invertido e : {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contem espaços')

    print(f'Seu nome tem {len(nome)} letras ')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")



