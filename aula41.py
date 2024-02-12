""" while/else """

string = 'MACACO'

i = 0
while i < len(string):
    letra = string[i]

    if letra == 'CA':
        break

    print(letra)

    i += 1
else:
    print('macaco saiu')