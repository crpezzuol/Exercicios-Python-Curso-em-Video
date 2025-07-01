import os
from time import sleep

os.system('cls' if os.name == 'nt' else 'clear')

print ('\033[1;32m=' * 41)
print('\033[1;33m>' * 10 ,'\033[1;34m10 TERMOS DE UMA PA', '\033[1;33m<' * 10)
print ('\033[1;32m=' * 41)
print('\033[m')
primeiro = int(input('Primeiro termo: \033[1;32m'))
print('\033[m')
razao = int(input('Razão: \033[1;32m'))
