# Exercicio 055 - Maior e Menor Peso
import os

os.system('cls' if os.name == 'nt' else 'clear')

maior = 0
menor = 0

print('=' * 30)
print('>' * 10 + 'Maior e Menor Peso', '<' * 10)
print('=' * 30)

for c in range(1, 8):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso    
print(f'O maior peso lido foi {maior}kg')
print(f'O menor peso lido foi {menor}kg')
print('\n')