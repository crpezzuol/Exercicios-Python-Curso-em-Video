#
import os
import random
import time

os.system('cls' if os.name == 'nt' else 'clear')

print('\033[1;33m>' * 38 + 'X' + '<' * 38)
print('>' * 30, '\033[1;34mLOTERIA - QUINA', '\033[1;33m<' * 30)
print('>' * 38 + 'X' + '<' * 38)
print('\033[m')
print('\033[1;33m>' * 23, '\033[1;34mESCOLHA 5 NÚMEROS ENTRE 1 E 80', '\033[1;33m<' * 22)
print('\n')

print('\n\033[1;31mAtenção! \033[1;32mVocê só pode escolher números entre 1 e 80.\033[m')
print ('\n')
for i in range(1, 6):
    numero = int(input(f'\033[mDigite o {i}º número: \033[1;32m'))
    if  numero > 80:
        print('\033[1;31mNúmero inválido! Digite um número entre 1 e 80.\033[m')
    
print('\n\033[1;32mSORTEANDO 5 NÚMEROS, AGUARDE...\n')
time.sleep(2)
numeros = random.sample(range(1, 81), 5)
print('\033[1;33mOs números sorteados foram:\033[m', end=' ')
for numero in numeros:
    print(f'\033[1;35m{numero:02d}\033[m', end=' ')

print('\n\033[m')