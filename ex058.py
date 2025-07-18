 # ex058
from time import sleep
import random

tentativas = 0
print('Sou seu computador...')
sleep(0.5)
print('Estou pensando em um número entre 0 e 10...')
sleep(1)
print('Será que você consegue adivinhar qual foi?')
palpite = int(input('Qual é o seu palpite: \033[1;32m'))
print('\033[m')
numero = random.randint(0, 10)
