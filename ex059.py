# ex059 Criando um Menu de Opções
# minha solução
from time import sleep
import os
os.system('cls' if os.name == 'nt' else 'clear')

valor_1 = int(input('Digite o primeiro valor: \033[1;32m'))
valor_2 = int(input('\033[mDigite o segundo valor: \033[1;32m'))
opcao = ''
while opcao != '5':
    print('\033[m=-=' * 13)
    print('''        [ 1 ] Somar 
        [ 2 ] Multiplicar
        [ 3 ] Maior
        [ 4 ] Novos números
        [ 5 ] Sair do Programa\n''')
    opcao = str(input('>>>>> Qual é a sua opção? \033[1;32m')).strip()
    print('\033[m')
    while opcao == '1':
        print(f'O resultado de {valor_1} + {valor_2} é igual á {valor_1 + valor_2}.')
        break
    while opcao == '2':
        print(f'O resultado de {valor_1} X {valor_2} é igual á {valor_1 * valor_2}.')
        break
    while opcao == '3':
        if valor_1 == valor_2:
            print(f'Os valores digitados são iguais.')
        elif valor_1 > valor_2:
            print(f'O maior número entre {valor_1} e {valor_2} é o {valor_1}')
        else:
            print(f'O maior número entre {valor_1} e {valor_2} é o {valor_2}.')
        break
    while opcao == '4':
        print('Informe os valores novamente:\n')
        valor_1 = int(input('Digite o primeiro valor: \033[1;32m'))
        valor_2 = int(input('\033[mDigite o segundo valor: \033[1;32m'))
        print('\033[m')
        break
    while opcao == '5':
        print('Finalizando...')
        sleep(1)
        break
    while opcao not in '12345':
        print('Opção inválida. Tente novamente!')
        break
print('=-=' * 13) 
print('\n')
print('Fim do programa! Volte sempre!')       
print('\n')
