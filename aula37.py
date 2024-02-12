"""
Repetições
while(enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um codigo não tem fim
"""

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        continue

    print(contador)

    if contador == 40:
        break

print('FIM!!!')