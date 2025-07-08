# ex056
import os

os.system('cls' if os.name == 'nt' else 'clear')

media_idade = 0
soma_idade = 0  
maior_idade = 0 
nome_maior_idade = ''


for c in range(1, 5):
    print(f'{"\033[1;34m>" * 10} \033[1;35m{c}ª PESSOA {"\033[1;34m<" * 10}')
    print('\033[m')
    nome = str(input(f'Digite seu NOME: \033[1;32m')).strip().capitalize()
    idade = int(input(f'\033[mDigite a idade de {nome}: \033[1;32m'))
    sexo = str(input(f'\033[mDigite o sexo de {nome} (M/F): \033[1;32m')).strip().upper()
    print('\033[m')
    soma_idade += idade

print(f'Amédia de idade do grupo: \033[1;32m{soma_idade / 4:.2f}\033[m anos')