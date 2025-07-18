import os
from time import sleep  

os.system('cls' if os.name == 'nt' else 'clear')
print('\n' * 3)

print('\033[1;31m=' * 24, '\033[34mTABUADA', '\033[1;31m=' * 24)
 
print('\n\033[m')

num = int(input('Digite um número para ver sua tabuada: \033[1;32m'))
print('\n\033[m')
sleep(0.5)  # Atraso de 0.5 segundos antes de iniciar a tabuada

for c in range(1, 11):
    print(f'{num} x {c:2} = \033[1;32m{num * c:3}\033[m')
    sleep(0.3)  # Atraso de 0.3 segundos entre os números

print('\n') 
print('\033[1;31m=' * 20, '\033[34mFIM DA TABUADA', '\033[1;31m=' * 21)
print('\n' * 3, '\033[m')
