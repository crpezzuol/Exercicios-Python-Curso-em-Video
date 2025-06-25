from time import sleep
import os

os.system('cls' if os.name == 'nt' else 'clear')
sleep(1)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[1;33mBUUMM!!! \033[1;32mPOW!!! \033[1;31mBANG!!!')
print('\033[m')
print('\n' * 3)