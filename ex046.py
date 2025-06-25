from time import sleep
import os

os.system('cls' if os.name == 'nt' else 'clear')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
