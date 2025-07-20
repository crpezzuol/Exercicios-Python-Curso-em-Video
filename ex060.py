# ex060  Cálculo do Fatorial
# minha 1 solução

import os

os.system('cls' if os.name == 'nt' else ' clear')

f = 1
n = int(input('Digite um número para calcular seu fatorial: \033[1;32m'))
print(f'\033[mCalculando {n}! =', end = '') 

for c in range(n, 0, -1):
    f *= c
    print(f' {c} ', end = 'x')

print(f' = {f}')
print('\n')

# 1 solução curso em video