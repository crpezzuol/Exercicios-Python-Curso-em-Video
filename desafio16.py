#
import os
import random

os.system('cls' if os.name == 'nt' else 'clear')

print('\033[1;33m>' * 38 + 'X' + '<' * 38)
print('>' * 30, '\033[1;34mLOTERIA - QUINA', '\033[1;33m<' * 30)
print('>' * 38 + 'X' + '<' * 38)
print('\033[m')
print('\033[1;32mSorteando 5 números entre 1 e 80...\033[m')
numeros = random.sample(range(1, 81), 5)


print('\033[m')