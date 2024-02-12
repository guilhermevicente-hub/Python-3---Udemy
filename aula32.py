"""
Faça um programa que peça ao usuario para digitar um numero inteiro,
informe se este número é  par ou impar. Caso o usuario não digite um numero
inteiro, informe que não é um numero inteiro
"""

# numero = input('Digite um numero: ')

# if numero.isdigit():
#     numero_int = int(numero)
#     par_impar = numero_int % 2 == 0
#     par_impar_txt = 'ímpar'

#     if par_impar is True:
#         par_impar_txt = 'par'

#     print(f'O número {numero_int} e {par_impar_txt}')
# else:
#     print('Você não digitou um numero inteiro')


# numero = input('Digite um numero: ')

# try:
#     numero_int = float(numero)
#     par_impar = numero_int % 2 == 0
#     par_impar_txt = 'ímpar'

#     if par_impar is True:
#         par_impar_txt = 'par'

#     print(f'O número {numero_int} e {par_impar_txt}')
# except:
#     print('Você não digitou um numero inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horario
descrito, exiba a saudação apropriada. EX.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

"""

entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 11 and hora <= 17:
        print('Boa tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite!')
    elif hora == 24:
        print('VAI DURMIR MACACO!')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite um numero inteiro')

    
"""

"""
Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto; se tiver 5 e 6 letras, escreva
"Seu nome e normal"; maior que 6 escreva "Seu nome é muito grande"
"""

nome = input('Digite o primeiro nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('seu nome e curto!')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome e normal!')
    else:
        print('Seu nome e muito grande!')
else:
    print('Digite mais de uma letra!')