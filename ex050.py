import os
from time import sleep

soma = 0  # s = soma dos números pares solicitados

os.system('cls' if os.name == 'nt' else 'clear')
print('\n' * 3)

print('\033[1;31m=' * 24, '\033[34mSOMA DOS NÚMEROS PARES', '\033[1;31m=' * 24)
print('\n\033[m')

for c in range(1, 7):
    num = int(input(f'Digite o {c}º número inteiro: '))
    for i in range(2, num+1, 2):
        print (f'Número par: {i}')
        if num == i:
            soma += num
print(f'A soma dos números pares digitados é: {soma}')
print('\n' * 3)