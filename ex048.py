import os
from time import sleep

cont = 0 # tn = total de números solicitados
soma = 0 # s = soma dos números solicitados

os.system('cls' if os.name == 'nt' else 'clear')

print('\n')
print('Soma dos números ímpares múltiplos de 3 no intervalo de 1 a 500:')
print('\n')

for c in range(1, 501, 2):  # Percorre os números de 1 a 500, pulando de 2 em 2 (ou seja, só os ímpares)
    if c % 3 == 0:
        soma += c  # Soma os números ímpares múltiplos de 3
        cont += 1

print(f'A soma de todos os {cont} valores solicidados é: {soma}.')
print('\n')
