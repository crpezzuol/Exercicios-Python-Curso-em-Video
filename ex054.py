# Exemplo de código para calcular a quantidade de maiores e menores de idade
import os
import datetime

os.system('cls' if os.name == 'nt' else 'clear')
hoje = datetime.date.today().year
maior = 0   # Contador de maiores de idade
menor = 0   # Contador de menores de idade
idade = 0  # Variável para armazenar a idade calculada

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
print(f'Ao todo tivemos {maior} pessoas maiores de idade.')
print(f'E também {menor} pessoas menores de idade.')
print('\n')