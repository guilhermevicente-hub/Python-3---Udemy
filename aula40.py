# Calculadora com while

while True:

    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite o operador para conta: ')

    num_val = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        num_val = True
    except:
        num_val = None


    if num_val is None:
        print('numeros invalidos')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    ##########
    print('Realizando sau conta. Confira o resultado abaixo: ')

    if operador == '+':
        print(f'{num_1_float} + {num_2_float} =', num_1_float + num_2_float)
    elif operador == '/':
        print(f'{num_1_float} + {num_2_float} =', num_1_float / num_2_float)
    elif operador == '-':
        print(f'{num_1_float} + {num_2_float} =', num_1_float - num_2_float)
    elif operador == '*':
        print(f'{num_1_float} + {num_2_float} =', num_1_float * num_2_float)

    sair = input('Quer sair ? [s]im: ')
    sair = sair.lower()
    sair = sair.startswith('s')

    if sair is True:
        break





