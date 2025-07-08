# ex056
import os

os.system('cls' if os.name == 'nt' else 'clear')

media_idade = 0
soma_idade = 0  
maior_idade = 0 
nome_maior_idade = ''
fem_menor_20 = 0


for c in range(1, 5):
    print(f'{"\033[1;34m>" * 10} \033[1;35m{c}ª PESSOA {"\033[1;34m<" * 10}')
    print('\033[1;34m>' * 15 + '\033[1;35mX\033[m' + '\033[1;34m<' * 15)
    print('\033[m')
    nome = str(input(f'Digite seu NOME: \033[1;32m')).strip().capitalize()
    idade = int(input(f'\033[mDigite a idade de {nome}: \033[1;32m'))
    sexo = str(input(f'\033[mDigite o sexo de {nome} (M/F): \033[1;32m')).strip().upper()
    print('\033[m')
    soma_idade += idade
    if c == 1 and sexo == 'M':
        maior_idade = idade
        nome_maior_idade = nome
    elif sexo == 'M' and idade > maior_idade:
        maior_idade = idade
        nome_maior_idade = nome
    elif sexo == 'F' and idade < 20:
        fem_menor_20 += 1

print(f'A média de idade do grupo: \033[1;32m{soma_idade / 4:.1f}\033[m anos')
print(f'O homem mais velho é \033[1;32m{nome_maior_idade}\033[m com \033[1;32m{maior_idade}\033[m anos.')
print(f'Ao todo são \033[1;32m{fem_menor_20}\033[m de mulheres com menos de 20 anos.')

print('\n')