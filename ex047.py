# imprimindo numeros pares de 0 a 50
import os
import time

os.system('cls' if os.name == 'nt' else 'clear')

print('Imprimindo números pares de 0 a 50')

for c in range(2, 51, 2):
    time.sleep(0.3)  # Atraso de 0.1 segundos entre os números
    print(c, end=' ')
print('\nFim da contagem de números pares de 0 a 50')
print('\n' * 3)
