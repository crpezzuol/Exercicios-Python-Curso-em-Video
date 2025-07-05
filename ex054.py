
import os
import datetime

os.system('cls' if os.name == 'nt' else 'clear')
hoje = datetime.date.today().year

# Solicita a idade de 7 pessoas e calcula a quantidade de maiores e menores de idade
for c in range (1, 8):
    idade = int(input(f'Digite a idade da {c}ª pessoa: '))
    