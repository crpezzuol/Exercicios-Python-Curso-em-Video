# ex056
import os

os.system('cls' if os.name == 'nt' else 'clear')

for c in range(1, 5):
    print(f'{"-" * 6} \033[1;33m{c}ª PESSOA\033[m {"-" * 6}')
    print('\n')
    nome = str(input(f'Digite seu NOME: '))
    idade = int(input(f'Digite a idade de {nome}: '))
    sexo = str(input(f'Digite o sexo de {nome} (M/F): ')).strip().upper()