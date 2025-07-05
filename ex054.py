
import os
import datetime

os.system('cls' if os.name == 'nt' else 'clear')
hoje = datetime.date.today().year

# Solicita a idade de 7 pessoas e calcula a quantidade de maiores e menores de idade
for c in range (1, 8):
    nascido = int(input(f'Digite a idade da {c}ª pessoa: '))
    idade = hoje - nascido
    if nascido >= 18:
        maior += 1
    else:
        menor += 1
print(f'Temos {maior} pessoas maiores de idade e {menor} pessoas menores de idade.')