import os
from time import sleep

os.system('cls' if os.name == 'nt' else 'clear')
print('\n' * 3)
for c in range(1, 7):
    soma = float(input(f'Digite o {c}º número: '))
    