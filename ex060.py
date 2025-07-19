# ex060  Cálculo do Fatorial
# minha solução

import os

os.system('cls' if os.name == 'nt' else ' clear')
c = 0
n = int(input('Digite um número para calcular seu fatorial: \033[1;32m'))
while c != n:
    print(f'\033[mCalculando {n}! =', end = ' ')
    for c in range(n +1, 0, -1):
        print(f'{n} x ', end = '')

        
    break
