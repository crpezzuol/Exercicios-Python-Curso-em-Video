# Exercicio 055 - Maior e Menor Peso
import os

os.system('cls' if os.name == 'nt' else 'clear')

maior = 0
menor = 0

print('\033[1;33m=' * 50)
print('>' * 15, '\033[1;32mMaior e Menor Peso', '\033[1;33m<' * 15)
print('=' * 50)
print('\033[m')

for c in range(1, 8):
    peso = float(input(f'Peso da {c}ª pessoa: \033[1;34m'))
    print('\033[m')
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso    
print(f'O maior peso lido foi \033[1;31m{maior}\033[m kg.')
print(f'O menor peso lido foi \033[1;32m{menor}\ kg')
print('\n')