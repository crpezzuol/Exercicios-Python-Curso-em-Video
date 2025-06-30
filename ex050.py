import os
from time import sleep

os.system('cls' if os.name == 'nt' else 'clear')

soma = 0  # s = soma dos números pares
cont = 0  # tn = total de números solicitados

for c in range(1, 7):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'\nA soma dos {cont} números pares digitados é: {soma}.')
print('\n' * 3)