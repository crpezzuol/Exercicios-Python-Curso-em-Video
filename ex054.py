# Exemplo de código para calcular a quantidade de maiores e menores de idade
import os
import datetime

os.system('cls' if os.name == 'nt' else 'clear')
hoje = datetime.date.today().year
maior = 0   # Contador de maiores de idade
menor = 0   # Contador de menores de idade
idade = 0  # Variável para armazenar a idade calculada

print('\033[1;34m-=' * 55)
print('\033[1;35m>' * 30,'\033[1;31mV e r i f i c a d o r  de  M a i o r i d a d e\033[m', '\033[1;35m<' * 30)
print('\033[1;34m-=' * 60)

print('\033[1;32mVamos verificar a maioridade de 7 pessoas!\033[m')
print('\n')
print('Digite a idade de cada pessoa, e o programa irá calcular quantas são maiores e menores de idade.')


# Solicita a idade de 7 pessoas e calcula a quantidade de maiores e menores de idade
for c in range (1, 8):
    nascido = int(input(f'Digite a idade da {c}ª pessoa: \033[1;32m'))
    print('\033[m')
    # Calcula a idade com base no ano atual
    idade = hoje - nascido
    if idade < 18:
        menor += 1
    else:
        maior += 1
print(f'Ao todo tivemos \033[1;32m{maior}\033[m pessoas maiores de idade.')
print(f'E também \033[1;33m{menor}\033[m pessoas menores de idade.')
print('\n')