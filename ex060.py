# ex060  Cálculo do Fatorial
# minha 1 solução

import os
from time import sleep
os.system('cls' if os.name == 'nt' else 'clear')

f = 1
n = int(input('Digite um número para calcular seu fatorial: \033[1;32m'))
print(f'\033[mCalculando {n}! =', end = '') 

for c in range(n, 0, -1):
    f *= c
    print(f' {c} ', end = 'x')

print(f' = {f}')
print('\n')

# minha 2 solução

# os.system('cls' if os.name == 'nt' else 'clear')

n = int(input('Digite um número para calcular seu fatorial: \033[1;32m'))
print('\033[mCalculando...')
sleep(1)

# 1 solução curso em video

from math import factorial
n = int(input('Digite um número para cacular seu fatorial: \033[1;32m'))
f = factorial(n)
print(f'\033[mO fatorial de {n} é {f}')


# 2 solução curso em video


