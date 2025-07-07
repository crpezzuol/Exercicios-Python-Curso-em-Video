# ex056
import os

os.system('cls' if os.name == 'nt' else 'clear')

for c in range(1, 5):
    nome = str(input(f'Digite o nome da {c}ª pessoa: '))
    idade = int(input(f'Digite a idade de {nome}: '))