from time import sleep
import random
import os

os.system('cls' if os.name == 'nt' else 'clear')

sleep(1)

for c in range(10, -1, -1):
    cor = random.choice(['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m'])
    print(cor)
    print(' ' * 21, c)
    print('\033[m', end='\r')
    sleep(1)
print('\n')
print(' ' * 10, '\033[1;33mBUUMM!!! \033[1;32mPOW!!! \033[1;31mBANG!!!')
print('\033[m')
print('\n' * 3)