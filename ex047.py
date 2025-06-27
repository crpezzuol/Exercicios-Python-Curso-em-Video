# imprimindo numeros pares de 0 a 50
import os
from time import sleep

os.system('cls' if os.name == 'nt' else 'clear')

print('Imprimindo números pares de 0 a 50')
print('\n')
sleep(0.5)
for c in range(2, 51, 2):
    print(' ' * 16, c)
    sleep(0.3)  # Atraso de 0.1 segundos entre os números
print('\nFim da contagem de números pares de 0 a 50')
print('\n' * 3)
