# Exemplo de código para calcular a quantidade de maiores e menores de idade
import os
import datetime

os.system('cls' if os.name == 'nt' else 'clear')
hoje = datetime.date.today().year
maior = 0   # Contador de maiores de idade
menor = 0   # Contador de menores de idade
idade = 0  # Variável para armazenar a idade calculada

print('\033[1;34m-=' * 20)
print('\033[1;34m Verificador de Maioridade \033[m')
print('\033[1;34m-=' * 20)

print('Verificador de Maioridade')

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