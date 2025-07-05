
import os

os.system('cls' if os.name == 'nt' else 'clear')


# Exercicio 055 - Maior e Menor Peso
for c in range(1, 8):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso    
print(f'O maior peso lido foi {maior}kg')
print(f'O menor peso lido foi {menor}kg')