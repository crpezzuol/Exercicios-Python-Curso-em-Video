import os
from time import sleep

tn = 0 # tn = total de números solicitados
s = 0 # s = soma dos números solicitados

os.system('cls' if os.name == 'nt' else 'clear')

print('Soma dos números ímpares múltiplos de 3 no intervalo de 1 a 500')
print('\n')

for c in range(1, 501, 2):  # Percorre os números de 1 a 500, pulando de 2 em 2 (ou seja, só os ímpares)
    if c % 3 == 0:
        s += c  # Soma os números ímpares múltiplos de 3
        tn += 1

print(f'A soma de todos os {tn} valores solicidados é: {s}')
print('\n')
