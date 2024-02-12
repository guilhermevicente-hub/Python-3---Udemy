"""
Faça um jogo para o usuario adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar da possibulidade para o 
usuário digitar uma letra.
- Qual o usuário digitar uma letra, você vai conferir
se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver 
    na palavr secreta; exiba *.
Faça a contagem de tentativas do seu usuário
"""


palavra_secreta = 'macaco'
acertadas = ''
tentativa = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    tentativa += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        acertadas += letra_digitada


    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
        
        print('Palavra formada:', palavra_formada)
    
    if palavra_formada == palavra_secreta:
        print('Você ganhou!! Parabens')
        print('A palavra era', palavra_secreta)
        print('Tentativas: ', tentativa)
            
            
            
