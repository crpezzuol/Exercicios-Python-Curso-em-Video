import os
from time import sleep  
os.system('cls' if os.name == 'nt' else 'clear')
print('\n' * 3)
print('\033[1;31m=' * 20, '\033[34mTABUADA', '\033[1;31m=' * 20)
print('\n\033[m')
num = int(input('Digite um número para ver sua tabuada: \033[1;32m'))
print('\n\033[m')
for c in range(1, 11):
    print(f'{num} x {c:2} = {num * c:3}')
print('\n' * 3)
