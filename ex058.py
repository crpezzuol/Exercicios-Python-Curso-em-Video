 # ex058
import os
from time import sleep
from random import randint

# minha solução

palpites = 0
os.system('cls' if os.name == 'nt' else 'clear')
print('>' * 20, 'JOGO DE ADIVINHAÇÃO', '<' * 20, '\n')
print('Sou seu computador...')
sleep(0.5)
print('Estou pensando em um número entre 1 e 10...')
sleep(1)
print('Será que você consegue adivinhar qual foi?\n')
jogador = int(input('Qual é o seu palpite? : \033[1;32m'))
print('\033[m')
computador = randint(1, 10)
palpites += 1
while jogador != computador:
    if jogador < computador:
        palpites += 1
        print('Mais... Tente mais uma vez!')
        jogador = int(input('Qual é o seu palpite? : \033[1;32m'))
        print('\033[m')
    else:
        jogador > computador
        palpites += 1
        print('Menos... Tente mais uma vez!')
        jogador = int(input('Qual é o seu palpite? : \033[1;32m'))
        print('\033[m')
if palpites == 1:
    print(f'Você acertou apenas com {palpites} tentativa, isso foi INCRIVEL!!!\n' )
else:
    print(f'Acertou com {palpites} tentativas, Parabéns!!!\n')


# solução curso em video
'''
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')   
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
print(f'Acertou com {palpites} tentativas. Parabéns!')
'''
