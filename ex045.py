import os
import random

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho():
    print('=' * 30, '\033[1;32mJOKENPÔ\033[m', '=' * 30)
    print('\n\033[m')
    print('''\033[1;34mSuas opções são:\033[m\n
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA
    [3] SAI FORA''')
    print('\n\033[m')

def main():
    limpa_tela()
    cabecalho()
    



main()
