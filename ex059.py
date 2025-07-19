# ex059 Criando um Menu de Opções
# minha solução

import os
os.system('cls' if os.name == 'nt' else 'clear')

valor_1 = int(input('Digite o primeiro valor: \033[1;32m'))
valor_2 = int(input('\033[mDigite o segundo valor: \033[1;32m'))
print('\033[m=-=' * 11)
print('    [ 1 ] Somar' 
'\n    [ 2 ] Multiplicar' 
'\n    [ 3 ] Maior' 
'\n    [ 4 ] Novos números' 
'\n    [ 5 ] Sair do Programa\n')
opcao = int(input('>>>>> Qual é a sua opção? \033[1;32m'))
print('\033[m')
while opcao == 1:
    print(f'A soma entre {valor_1} + {valor_2} é {valor_1 + valor_2}')
    break
print('=-=' * 11)
    while opcao == 2:
        print(f'A multiplicação entre {valor_1} * {valor_2} é {valor_1 * valor_2}')
        
print('\n')
