 # ex058
import os
from time import sleep
import random


tentativas = 0
os.system('cls' if os.name == 'nt' else 'clear')
print('>' * 20, 'JOGO DE ADIVINHAÇÃO', '<' * 20)
print('Sou seu computador...')
sleep(0.5)
print('Estou pensando em um número entre 0 e 10...')
sleep(1)
print('Será que você consegue adivinhar qual foi?\n')
numero = random.randint(0, 10)
print(numero)
palpite = int(input('Qual é o seu palpite? : \033[1;32m'))
print('\033[m')


tentativas += 1
while palpite != numero:
    if palpite < numero:
        tentativas += 1
        print('Mais... Tente mais uma vez!')
        palpite = int(input('Qual é o seu palpite? : \033[1;32m'))
        print('\033[m')
    else:
        palpite > numero
        tentativas += 1
        print('Menos... Tente mais uma vez!')
        palpite = int(input('Qual é o seu palpite? : \033[1;32m'))
        print('\033[m')
if tentativas == 1:
    print(f'Você acertou apenas com {tentativas} tentativa, isso foi INCRIVEL!!!' )
print(f'Acertou com {tentativas} tentativas, Parabéns!!!')
print('\n')
