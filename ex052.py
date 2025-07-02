import os
from time import sleep

os.system('cls' if os.name == 'nt' else 'clear')
cont = 0

print ('\033[1;32m=' * 66)
print('\033[1;33m>' * 25 ,'\033[1;34mNÚMEROS PRIMOS', '\033[1;33m<' * 25)
print ('\033[1;32m=' * 66)
print('\033[m')
num = int(input('Digite um número: \033[1;34m'))
print('\033[m')
sleep(0.2)
print('\033[1;32mAnalisando...')
print('\033[m')
sleep(0.5)
for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[1;32m{c}\033[m', end='\033[1;35m ► \033[m')  # alt + 16
        cont += 1
    else:
        print(f'\033[1;31m{c}\033[m', end='\033[1;35m ► \033[m')  # alt + 16
print('\033[1;33mFIM\033[m\n')

if cont == 2:
    print(f'O número \033[1;33{num}\033[m foi divisível \033[1;32m{cont} \033[mvezes')
    print(f'E por isso \033[1;32mÉ PRIMO!')
else:
    print(f'O número \033[1;33{num}\033[m foi divisível \033[1;31m{cont} vezes\033[m.')
    print(f'E por isso \033[1;31mNÃO É PRIMO!')
sleep(0.5)
print('\033[m')
print('\033[1;32m=' * 66)
print('\033[1;33m>' * 25 ,'\033[1;34mFIM DO PROGRAMA', '\033[1;33m<' * 24)
print('\033[1;32m=' * 66)