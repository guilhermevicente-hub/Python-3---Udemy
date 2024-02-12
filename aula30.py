"""
CONSTANTE = "Variaveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)

"""

velocidade = 61 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 esta
RADAR_RANGE = 1 # A distancia onde o radar pega

vel_carro_r1 = velocidade > RADAR_1
carro_passou_r1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado = carro_passou_r1 and vel_carro_r1

if vel_carro_r1:
    print('Velocidade carro passou do radar 1')

if carro_passou_r1:
    print('Carro passou radar 1')


if carro_multado:
    print('Carro multado em radar 1')