from time import sleep
import random
import os

os.system('cls' if os.name == 'nt' else 'clear')
sleep(1)
for c in range(10, -1, -1):
    cor = random.randint(31, 36)
    print(' ' * 21, '\033[1;' + cor + 'm' c)
    print('\033[m', end='\r')
    sleep(1)
print('\n')
print(' ' * 10, '\033[1;33mBUUMM!!! \033[1;32mPOW!!! \033[1;31mBANG!!!')
print('\033[m')
print('\n' * 3)